# data-science-data-cleaning-flight-delays
Data cleaning and exploratory analysis project using pandas on airport flight data. The project demonstrates focusing on handling missing values, data type conversion, datetime processing, and analyzing how the day of the week impacts flight departure delays.

## Data Sources
We extracted the flight delay data using the anyflights package in R (https://github.com/simonpcouch/anyflights), which is similar to nycflights13 (https://github.com/tidyverse/nycflights13).

We selected ATL and the year 2023. This contains data on 336434 flights. We randomly took 5000 samples from this dataset. 


## US Daily Passengers
The passenger dataset comes from the Transportation Security Administration (TSA), which counts the number of people that go through TSA checkpoints each day.

https://www.tsa.gov/travel/passenger-volumes/2023
