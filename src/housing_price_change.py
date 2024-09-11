import pandas as pd
import os

# Load created CSV file that contains station name and distance 
combined_df = pd.read_csv("/Users/atwoo/Documents/Fairly_even/data/interim_data/combined_station_geocode.csv")

# Function to calculate lag and price change
def calculate_price_changes(group):
    """Calculate the price change  in meters between two latitude and longitude coordinate points.

    Parameters
    ----------
    group : dataframe 
        Dataframe where rows are grouped by Address name
        
    Returns
    -------
    dataframe
        returns dataframe where columns for price change after x years has been added
    """
    
    group = group.sort_values(by="Year")
        
    # Loop over all possible pairs of years in the group
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            year_diff = group.iloc[j]['Year'] - group.iloc[i]['Year']
            price_change = group.iloc[j]['Sale_Price'] - group.iloc[i]['Sale_Price']
            
            # Create a new column name based on the year difference
            col_name = f"Price_Change_{year_diff}_Years"
            group.loc[group.index[j], col_name] = price_change
    
    return group

# Apply the above function to each group of properties
df_result = combined_df.groupby("Address").apply(calculate_price_changes)
df_result = df_result.reset_index(drop=True)

# Re-order columns in ascending order  
price_idx = ["Price_Change_0_Years","Price_Change_1_Years","Price_Change_2_Years","Price_Change_3_Years","Price_Change_4_Years","Price_Change_5_Years","Price_Change_6_Years","Price_Change_7_Years","Price_Change_8_Years","Price_Change_9_Years","Price_Change_10_Years","Price_Change_11_Years","Price_Change_12_Years"]
reordered_cols = df_result[price_idx]
remaining_cols = df_result.drop(columns=price_idx)
df_result = pd.concat([remaining_cols, reordered_cols], axis=1)
df_result = df_result.drop(columns= ['Unnamed: 0', 'index'])

file_name = "final_df.csv"
save_path = os.path.join("/Users/atwoo/Documents/Fairly_even/data/processed_data",file_name)
df_result.to_csv(save_path)
print("CSV file created!")