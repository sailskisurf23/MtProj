# CAPSTONE IDEAS

### [Mountain Project](www.mountainproject.com) EDA and Recommenders
  - *Partner Recommender*
  - *Route Recommender*

#### Summary
- Analyze MtProj data and create recommenders


#### Objective
- Identify 'clusters' of climbers within Mt Project community. clusters would have similar climbing level, interests etc
- Characterize and classify routes based on difficulty, style and NLP on comments about each route
- Create app to identify appropriate partners based on common 'interests' (IE  *To Do's*) and common 'experience' (IE *Ticks*)
- Recommend routes based on using personalized information about each climber


##### Presentation
- Show results of EDA using some visualization software. In Jupyter NB or PPT?
- Create flask app with widgets



### [Smarter Sorting](http://smartersorting.com/#top) Classification Model
##### Summary
- Develop a model to **predict** waste category previously uncategorized products
##### Objective
- Smarter Sorting sells scanners to municipalities which quickly *identify and categorize* household products into *waste categories*. This allows municipalities to sell these waste products to recyclers for *re-use* instead paying for shipping and incineration.
- Smarter Sorting has harvested data on thousands of household products based on what the product manufacturer has published. Based on category expertise and the data available to them, they have manually labeled some portion of the products that they have gathered data on but there are thousands more which are currently unlablled.
- I want to develop an algorithm that will correctly predict which *waste category* a product belongs to based on the data that Smarter Sorting has about these products

##### Presentation
- Will report the accuracy and methodology used to create the model in a PowerPoint or Keynote presentation

##### Next steps
- Follow up with Smarter Sorting to better understand their needs and what data / predictors  they have available

### Analyzing Cycling Infrastructure

##### Summary
- Use [Strava](www.strava.com) cycling data in conjuction with other data sources to identify corridors to improve / invest in cycling infrastructure in the city of Austin (or somewhere else if more interesting)

##### Objective
- Cycling is the best way to get around: it's fun, it's healthy, it's cheap, it's good for the environment.
- There are a few barriers that prevent many individuals from use a bike to get to work:
    - Cycling can be **dangereous**: 726 deaths nationally in 2012, ~49,000 inured [*](https://www.herrmanandherrman.com/bicycle-accidents-lawyers/texas-bicycle-accident-statistics/)
    - Rough roads and poor infrasrtuture can **slow down** cyclists as well as add uneccesary wear and tear on both the equipment and the cyclist
- Using strava data, I can identify high-traffic corridors for cyclists. See strava's [HEATMAP](https://www.strava.com/heatmap#12.63/-97.72913/30.25549/hot/all)
- I also think I can infer from the user data, the average speed of cyclists at any given location.
- Using city data I can also grab the location of cycling **incidents**. Fatalities/ injuries etc.


##### Presentation
- I think I can do some *awesome* dataviz for this in a Jupyter Notebook.

### Analyzing Lyft Data

##### Summary
- Identify routes / strategies for [Lyft](https://www.lyft.com/), [Uber](www.uber.com) or [Ride Austin](https://www.rideaustin.com/) drivers to make the most $$ / hr

##### Objective
- Lyft drivers operate a small business with super tight margins. My goal is to identify routes / strategies which allow them to make the most money without getting stuck in traffic or wandering areas of the city where there are no riders.
- I'm not familiar with the data I can get from Lyft's API yet so I'm not sure exactly how I'll tackle the problem, but I think I should be able to get some ride data on a *per driver* basis which should allow me to gather data to infer the objective

##### Presentation
- Jupyter Notebook with cool dataviz
