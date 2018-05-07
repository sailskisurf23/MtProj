import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from surprise import SVD, SVDpp, Dataset, accuracy, Reader
from surprise.model_selection import train_test_split, GridSearchCV

######################### Statistics ##########################

def unq_u_r(df):
    '''
    Return number of users and routes in df
    '''
    return df['user'].nunique(), df['route'].nunique()

def better_sample(df,u=10000,r=20000):
    '''
    Return return random sample of DataFrame containing u-users and r-routes
    '''
    user_sample = np.random.choice(np.array(df.groupby('user').count().index),u,replace=False)
    route_sample = np.random.choice(np.array(df.groupby('route').count().index),r,replace=False)
    return df[(df['user'].isin(user_sample)) & (df['route'].isin(route_sample))]

def ru_counts(df):
    '''
    For each climb, count number of users that rated it,
    and for each user, count number of climbs they rated

    ---Parameters---
    df: Pandas DataFrame

    ---Returns--
    u_r_counts: Pandas Series
    r_u_counts: Pandas Series
    '''
    u_r_counts = df.groupby(['user']).count()['route']
    r_u_counts = df.groupby(['route']).count()['user']
    return u_r_counts,r_u_counts

def mat_density(df):
    '''
    Compute density of sparse matrix
    '''
    n_route , n_user = unq_u_r(df)
    mat_size = n_route * n_user
    return df.shape[0] / mat_size

def pr_mat_stats(df, title="Matrix Stats"):
    '''
    Print size, shape and density of matrix
    '''
    n_route , n_user = unq_u_r(df)
    mat_size = n_route * n_user
    density = mat_density(df)
    print(title)
    print('---------------------')
    print('matrix size: {}'.format(mat_size))
    print('matrix shape: users {}, routes {}'.format(n_user,n_route))
    print('matrix density: {}'.format(density))

def algo_metrics(df):
    '''
    Return metrics algo metrics for df: (rmse,mae,fcp)

    ---Parameters---
    df (Pandas DataFrame) RUS DataFrame
    u (int) Number of ratings threshold for users
    r (int) Number of ratings threshold for routeIDs

    ---Returns---
    metrics (tuple)
    '''
    reader = Reader(line_format='user item rating', sep=',', skip_lines=1)
    data = Dataset.load_from_df(df, reader=reader)
    trainset, testset = train_test_split(data, test_size=.2)
    # Fit out of the box SVD to trainset and predict on test set
    algo = SVD()
    algo.fit(trainset)
    predictions = algo.test(testset)
    return accuracy.rmse(predictions), accuracy.mae(predictions), accuracy.fcp(predictions)

##################### DataFrame Manipulation ######################

def df_add_counts(df):
    '''
    Add columns for counts to df:
    - user ratings per route
    - route ratings per user

    ---Parameters---
    df (Pandas DataFrame) RUS DataFrame
    u (int) Number of ratings threshold for users
    r (int) Number of ratings threshold for routeIDs

    ---Returns---
    df_counts (Pandas DataFrame)
    '''
    # count ratings per user and route
    u_r_counts,r_u_counts = ru_counts(df)
    df_r_ucounts = r_u_counts.reset_index()
    df_r_ucounts.columns = ['route','count_ru']
    df_u_rcounts = u_r_counts.reset_index()
    df_u_rcounts.columns = ['user','count_ur']
    # merge ratings back onto original df
    df_counts = pd.merge(df, df_u_rcounts, on='user')
    df_counts = pd.merge(df_counts, df_r_ucounts, on='route')
    return df_counts

def add_counts_bins(df):
    '''
    Add columns for counts to df:
    - user ratings per route
    - route ratings per user
    - user bins based on number of routes rated

    ---Parameters---
    df (Pandas DataFrame) RUS DataFrame
    u (int) Number of ratings threshold for users
    r (int) Number of ratings threshold for routeIDs

    ---Returns---
    df_counts_bins (Pandas DataFrame)
    '''
    df_counts_bins = df_add_counts(df)
    conditions = [  (df_counts_bins['count_ur'] <= 5),
                    (df_counts_bins['count_ur'] >  5) & (df_counts_bins['count_ur'] <= 10),
                    (df_counts_bins['count_ur'] > 10) & (df_counts_bins['count_ur'] <= 15),
                    (df_counts_bins['count_ur'] > 15) & (df_counts_bins['count_ur'] <= 20),
                    (df_counts_bins['count_ur'] > 20)]
    choices = ['u_bin_0_5', 'u_bin_6_10', 'u_bin_11_15', 'u_bin_16_20', 'u_bin_20+']
    df_counts_bins['u_bin'] = np.select(conditions, choices, default='None')
    return df_counts_bins

def rus_chop(df, u=5, r=5):
    '''
    Chop RUS DF based on minimum cold-start thresholds.

    ---Parameters---
    df (Pandas DataFrame) RUS DataFrame
    u (int) Number of ratings threshold for users
    r (int) Number of ratings threshold for routeIDs

    ---Returns---
    df_chopped (Pandas DataFrame) Chopped RUS DataFrame
    '''
    # count ratings per user and route
    df_counts = df_add_counts(df)
    # chop df based on threshold
    df_chopped = df_counts[(df_counts['count_ur'] >= u) & (df_counts['count_ru'] >= r)]
    return df_chopped[['user','route','num_stars']]

################# Gridsearching, HEAVYLOAD ####################

def thresh_density_arr(df, u=5, r=5):
    '''
    Compute matix density for all combinations of thresholds for range(u),range(r)

    ---Parameters---
    df (Pandas DataFrame) RUS DataFrame
    u (int) Number of ratings threshold for users
    r (int) Number of ratings threshold for routeIDs

    ---Returns---
    density_arr (2d np-array)
    '''
    density_arr = np.zeros((u,r))
    for i in range(u):
        for j in range(r):
            df_chopped = rus_chop(df,i,j)
            density = mat_density(df_chopped)
            density_arr[i,j] = density
    return density_arr

def thresh_metrics_arrs(df, u=5, r=5):
    '''
    Compute metrics for every combination of thresholds

    ---Parameters---
    df (Pandas DataFrame) RUS DataFrame
    u (int) Number of ratings threshold for users
    r (int) Number of ratings threshold for routeIDs

    ---Returns---
    arr_rmse, arr_mae, arr_fcp (tuple of np-arrays)

    '''
    arr_rmse = np.zeros((u,r))
    arr_mae = np.zeros((u,r))
    arr_fcp = np.zeros((u,r))
    for i in range(u):
        for j in range(r):
            df_chopped = rus_chop(df,i,j)
            rmse, mae, fcp = algo_metrics(df_chopped)
            arr_rmse[i,j] = rmse
            arr_mae[i,j] = mae
            arr_fcp[i,j] = mae
    return arr_rmse, arr_mae, arr_fcp



def suprise_gridsearch(data, algo_class, param_grid):
    '''
    Prints off best results & parameters from gridsearch

    ---Parameters---
    data (suprise dataset)
    algo_class (algo_class)
    param_grid (dictionary)
    '''

    gs = GridSearchCV(algo_class, param_grid,
                    measures=['rmse', 'mae'], cv=3, n_jobs=-1)
    gs.fit(data)
    print(gs.best_score['rmse'])
    print(gs.best_params['rmse'])


####################### PLOTTING #################################


def plt_count_hists(df, n=30):
    '''
    Plot hists of rating counts, routes by user and users by route

    ---Parameters---
    df (Pandas DataFrame) RUS DataFrame
    n (int) limit x axis and bin everything to the right
    '''
    u_r_counts,r_u_counts = ru_counts(df)
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(14,5))
    ax1.hist(u_r_counts, bins=list(range(1,n+1)))
    ax1.set_title('Count routes rated by user')
    ax1.set_ylabel('User count')
    ax1.set_xlabel('Number of route ratings')
    ax2.hist(r_u_counts, bins=list(range(1,n+1)))
    ax2.set_title('Count user ratings by route')
    ax2.set_ylabel('Route count')
    ax2.set_xlabel('Number of user ratings')
    plt.show()

def plt_cumsum(df, n=30):
    '''
    Plot proportion of users excluded by varying threshold

    ---Parameters---
    df (Pandas DataFrame) RUS DataFrame
    n (int) limit x axis and bin everything to the right
    '''
    u_r_counts, r_u_counts = ru_counts(df)
    u_r_cumsum = u_r_counts.value_counts().sort_index().cumsum() / unq_u_r(df)[0]
    r_u_cumsum = r_u_counts.value_counts().sort_index().cumsum() / unq_u_r(df)[1]
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(14,5))
    ax1.plot(u_r_cumsum)
    ax1.set_xlim([0, n+1])
    ax1.set_title('Cumsum routes rated by user')
    ax1.set_ylabel('Proportion of users excluded')
    ax1.set_xlabel('Number of route ratings - thresh')
    ax2.plot(r_u_cumsum)
    ax2.set_xlim([0, n+1])
    ax2.set_title('Cumsum user ratings by route')
    ax2.set_ylabel('Proportion of routes excluded')
    ax2.set_xlabel('Number of user ratings - thresh')
    plt.show()

def thresh_heatmap(arr, title):
    '''
    Plot heatmap of a an array of metrics by varying threshold

    ---Parameters---
    arr (np 2d-array)
    title (str)
    '''
    sns.set()
    ax = sns.heatmap(arr)
    ax.set_title(title,size=16)
    ax.set(xlabel='User Threshold',ylabel='Route Threshold')
    plt.show()

def plot_star_counts(df):
    '''
    Plot count of ratings by star value
    '''
    plt.figure(figsize=(10,6))
    plt.bar(list(range(5)),df['num_stars'].value_counts(sort=False))
    plt.xlabel('Star Value')
    plt.ylabel('Counts')
    plt.title('Count of ratings by star value', size=16)
    plt.show()

def hist_star_counts_byroute(df):
    '''
    Plot histogram of routes by average star value
    '''
    plt.figure(figsize=(14,5))
    plt.hist(df.groupby('route').mean()['num_stars'], bins = 10, rwidth=.8)
    plt.xlabel('Star Value')
    plt.ylabel('Counts')
    plt.title('Count of routes by average star value', size=16)
    plt.show()

def scatter_stars_counts(df,cmap):
    df_agg = df.groupby('route').agg(['mean','count'])['num_stars']
    df_agg['meanxcount'] = (df_agg['mean'] * np.log(np.log(df_agg['count'])))**2.5
    plt.figure(figsize=(10,6))
    plt.scatter(df_agg['mean'], df_agg['count'],alpha = 1, cmap=cmap,c=df_agg['meanxcount'])
    plt.xlabel('Star Value')
    plt.ylabel('Counts')
    plt.ylim(0,1250)
    plt.title('Count of Routes by Average Star Value', size=16)
    plt.colorbar(ticks=[0])
    plt.show()

def scatter_stars_counts2(df):
    df_agg = df.groupby('route').agg(['mean','count'])['num_stars']
    df_agg['meanxcount'] = (df_agg['mean'] * np.log(np.log(df_agg['count'])))**2.5
    df_agg1 = df_agg[df_agg['meanxcount'] >= 75]
    df_agg2 = df_agg[df_agg['meanxcount'] < 75]

    plt.figure(figsize=(10,6))
    plt.scatter(df_agg1['mean'], df_agg1['count'], alpha = .7, c='red')
    plt.scatter(df_agg2['mean'], df_agg2['count'], alpha = .7, c='blue')
    plt.xlabel('Star Value')
    plt.ylabel('Counts')
    plt.ylim(0,1250)
    plt.title('Count of Routes by Average Star Value', size=16)

def scatter_stars_counts3(df_agg,cmap):
    df_agg['meanxcount'] = (df_agg['mean'] * np.log(np.log(df_agg['count'])))**2.5
    plt.figure(figsize=(10,6))
    plt.scatter(df_agg['mean'], df_agg['count'],alpha = 1, cmap=cmap,c=df_agg['est'])
    plt.xlabel('Star Value')
    plt.ylabel('Counts')
    plt.ylim(0,1250)
    plt.title('Count of Routes by Average Star Value', size=16)
    plt.colorbar(ticks=[0])
    plt.show()

def scatter_stars_counts4(df,cmap):
    df_agg = df.groupby('route').agg(['mean','count'])['num_stars']
    df_agg['meanxcount'] = (df_agg['mean'] * np.log(np.log(df_agg['count'])))**2.5
    plt.figure(figsize=(10,6))
    plt.scatter(df_agg['mean'], df_agg['count'],alpha = .5)
    plt.xlabel('Star Value')
    plt.ylabel('Counts')
    plt.ylim(0,1250)
    plt.title('Count of Routes by Average Star Value', size=16)
    plt.show()

def violins(algo, testset):
    '''
    Plot violin chart showing descrepancy between true and predicted ratings.
    '''
    predictions = algo.test(testset)
    preds_df = pd.DataFrame(predictions)
    data = [preds_df['est'][preds_df['r_ui'] == rating] for rating in range(1, 5)]
    plt.violinplot(data, range(1,5), showmeans=True)
    plt.xlabel('True Ratings')
    plt.ylabel('Predicted Ratings')
    plt.title('True vs. SVD Recommender Predicted Ratings')
    plt.show()

def plot_errorbars(df):
    '''
    Plot errorbars by userbin
    '''
    df_counts_bins = add_counts_bins(df)
    u_bin_labels = np.array(df_counts_bins.groupby('u_bin').count().index)
    eb_df = df_counts_bins.groupby('u_bin')['num_stars'].agg({'mean' : np.mean, 'std' : np.std})
    plt.figure(figsize=(14,5))
    plt.errorbar(np.arange(5), eb_df['mean'].values, eb_df['std'].values, fmt='ok', lw=3)
    plt.xlim(-1, 5)
    plt.xticks(range(5),u_bin_labels)
    plt.title('Errorbars by Number of Routes Rated')
    plt.show()

def plot_RMSE_userthresh(df, arr_rmse, title, r=0):
    '''
    Plot RMSE by user-coldstart threshold; assumes route threshold = r
    '''
    arr_rmse_df = pd.DataFrame(arr_rmse)
    usersurvivors = []
    for u in range(30):
        usersurvivors.append(unq_u_r(rus_chop(df,u,r))[0])
    usersurvivors_df = pd.DataFrame(usersurvivors,columns=['survivors']).transpose()
    arr_rmse_survivors_df = pd.concat([arr_rmse_df,usersurvivors_df],axis=0).transpose()

    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111)
    ax.plot(arr_rmse_survivors_df[0],c='blue',label='RMSE')
    ax.set_title(title, size=16)
    ax.set_ylim(.6,.75)
    ax.set_xlabel('Cold-start threshold')
    ax.set_ylabel('RMSE')

    ax2 = ax.twinx()
    ax2.plot(arr_rmse_survivors_df['survivors'],c='green',label='Users Retained')
    ax2.set_ylim(0,40000)
    ax2.set_ylabel('Users retained')
    ax2.grid(False)

    plt.show()

def plot_RMSE_routethresh(df, arr_rmse, title, u=0):
    '''
    Plot RMSE by route-coldstart threshold; assumes user threshold = u
    '''
    arr_rmse_df = pd.DataFrame(arr_rmse)
    route_survivors = []
    for r in range(30):
        route_survivors.append(unq_u_r(rus_chop(df,u,r))[1])
    route_survivors_df = pd.DataFrame(route_survivors,columns=['survivors'])
    arr_rmse_survivors_df = pd.concat([arr_rmse_df,route_survivors_df],axis=1)

    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111)
    ax.plot(arr_rmse_survivors_df[0],c='blue',label='RMSE')
    ax.set_title(title, size=16)
    ax.set_ylim(.6,.75)
    ax.set_xlabel('Cold-start threshold')
    ax.set_ylabel('RMSE')
    ax.legend()

    ax2 = ax.twinx()
    ax2.plot(arr_rmse_survivors_df['survivors'],c='green',label='Routes Retained')
    ax2.set_ylim(0,90000)
    ax2.set_ylabel('Users retained')
    ax2.grid(False)

    plt.show()
