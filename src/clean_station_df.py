import pandas as pd
import os

folder_directory = "/Users/atwoo/Documents/Fairly_even/data/raw_data"

station_data_filename = "MTA_Subway_Stations.csv"
station_data_path = os.path.join(folder_directory, station_data_filename)

station_data = pd.read_csv(station_data_path)
columns = ["Borough","Stop Name","GTFS Latitude", "GTFS Longitude", "Georeference"]
station_data = station_data[columns]

# Change borough names
borough_map = {"M": "Manhattan", "Bk" : "Brooklyn", "Bx" : "Bronx", "Q" : "Queens", "SI" : "Staten Island"}

for row_idx, elem in enumerate(station_data["Borough"]):
    if elem in borough_map:
        station_data["Borough"][row_idx] = borough_map[elem]
        
# Change Latitude and Longitude index names
station_data.rename(columns= {"GTFS Latitude" : "Station_Latitude", "GTFS Longitude" : "Station_Longitude"}, inplace= True)

# Save Cleaned station Data as CSV
clean_station_data_filename = "clean_station_data.csv"
clean_path = os.path.join(folder_directory, clean_station_data_filename)
station_data.to_csv(clean_path, index= False)