import joblib
import pandas as pd
import os

def predict_property_value(current_property_value, years_ahead, building_code, borough, station_distance):
    """Predict the increase in property value

    Parameters
    ----------
    current_property_value : float
        Current value of property being passed in  
    year_ahead : int
        The number of years ahead that user wants to predict the value of their property will be         
    building_code : string
        The building classification code of the property to be predicted
    borough : string 
        The borough of where the property is located 

    Returns
    -------
    float
        returns the predicted property value 
    """
    codes = ["A1", "A2", "A5"]
    borough_lst = ["Staten", "Queens", "Bronx", "Brooklyn"]

    # Validate passed in parameters 
    assert (years_ahead > 0 and years_ahead <= 5, "Years value must be between 0 and 5!")
    assert (building_code not in codes, "Building code must be either A1, A2 or A5!")
    assert (borough not in borough_lst, "Incorrect borough name\nEnsure first letter of borough is capitalized\nManhattan is not supported")
    assert (station_distance > 9 and station_distance < 8763, "Station distance must be between 9 and 8763 meters")


    # Load the corresponding model based on borough, building code, and years ahead
    model_filename = f'model_{borough}_{building_code}_years_ahead_{years_ahead}.pkl'
    model_path = os.path.join("/Users/atwoo/Documents/Fairly_even/models", model_filename)
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"The model for {borough}, {building_code}, {years_ahead} years ahead does not exist.")
    
    model = joblib.load(model_path)
    
    # Prepare the input data
    input_data = pd.DataFrame({
        'Sale_Price': [current_property_value],
        'Station_Distance': [station_distance],
    })
    
    # Make the prediction using the loaded model
    predicted_price_change = model.predict(input_data)[0]
    
    # Calculate the predicted future property value
    future_property_value = current_property_value + predicted_price_change
    
    return future_property_value