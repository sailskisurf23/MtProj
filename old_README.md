# [Mountain Project](www.MountainProject.com) Recommender

### Background

Mountain project is a climbing website with an extensive [route database](https://www.mountainproject.com/route-guide), active discussion [forum](https://www.mountainproject.com/forum), and ~20k active users. Users can browse for climbing routes, **tick** the routes that they have climbed and **rate** them on a 4-star scale. Additionally, users can upload photos and share useful information about their experience on each route in the comments section.

### Research
The approaches to be employed in this project have been implemented and documented by others:

[Recommender tutorial](https://towardsdatascience.com/how-did-we-build-book-recommender-systems-in-an-hour-the-fundamentals-dfee054f978e)

[NLP project on data scraped from forum](https://nycdatascience.com/blog/student-works/topic-modeling-user-clustering-internet-discussion-forums-case-study/)


### Objective

My goal is to make it easier for users to find routes that they will be interested in. To do this I built a route recommender based on route and user data harvested from the Mountain Project website.

For the **Route Recommender**, my idea is to construct a matrix of all routes and users. The values could either be *explicit* (the star rating given to a route by that user), or *implicit* (whether or not a user has **ticked** a route or whether or not it is on their **To-Do list**). I will use a matrix decomposition method to fill the missing values in the matrix and thereby predict how each user would rate each climb. For implementation, if a user were looking for routes in a particular area - the recommender could return the 5-10 routes that would appeal to them most *in that area*.

One possible avenue of further exploration would be to incorporate users' **comments** on each route using NLP in order to add insight as to the character of each route (and each user).

### Presentation

I will document the process of collecting, cleaning and exploring the data and compile the it in a Powerpoint Presentation. This presentation will also cover the methodology used in my modeling process and will report the success metrics I use to evaluate the model.

The logical goal for a recommender project is to create an application for a user to get recommendations. The idea is to dynamically pipe to users route suggestions based on who they are and where they are looking. This would be build into a flask app. Ideally, I would like to pair with a Web-dev student and build beautiful and clean front end.

### The Dataset

Mountain Project offers a basic API which delivers some useful information about routes and users in JSON format. Making calls to the API is relatively straightforward and I can save the data to a database.

I would like to gather more detailed information about how each user has rated and commented on each route. To do this I will need to scrape and parse raw HTML pages from the Mountain Project website.

### Potential Roadblocks

 - The scraping process will be difficult.
   - There are a huge number of pages to scrape and I'm not sure how to get the page ids for all routes on the website
   - I will need to make a large number of HTTP Get requests from the website without getting blocked.
 - Parsing the data won't be easy either.
   - the most valuable data is going will be returned as a huge messy pile of HTML which will need to be carefully catalogued in a Mongo DB and processed in order to extract any insights and build a useful recommender.
 - Quantitatively measuring the effectiveness of this recommender won't necessarily give results that are in line with intuition.
   - RMSE won't tell me how 'appropriate' the routes I am predicting are for a given user. Some routes are Objectively very good, and rated highly by nearly all that climb them. But they might be far too hard and potentially dangerous for a climber of insufficient skill.
   - could tune the recommender based on intuition and feedback from other climbers / friends.
