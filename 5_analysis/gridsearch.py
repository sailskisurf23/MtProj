import pandas as pd
import numpy as np
import analysis_helpers as ah
from surprise import NMF, SVD, SVDpp, Dataset, accuracy, Reader
from surprise.model_selection import train_test_split
np.random.seed(2)

rus_master_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/3_rus/rusfiles/rus_master.csv'
#rus_master_loc = '/home/ec2-user/rus_master.csv'

param_grid = {  'n_epochs'  : [100],
                'lr_all'    : [0.002, 0.004, 0.006, 0.008],
                'reg_all'   : [0.06, 0.08, 0.1, 0.2]}

df = pd.read_csv(rus_master_loc)[['user','route','num_stars']]

print('param_grid: {}'.format(str(param_grid)))
df_chopped_u10_r3 = ah.rus_chop(df,10,3)
reader = Reader(line_format='user item rating', sep=',', skip_lines=1)
data = Dataset.load_from_df(df_chopped_u10_r3, reader=reader)
ah.suprise_gridsearch(data, SVDpp, param_grid)
