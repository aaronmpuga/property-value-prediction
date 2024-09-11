import time
import pandas as pd
from geopy.geocoders import Nominatim
import os 

# Path to save backup CSV file every 1800 addresses
save_directory = "/Users/atwoo/Documents/Fairly_even/data/interim_data"

backup_csv_path = os.path.join(save_directory, "geocoded_addresses_codeA_backup.csv")
final_csv_path = os.path.join(save_directory, "geocoded_housing_data_codeA_final.csv")
df_path = os.path.join(save_directory, "housing_data_codeA.csv")

housing_data_codeA = pd.read_csv(df_path)

geo = Nominatim(user_agent="my_housing_project_app")

# Address cache
address_dict = {}

def getMeridian(street: str, postalcode: int, city: str, index: int) -> tuple:
    """
    Determines the longitidue and latitude values for a given address
    Parameters
    ----------
    street : str
        Street address for the location of the desired latitude and longitude values.
    postalcode : int
        Postalcode or zipcode  for the location of the desired latitude and longitude values. 
    city : str
        City name for the location of the desired latitude and longitude values. 

    Returns
    -------
    tuple
        latitude and longitude pairing.

    """
    # Construct the structured query dictionary (defined by geopy)
    query = {
        'street': street,
        'postalcode': postalcode,
        'city' : city,
        'state' : "NY"
    }

    # Convert query dictionary to a string to use as a key for the cache
    query_key = str(query)
    
    # Check if the query has been seen before
    if query_key in address_dict:
        return address_dict[query_key]
    else:
        try:
            location = geo.geocode(query)
            if location:
                address_dict[query_key] = (location.latitude, location.longitude)
            else:
                address_dict[query_key] = (None, None)
                
        except Exception as e:
            print(f"Couldn't find latitude and longitude for {query_key}: {e}")
            address_dict[query_key] = (None, None)
                
    if index % 1800 == 0:
        print(f"Processed {index} addresses so far!")
        # Save progress to a backup CSV file every 1800 addresses (approximately every 30 minutes)
        pd.DataFrame.from_dict(address_dict, orient="index", columns=["Latitude", "Longitude"]).to_csv(backup_csv_path)
        
    # Rate limiting: pause between requests to avoid hitting the rate limit
    time.sleep(1)  
    
    return address_dict[query_key]

# Execute method 
housing_data_codeA["Latitude"], housing_data_codeA["Longitude"] = zip(*housing_data_codeA.apply(
    lambda row: getMeridian(row["Address"], row["Zip_Code"], row["Borough"], row.name), axis=1))

housing_data_codeA.to_csv(final_csv_path, index=False)
print(f"Completed! The final data has been saved to data folder")
