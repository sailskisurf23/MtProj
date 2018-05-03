import pickle
import analysis_helpers as ah
import numpy as np
import pandas as pd
from surprise import AlgoBase, Dataset, evaluate, accuracy, SVD, Reader
from surprise.model_selection import train_test_split

rus_master_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/3_rus/rusfiles/rus_master.csv'
pickle_write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/6_app/algo.pkl'
algo_rids_write_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/algo_rids.csv'

# rus_master_loc = '/home/ec2-user/rusfiles/rus_master.csv'
# pickle_write_loc = '/home/ec2-user/preds.pkl'

def main():
    print('Reading in and chopping data...')
    df = pd.read_csv(rus_master_loc)
    df_chopped = ah.rus_chop(df,5,10)
    reader = Reader(line_format='user item rating', sep=',', skip_lines=1)
    data = Dataset.load_from_df(df_chopped[['user','route','num_stars']], reader=reader)

    print('Training on full data...')
    trainset = data.build_full_trainset()
    algo = SVD()
    algo.fit(trainset)

    print('Writing relevant route_ids')
    algo_rids = pd.DataFrame(df_chopped.groupby('route').count().index)
    algo_rids.to_csv(algo_rids_write_loc,index=None)

    print('Pickling algo...')
    pickle.dump(algo, open(pickle_write_loc, 'wb'))

    print('Done, pickled algo is here: {}'.format(pickle_write_loc))
    print('Route IDs contained in algo are here: {}'.format(algo_rids_write_loc))


if __name__ == '__main__':
    main()
