Hello,

My name is Colin and I'm a Data Scientist!

Since yesterday I accomplished,

1. *combine all scraped mongo dumps locally (still running unfortunately, will get to this EOD)*

2. *get rest endpoints to Ian.. eg json string to and from.*

3. *Combine all scraped mongo dumps locally*

4. *Spin up EC2, get 'hello world' running as response to JSON request.
  - Then hardcode 10 routes as JSON response to*
  - Test with insomnia

5. *Parse features into route_features.csv*
  - *Do a lot of cleaning*

6. *Create rus_master.csv*

7. Do Analysis:
  - Plot histogram and identify cold starts.
  - Look at sparsity.
  - Make some Hypotheses about SVD Parameters.

------- EOD Friday (or Sunday if necessary)-----------



7. fit model to rus_clean.csv
  - try on EC2 with Surprise
    - if this doesn't work, will need to cluster compute using PYSPARK
  - grid search params (if initial fit takes >2-3mins, use subset of rus_clean.csv)

8. Build recommender
  - Read route features in as DF
  - filter routes based on JSON string (return list of routeIDs)
  - use algo.test(list of userID(same), list of routeIDs)

9. Incorporate recommender into Flask app

10. Work on Documentation / Presentation

11. Do NLP analysis

12. Add 'Keywords functionality into App'
