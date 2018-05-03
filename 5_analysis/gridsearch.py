import pandas as pd
import numpy as np
import analysis_helpers as ah
from surprise import SVD, SVDpp, Dataset, accuracy, Reader
from surprise.model_selection import train_test_split
np.random.seed(2)

rus_master_loc = '/Users/colinbrochard/DSI_Capstone_local/MtProjRec/2_data/3_rus/rusfiles/rus_master.csv'
#rus_master_loc = '/home/ec2-user/rus_master.csv'
param_grid = {  'n_epochs': [20, 40],
                'lr_all': [0.005,0.006],
                'reg_all': [0.15,0.2,0.25]}

df = pd.read_csv(rus_master_loc)[['user','route','num_stars']]
# df_better_sample = ah.better_sample(df,12000,32000)

df_chopped_u10_r3 = ah.rus_chop(df,10,3)
reader = Reader(line_format='user item rating', sep=',', skip_lines=1)
data = Dataset.load_from_df(df_chopped_u10_r3, reader=reader)
ah.suprise_gridsearch(data, SVD, param_grid)
