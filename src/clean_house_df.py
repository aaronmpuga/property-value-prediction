import pandas as pd
import os

# Path to "housing_sales_data" file 
folder_directory = "/Users/atwoo/Documents/Fairly_even/data/interim_data"

housing_filename = "housing_sales_data.csv"
housing_data_path = os.path.join(folder_directory, housing_filename)

housing_data = pd.read_csv(housing_data_path, low_memory=False)
housing_data = housing_data.drop(housing_data.columns[21:], axis=1)
housing_data = housing_data.drop(axis = 0, index= [0,1,2])
new_column_names =["Borough","Neighborhood","Building_Class_Category","Tax_Class","Tax_Block","Tax_Lot","Easement", "Building_Classification_Code_At_Present","Address",
                    "Apartment_Number", "Zip_Code", "Residential_Units", "Commercial_Units", "Total_Units", "Land_Square_Feet", "Gross_Square_Feet", "Year_Built", 
                    "Tax_Class_At_Time_Of_Sale", "Building_Classification_Code_At_Time_Of_Sale", "Sale_Price", "Sale_Date"]

housing_data.columns = new_column_names
housing_data = housing_data.drop(axis=0, index=[3])
housing_data = housing_data.reset_index(drop= True)

# Re-order columns of dataframe
columns_kept = ["Borough", "Neighborhood", "Building_Class_Category", 
    "Building_Classification_Code_At_Time_Of_Sale", "Address", "Zip_Code", "Sale_Price", "Sale_Date"]
housing_data = housing_data[columns_kept]

# Used the "zip_borough.csv" CSV file to map each property to a borough, given the zip codes of each property in dataframe
zip_dir = "/Users/atwoo/Documents/Fairly_even/data/raw_data"

zip_borough_map_path = os.path.join(zip_dir, "zip_borough.csv")
zip_to_borough = pd.read_csv(zip_borough_map_path)

# Aligning column names and dtype of column cell data before merging
zip_to_borough.columns = ["Zip_Code", "Borough"]
housing_data["Zip_Code"] = pd.to_numeric(housing_data["Zip_Code"], errors = "coerce")
housing_data = housing_data.dropna(subset=["Zip_Code"])
housing_data["Zip_Code"] = housing_data["Zip_Code"].astype("int64")
housing_data = housing_data.merge(zip_to_borough, on="Zip_Code", how="left")

# Removing unmapped zipcode rows and re-ordering columns of dataframe
housing_data = housing_data.dropna(subset= ["Borough_y"])
housing_data = housing_data.drop(columns = ["Borough_x"])
housing_data = housing_data.rename(columns = {"Borough_y": "Borough"})
housing_data = housing_data[columns_kept]

# Removing rows where the sale price is zero (Indication of transfer of ownership involving no money according to glossary)
housing_data["Sale_Price"] = housing_data["Sale_Price"].astype("int64")
housing_data = housing_data[housing_data["Sale_Price"] != 0]
housing_data = housing_data.reset_index(drop= True)

# Formating date and time values
housing_data["Sale_Date"] = pd.to_datetime(housing_data["Sale_Date"])
housing_data["Year"] = housing_data["Sale_Date"].dt.year
housing_data = housing_data.sort_values(by= ["Address","Year"])

# Saving cleaned "housing_sales_data" dataframe as CSV file "cleaned_file_name"
cleaned_file_name = "Cleaned_NYC_Property_Sales_Data_2003_To_2015.csv"
cleaned_filepath = os.path.join(folder_directory, cleaned_file_name)

housing_data.to_csv(cleaned_filepath, index=False)