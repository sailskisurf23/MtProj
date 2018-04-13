# [Mountain Project](www.MountainProject.com) Recommenders

### Background

Mountain project is a climbing website with an extensive [route database](https://www.mountainproject.com/route-guide), active discussion [forum](https://www.mountainproject.com/forum), and ~20k active users. Users of the website can browse for climbing routes, **tick** the routes that they have done and **rate** them on a 4-star scale. Additionally users upload photos and share useful information about their experience on each route in the comments section.

Mountain Project currently has [partner search](https://www.mountainproject.com/partner-finder) and route search. This functionality allows users to search for appropriate routes and partners based on ability / route difficulty as well as location.

### Objective

I want to make it easier for users to find routes that they will be interested and partners who will be a good fit. My goal is to build a partner and route recommenders based on route and user data harvested from the Mountain Project website.

For the **Route Recommender**, my idea is to construct a matrix of all routes and users. The values could either be *explicit* (the star rating given to a route by that user), or *implicit* (whether or not a user has **ticked** a route or whether or not it is on their **To-Do list**). We then use a matrix decomposition method to fill the missing values in the matrix and thereby predict how each user would rate each climb. For implementation, if a user were looking for routes in a particular area - we could return the 5-10 routes that would appeal to them most *in that area*.

For the **Partner Recommender**, the goal is to suggest partners that have similar objectives and a similar level of experience. For objectives, we can evaluate how many **To-Do's** each user has in common with another. Similarly, for experience we can look at each users **Ticks**.

One possible avenue of further exploration would be to incorporate users' **comments** on each route using NLP in order to add insight as to the character of each route (and each user).

### Presentation

I will document the process of collecting, cleaning and exploring the data with a Powerpoint Presentation. This presentation will also cover the methodology used in my modeling process and will report the success metrics I use to

The logical goal for a recommender project is to create an application for a user to get recommendations. The idea is to dynamically pipe to users route suggestions based on who they are and where they are looking. This would be build into a flask app. Ideally, I would like to pair with a Web-dev student and build beautiful and clean front end.

### The Dataset

Mountain Project offers a basic API which delivers some useful information about routes and users in JSON format. Making calls to the API is relatively straightforward, and I can save the data to a database

I would like to gather more detailed information about how each user has rated and commented on each route. To do this I will need to scrape and parse raw HTML pages from the Mountain Project website.

### Potential Roadblocks

 - The scraping process will be difficult
   - There are a huge number of pages to scrape, and I'm not sure how to get the page id for all routes on the website
   - I will need to make a large number of HTTP Get requests from the website without getting blocked
 - Parsing the data won't be easy either.
   - the most valuable data is going to come back as a huge messy pile of HTML which will need to be carefully catalogued in a Mongo DB and processed in order to extract any insights and build a useful recommender.
 - Measuring the effectiveness of this recommender isn't really possible.
   - RMSE won't tell me how 'appropriate' the routes I am predicting are for a given user. Some routes are Objectively very good, and rated highly by nearly all that climb them. But they might be far too hard and potentially dangerous for a climber of insufficient skill
