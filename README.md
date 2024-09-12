# New York City Property Property Value Prediction Using Housing Sales Data

This project aims to predict NYC property values based on there distance to train stations and historical housing sales data from 2003-2015. Using a dataset of over 900,000 records, the project focuses on single-family dwellings (Building Code A) and applies machine learning models to estimate future property values. This work leverages regression models and geographic data to build accurate predictions.


## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data](#data)
5. [Model and Approach](#model-and-approach)
6. [Results](#results)
7. [Future Work](#future-work)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)

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
2. Set-up Virtual environment and install dependencies
   ```bash
   git clone https://github.com/aaronmpuga/property-value-prediction.git
   cd property-value-prediction
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt

3. Set up the Nominatim API for location data (if applicable):
- Use the free Nominatim API to get geographic coordinates for each property.
- Note: Nominatim API only process one request per second so if you plan on finding longitude and latitude values for a large amount of properties I would suggest the use of a paid geographic API to process data faster.

## Usage
To test the prediction models follow the steps below 
1. Download the random forest regression [models folder](./models) to your local device
2. Download the [predict.py](./src/predict.py) function
3. In your IDE open the predict.py function and add this code at the end of the function
   ```python
   curr_price = 300000  # Current property value input by the user
   years = 5 # How many years ahead the user wants to predict
   b_code = "A1"     # Building classification code of user's property
   borough = "Queens"      # The borough the property is in
   station_dist = 500   # Distance of the property from the station in meters

   predicted_value = predict_property_value(curr_price, years, b_code, borough, station_dist)
   print(f"The predicted property value in {years_ahead} years is: {predicted_value}")
- curr_price, years, b_code, borough and station_dist are example inputs for the function to take in. Change these values to what you would like to predict. 






# Files
The data used in this project was taken from [Kaggle](https://www.kaggle.com/datasets/dgawlik/nyse/data?select=prices.csv)

The stock data within these csv files ranges from the years 2010 to 2016 (varies by company)

- `fundamentals.csv`: Contains fundamental financial data of companies.
- `prices.csv`: Contains daily stock prices of companies.
- `prices-split-adjusted.csv`: Contains split-adjusted stock prices.
- `securities.csv`: Contains additional company information.
