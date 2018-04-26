Hello,

My name is Colin and I'm a Data Scientist!

Since Monday I accomplished,

1. *get final clean route list*

2. *I want to get this scraper up and running on an EC2.*

3. *I'll then build a script to parse userID's and ratings for each route and run it on a portion of the data.*

4. *Lastly, if time permits, I'd like to get a ppt mockup of the front end over to Ian so that I can flesh out what the basic functionality of the recommender should be*

5. *Build calendar for 2 week timeframe*


Today,

1. combine all scraped mongo dumps locally (still running unfortunately, will get to this EOD)

2. *get rest endpoints to Ian.. eg json string to and from.*

3. *do some basic EDA, looking at the sparsity of the data (how many routes users have rated etc.)*
    - looked at 10k routes > has 100k ratings from 17k users.
    - estimate 100k routes > 1M ratings from 30k Users
      - estimated density 1M / 3B = 1 / 3k; not sure how to evaluate this

4. do SVD using surprise to make my first iteration of a recommender on a small subsample of the data.


% make sure to handle cold start case or just drop those users/ routes
