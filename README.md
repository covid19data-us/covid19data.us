# covid19data.us

all things related to simplification, aggregation, viewing, charting, managing covid19 data

covid19data.us
software and data aggregation for the public - examples, use_cases, etc.

Goal of project: Make the time series data extremely easy for others to use, pull, chart, etc.

History: on January 23, 2020 - I started a world news aggregation site, after members of my remote teams in JPMC (APAC) began discussing the topic of a new coronavirus. Since I am proudly an x-Googler, I had a few data questions from some folks which was verified. My x-Military contacts also confirmed movement on the topic. That resulted in - organizing news so I could stay up to speed - traffic picked up and I needed some content checkers because the search is challenged and news agencies are less than accurate. -- I currently have 3 people in PH checking/categorizing/posting content

Here: https://covid19data.com

in March the US became a topic and I needed a more US centric site. I got some inspiration from a few medical specific sites and someone coined the phrase: Ninja Virus -- so...

Here: https://ninjavirus.com. -- US Centric

These are Wordpress sites hosted on Google - with RSS crawlers, Twitter Crawler, URL Crawler, etc. -- uggh@CMS@wordpress -- but I needed something click:fast [not my day job].

Now we are here today: -- a few have contributed and probably this should merge into covidtracker project. Over the weekend i opened up another GCP project and decided with the help of a couple of others to pull JHU data into Prometheus and expose the endpoint and do a little Grafana work. -- Add the datasource in Grafana (whosoever will).

Anyway...

--- Contribute if you believe ---

"We should not hold data hostage"

"Keep it simple: Minimalist thinking"

"A language is a choice, whatever gets it done i.e. Polyglot" - we all have our favorites

LINKS:

-- api.covid19data.us --> prometheus [TSDB] with JHU covid data [nightly pulls]

-- graphs.covid19data.us --> grafana dashboards [share, embed, copy:paste, etc.]

-- dev.covid19data.us --> [needs contributions]

-- news.covid19data.us --> transitioning https://ninjavirus.com [US centric WP site]

-- www -- defaults to grafana for now [needs contributions]

![](images/smaller_gcp_setup.png)

Credit to Johns Hopkins for giving us the data! Credit to the covidtracker folks - keeping an eye on the work there
