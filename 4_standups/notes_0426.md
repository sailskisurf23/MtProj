Hello,

My name is Colin and I'm a Data Scientist!

Since yesterday I accomplished,

1. combine all scraped mongo dumps locally (still running unfortunately, will get to this EOD)

2. *get rest endpoints to Ian.. eg json string to and from.*

3. *do some basic EDA, looking at the sparsity of the data (how many routes users have rated etc.)*

Today,

1. *Combine all scraped mongo dumps locally*

2. parse all data I need out of the routes pages, grab data I need from API
  - *scrape route data for filters from API (maybe save this for later)*
  - create master RUS file
  - **parse route descriptions & comments**

3. Start working on App with limited number of routes and Naive recommender
  - set up ec2,
  - installing insomnia,
  - get hello world flask app up and running
  - make sure to handle cold start case or just drop those users/ routes
