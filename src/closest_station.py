#Functions to calculate closest train station to each property 

import numpy as np 
from geopy.distance import geodesic
import pandas as pd
import os

geo_codeA = pd.read_csv("/Users/atwoo/Documents/Fairly_even/data/interim_data/geocoded_housing_data_codeA_final.csv")

geo_codeA.dropna(axis= 0, subset= ["Latitude", "Longitude"], inplace= True)
geo_codeA = geo_codeA.reset_index()
station_data = pd.read_csv("/Users/atwoo/Documents/Fairly_even/data/processed_data/clean_station_data.csv")

def calculate_distance (latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    """Calculate the distance in meters between two latitude and longitude coordinate points.

    Parameters
    ----------
    latitude_1 : float
        latitude value of first coordinate point
    longitude_1 : float
        longitude value of first coordinate point
    latitude_2 : float
        latitude value of second coordinate point
    longitude_2 : float
        longitude value of second coordinate point
        
    Returns
    -------
    float
        distance between coordinate points 
    """

    return geodesic((latitude_1, longitude_1), (latitude_2, longitude_2)).meters

def get_nearest_station (property_latitude: float, property_longitude: float, station_df) -> tuple:
    """Find the nearest train station name and its distance to the inputted property's latitude and longitude coordinate points

    Parameters
    ----------
    property_latitude : float
        latitude value of the property 
    property_longitude : float
        longitude value of the property        
    station_df : csv file 
        Csv file containing the station data for all train stations in new york. Each row must have a two columns correpsonding to a stations latitude and longitude, 
        titled Station_Latitude and Station_Longitude respectively.

    Returns
    -------
    tuple
        returns tuple of station name followed by distance of station to property

    """
    distances = station_df.apply(lambda row: calculate_distance(property_latitude, property_longitude, row["Station_Latitude"], row["Station_Longitude"]), axis=1)
    dist_idx = distances.idxmin()
    nearest_station = station_df.loc[dist_idx, "Stop Name"]
    nearest_station_dist = distances.min()

    return nearest_station, nearest_station_dist

# Execute method on dataframe
geo_codeA[["Nearest_Station", "Station_Distance"]] = geo_codeA.apply(lambda row: pd.Series(get_nearest_station(row["Latitude"], row["Longitude"], station_data)), axis=1)
geo_codeA = geo_codeA.drop(columns=["index"])

file_name = "combined_station_geocode.csv"
save_path = os.path.join("/Users/atwoo/Documents/Fairly_even/data/interim_data",file_name)
geo_codeA.to_csv(save_path)
print("CSV file created!")