import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

folder_directory = "/Users/atwoo/Documents/Fairly_even/data"
file_name = "final_df.csv"
data_path = os.path.join(folder_directory, file_name)

df_result = pd.read_csv(data_path)

popular_codes = df_result['Building_Classification_Code_At_Time_Of_Sale'].value_counts()[2:4]
dist_dict = {"647.0 - 1445.0" : "dist2", "2863.0 - 8763.0" : "dist4", "9.0 - 647.0" : "dist1", "1445.0 - 2863.0" : "dist3"}

# Iterate over each unique building code
for code in popular_codes.index:
    df_code = df_result[df_result['Building_Classification_Code_At_Time_Of_Sale'] == code]
    
    # Iterate over each unique station distance group
    for distance_group in df_code['Station_Distance_Group'].unique():
        df_distance = df_code[df_code['Station_Distance_Group'] == distance_group]
        
        # Iterate over each years_ahead lag feature
        for i in range(13):
            feature_col = f'Price_Change_{i}_Years'
            
            # Filter rows where this feature is not NaN
            df_code_nonan = df_distance.dropna(subset=[feature_col])

            # Define X and y
            features = df_code_nonan.drop(columns=[feature_col] + [f'Price_Change_{j}_Years' for j in range(13)])
            target = df_code_nonan[feature_col]
            
            # Convert categorical variables to dummy/indicator variables
            features = pd.get_dummies(features, drop_first=True)
            features = features.dropna()
            target = target.loc[features.index]

            # Train-test split
            X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=23)
            
            # Initialize and train the model
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            
            # Save the model
            model_filename = f'model_{code}_{dist_dict[distance_group]}_years_ahead_{i}.pkl'
            joblib.dump(model, model_filename)
            
            print(f"Model for {code}, {dist_dict[distance_group]} for years {i} was saved")
