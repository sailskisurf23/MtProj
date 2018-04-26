Hello,

My name is Colin and I'm a Data Scientist!

Since yesterday I accomplished,

1. combine all scraped mongo dumps locally (still running unfortunately, will get to this EOD)

2. *get rest endpoints to Ian.. eg json string to and from.*

3. *do some basic EDA, looking at the sparsity of the data (how many routes users have rated etc.)*
    - looked at 10k routes > has 100k ratings from 17k users.
    - estimate 100k routes > 1M ratings from 30k Users
      - estimated density 1M / 3B = 1 / 3k; not sure how to evaluate this



Today,

1. combine all scraped mongo dumps locally (still running unfortunately, will get to this EOD)

2. parse all data I need out of the routes pages, create master RUS file

3. do SVD using surprise to make my first iteration of a recommender on a small subsample of the data.




% make sure to handle cold start case or just drop those users/ routes
