Hello,

My name is Colin and I'm a Data Scientist!

Over the weekend I scraped a list of most of the routeID's and UserID's from the Website, Mt Project.com

Then I wanted to figure out how to set up a Mongo DB and dump the full content for each 'route' and 'routestats' page into a mongoDB.

I figured out how to do this locally, but I ran out of time to thread this off on an EC2.



Today,

1. I want to get this scraper up and running on an EC2.

2. I'll then build a script to parse userID's and ratings for each route and run it on a portion of the data.

3. I'll then do some basic EDA, looking at the sparsity of the data (how many routes users have rated etc.), then do SVD using surprise to make my first iteration of a recommender on a small subsample of the data.

4. *Lastly, if time permits, I'd like to get a ppt mockup of the front end over to Ian so that I can flesh out what the basic functionality of the recommender should be*

5. Build calendar for 2 week timeframe
