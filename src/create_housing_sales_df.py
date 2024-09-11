import pandas as pd
import os 

rolling_sales_directory = "/Users/atwoo/Documents/Fairly_even/data/raw_data/Annualized_Rolling_Sales_Update"

file_df_list = []

for file in os.listdir(rolling_sales_directory):
    if file.endswith('.xls') or file.endswith('.xlsx'):
        file_path = os.path.join(rolling_sales_directory, file)
        df = pd.read_excel(file_path)
        file_df_list.append(df)

housing_sales_df = pd.concat(file_df_list, ignore_index=True)
housing_sales_df.to_csv('housing_sales_data.csv', index=False)

print("Combined rolling sales CSV created!")