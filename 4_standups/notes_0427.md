Hello,

My name is Colin and I'm a Data Scientist!

Since yesterday I accomplished,

1. *combine all scraped mongo dumps locally (still running unfortunately, will get to this EOD)*

2. *get rest endpoints to Ian.. eg json string to and from.*

3. *Combine all scraped mongo dumps locally*

4. *Spin up EC2, get 'hello world' running as response to JSON request.*
  - *Then hardcode 10 routes as JSON response to*
  - *Test with insomnia*

5. *Parse features into route_features.csv*
  - *Do a lot of cleaning*

6. *Create rus_master.csv*

7. *Do Analysis:*
  - *Plot histogram and identify cold starts.
  - Look at sparsity.*
  - Determine threshold for 'cold-start', justify it in note to Dan/Joe
  - Make some Hypotheses about SVD Parameters.
  - grid search params (if initial fit takes >2-3mins, use subset of rus_clean.csv)
  - keep going with Analysis: MOPs, visualizations (look at ratings by user bins)

7. fit model to df_rus (chopped) - use EC2
  - return and pickle df_rup

--- EOD Monday---

8. *Build recommender
  - Read route features in as DF
  - filter routes based on JSON string (return list of routeIDs)*
  - pull in df_rup (predictions matrix) and return top recs (json_handler_v1.py)

9. *Incorporate recommender into Flask app*

--- EOD Weds ---

10. Work on Documentation/ cleaning scripts & NBs

11. Presentation

12. Do NLP analysis
  - Add 'Keywords functionality into App'
