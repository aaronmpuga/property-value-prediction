import pandas as pd
import os 

path_to_sales_files = "/Users/atwoo/Documents/Fairly_even/Annualized_Rolling_Sales_Update"

file_df_list = []

for file in os.listdir(path_to_sales_files):
    if file.endswith('.xls') or file.endswith('.xlsx'):
        file_path = os.path.join(path_to_sales_files, file)
        df = pd.read_excel(file_path)
        file_df_list.append(df)

housing_sales_df = pd.concat(file_df_list, ignore_index=True)
housing_sales_df.to_csv('housing_sales_data.csv', index=False)

print("CSV created!")
