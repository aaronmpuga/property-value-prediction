# New York City Property Property Value Prediction Using Housing Sales Data

This project aims to predict NYC property values based on their distance to train stations and historical housing sales data from 2003-2015. Using a dataset of over 900,000 records, the project focuses on single-family dwellings (Building Code A) and applies machine learning models to estimate future property values. This work leverages regression models and geographic data to build accurate predictions.


## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data](#data)
6. [Future Work](#futurework)



## Features
- Data cleaning and preprocessing pipeline for housing sales data.
- Integration of geographic data using the Nominatim API to retrieve location details.
- Machine learning models for property value prediction (Linear Regression, Random Forest).
- Feature engineering with building code, price change, and other key attributes.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/aaronmpuga/property-value-prediction.git
   cd property-value-prediction
2. Set up Virtual environment and install dependencies
   ```bash
   git clone https://github.com/aaronmpuga/property-value-prediction.git
   cd property-value-prediction
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt

3. Set up the Nominatim API for location data (if applicable):
- Use the free Nominatim API to get geographic coordinates for each property.
- Note: Nominatim API only processes one request per second so if you plan on finding longitude and latitude values for a large amount of properties I would suggest the use of a paid geographic API to process data faster.

## Usage
To test the prediction models follow the steps below: 
1. Download the random forest regression [models folder](./models) to your local device
2. Download the [predict.py](./src/predict.py) python script to your local device
3. In your IDE open the predict.py function and add this code at the end of the function
   ```python
   curr_price = 300000  # Current property value input by the user
   years = 5 # How many years ahead the user wants to predict
   b_code = "A1"     # Building classification code of user's property
   borough = "Queens"      # The borough the property is in
   station_dist = 500   # Distance of the property from the station in meters

   predicted_value = predict_property_value(curr_price, years, b_code, borough, station_dist)
   print(f"The predicted property value in {years_ahead} years is: {predicted_value}")
- curr_price, years, b_code, borough and station_dist are example inputs for the function to take in. Change these values to what you would like to predict

## Data 
- The [raw_data](./data/raw_data) folder is reserved for files and data that were sourced online at the start of the project from sites such as Kaggle and dataNy.gov
   - The Annulized_Rolling_Sale_Update folder taken from [NYC Open Data](https://data.cityofnewyork.us/Housing-Development/NYC-Calendar-Sales-Archive-/uzf5-f8n2/about_data) has all the Excel files containing all the property sales data across all boroughs in NYC from 2003 - 2015 that was used in this project
   - 
   -  The [zip_borough.csv](./data/raw_data/zip_borough.csv) file taken from [Kaggle](https://www.kaggle.com/datasets/kimjinyoung/nyc-borough-zip) was used to create the borough column in the housing sales dataframe by mapping each property zipcode to its corresponding borough name
   -  The [MTA_Subway_Stations.csv](./data/raw_data/MTA_Subwa_Stations.csv) file taken from [data.gov](https://catalog.data.gov/dataset/mta-subway-stations) held the train station data used throughout the project
- The [interim_data](./data/interim_data) folder contains modified/cleaned datasets that have been created based on the inital data in the raw_data folder or from other csv files in the folder. 
- The [processed_data](./data/processed_data) folder contains the final csv file datasets that contain all the data necessary for their respective purposes

## Future Work 
- Expand the model to include additional building codes (e.g., Code B and D).
- Implement more sophisticated geographic feature extraction using APIs with better limits.
- Explore deep learning models for improved predictions
- Develop a web-based application for real-time property value prediction.
