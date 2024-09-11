import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

folder_directory = "/Users/atwoo/Documents/Fairly_even/data/processed_data"
file_name = "final_df.csv"
data_path = os.path.join(folder_directory, file_name)

df_result = pd.read_csv(data_path)

popular_codes = ['A1', 'A5', 'A2']  

boroughs = ["Staten", "Queens", "Bronx", "Brooklyn"]

# This removes all values in price change x years columns that are less than 0 
for i in range(13):
    n_col = f'Price_Change_{i}_Years'
    df_result[n_col] = df_result[n_col].apply(lambda x: 0 if x < 0 else x) 


# Iterate over each borough, building classification code, and years_ahead lag feature
for borough in boroughs:
    for building_code in popular_codes:
        for i in range(6):
            feature_col = f'Price_Change_{i}_Years'
            
            # Drop rows where price change column i year's value is NaN indicating that the dropped row didn't 
            # have a price change value for the desired i years ahead 
        
            df_nonan = df_result.dropna(subset=[feature_col])
            df_filtered = df_nonan[ (df_nonan['Building_Classification_Code_At_Time_Of_Sale'] == building_code) & 
                                        (df_nonan['Borough'] == borough)]

            # Define X (features) and y (target)
            numerical_features = df_filtered[['Sale_Price', 'Station_Distance']]

            features = numerical_features
            # Target variable is the values in price change i years column
            target = df_filtered[feature_col]  

            features = features.dropna()
            target = target.loc[features.index]

            # Train-test split
            X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=23)

            # Initialize and train the model
            model = RandomForestRegressor(n_estimators=100, random_state=23)
            model.fit(X_train, y_train)

            # Save the model on local device
            model_filename = f'model_{borough}_{building_code}_years_ahead_{i}.pkl'
            model_dir = "/Users/atwoo/Documents/Fairly_even/models"
            model_filepath = os.path.join(model_dir, model_filename)
            joblib.dump(model, model_filepath)

            print(f"Model for {borough}, {building_code} {i} years ahead was saved.")
