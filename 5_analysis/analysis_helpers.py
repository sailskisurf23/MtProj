import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def unq_u_r(df):
    return df['user'].nunique(), df['route'].nunique()

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
    n_route , n_user = unq_u_r(df)
    mat_size = n_route * n_user
    return df.shape[0] / mat_size

def pr_mat_stats(df):
    n_route , n_user = unq_u_r(df)
    mat_size = n_route * n_user
    density = mat_density(df)
    print('matrix size: {}'.format(mat_size))
    print('matrix shape: users {}, routes {}'.format(n_user,n_route))
    print('matrix density: {}'.format(density))


def rus_chop(df,u=5,r=5):
    '''
    Chop RUS DF based on minimum coldstart thresholdself.
    ---Parameters---
    df (Pandas DataFrame) RUS DataFrame
    u (int) Number of ratings threshold for users
    r (int) Number of ratings threshold for routeIDs

    ---Returns---
    df_chopped (Pandas DataFrame) Chopped RUS DataFrame
    '''
    # count ratings per user and route
    u_r_counts,r_u_counts = ru_counts(df)
    df_r_ucounts = r_u_counts.reset_index()
    df_r_ucounts.columns = ['route','count_ru']
    df_u_rcounts = u_r_counts.reset_index()
    df_u_rcounts.columns = ['user','count_ur']
    # merge ratings back onto original df
    df_counts = pd.merge(df,df_u_rcounts, on='user')
    df_counts = pd.merge(df_counts,df_r_ucounts, on='route')
    # chop df based on threshold
    df_chopped = df_counts[(df_counts['count_ur'] >= u) & (df_counts['count_ru'] >= r)]
    return df_chopped[['route','user','num_stars']]

def thresh_density_arr(df,u=5,r=5):
    '''
    '''
    rus_density_thresh = np.zeros((u,r))
    for i in range(u):
        for j in range(r):
            df_chopped = rus_chop(df,i,j)
            density = mat_density(df_chopped)
            rus_density_thresh[i,j] = density
    return rus_density_thresh

def plt_count_hists(df,n=30):
    '''
    Plot hists of u_r_counts and r_u_counts, xlim = n(int)
    '''
    u_r_counts,r_u_counts = ru_counts(df)
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(14,5))

    ax1.hist(u_r_counts, bins=list(range(1,n+1)))
    ax1.set_title('Count routes rated by user')
    ax1.set_ylabel('User count')
    ax1.set_xlabel('Number of route ratings')

    ax2.hist(r_u_counts, bins=list(range(1,n+1)))
    ax2.set_title('Count user ratings by route')
    ax2.set_ylabel('Route count')
    ax2.set_xlabel('Number of user ratings')
    plt.show()

def plt_cumsum(df,n=30):
    '''
    Plot hists of u_r_cumsum and r_u_cumsum, xlim = n(int)
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

def density_heatmap(arr):
    sns.set()
    ax = sns.heatmap(arr)
    ax.set_title('Matrix Density by Cold-start Threshold',size=16)
    ax.set(xlabel='User Threshold',ylabel='Route Threshold')
    plt.show()
