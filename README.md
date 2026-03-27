# flight-delay-predictor-dashboard
Machine learning dashboard that predicts flight delays using historical flight and weather data.
- 
What I have done so far in my flight delay project:

1. Collected and combined the flight data
I downloaded multiple flight data files and combined them into one dataset called combined_flights.csv so all of the data would be in one place.

2. Started cleaning the dataset
I began preparing the data so it would be easier to use for prediction. This included working with the combined dataset instead of the separate raw files.

3. Defined the target variable
I created the target column for the project, called is_delayed.

4. Labeled flights as delayed or not delayed
I set:
- is_delayed = 1 if ARR_DELAY > 15 minutes
- is_delayed = 0 otherwise

5. Removed flights that do not fit the MVP
To keep the first version of the project simpler and cleaner, I removed:
- canceled flights
- diverted flights
- rows with missing arrival delay values

6. Checked that the new target column worked
I printed sample rows and checked the value counts for is_delayed to make sure the labeling was correct.

7. Saved the cleaned dataset
I saved the updated file as flights_with_target.csv, which is now ready for the next step of the project.

Current result:
After cleaning and labeling the data, the output showed:
- 902 flights labeled not delayed
- 97 flights labeled delayed

So far, I have turned the raw flight data into a cleaned dataset with a clear prediction target that I can use for the next stages of the project.
