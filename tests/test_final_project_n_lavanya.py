from final_project_n_lavanya import __version__
from final_project_n_lavanya import final_project_n_lavanya

import requests
import json
import os
import pandas as pd
import datetime
import pytest

# Remember to save API key as an environment variable before running the tests.

api_key = os.getenv('ltadatamall_api_key')

def test_version():
    assert __version__ == '0.1.0'
    
# These tests check whether appropriate assertions are raised to ensure that inputs are entered as strings.

with pytest.raises(AssertionError):
    get_bus_arrivals(123456, '83139') # need 2 more
    get_bus_arrivals(api_key, 83139)
    get_bus_arrivals(api_key, '83139', 15)
    get_bus_services(123456)
    get_bus_routes(123456)
    get_bus_stops(123456)
    get_bus_pass_vol_bus(123456)
    get_bus_pass_vol_bus(api_key, 202012)
    get_bus_pass_vol_odbus(123456)
    get_bus_pass_vol_odbus(api_key, 202012)
    get_bus_pass_vol_odtrain(123456)
    get_bus_pass_vol_odtrain(api_key, 202012)
    get_bus_pass_vol_train(123456)
    get_bus_pass_vol_train(api_key, 202012)
    get_taxi_availability(123456)
    get_taxi_stands(123456)
    get_train_service_alerts(123456)
    get_carpark_availability(123456)
    get_erp_rates(123456)
    get_est_travel_times(123456)
    get_faulty_traffic_lights(123456)
    get_road_openings(123456)
    get_road_works(123456)
    get_traffic_images(123456)
    get_traffic_incidents(123456)
    get_traffic_speed_bands(123456)
    get_variable_messages(123456)
    get_bicycle_parking(123456, '1.36666', '103.7666')
    get_bicycle_parking(api_key, 1.36666, '103.7666')
    get_bicycle_parking(api_key, '1.36666', 103.7666)
    get_bicycle_parking(api_key, '1.36666', '103.7666', 2.0)
    get_geospatial(123456, 'RoadHump')
    get_geospatial(api_key, RoadHump)
    get_facilities_maintenance(123456, 'NS1')
    get_facilities_maintenance(api_key, NS1)
    
## These tests check whether appropriate assertions are raised to ensure that API key entered as a string is valid.
    
with pytest.raises(AssertionError):
    get_bus_arrivals('123456', '83139')
    get_bus_services('123456')
    get_bus_routes('123456')
    get_bus_stops('123456')
    get_bus_pass_vol_bus('123456')
    get_bus_pass_vol_odbus('123456')
    get_bus_pass_vol_odtrain('123456')
    get_bus_pass_vol_train('123456')
    get_taxi_availability('123456')
    get_taxi_stands('123456')
    get_train_service_alerts('123456')
    get_carpark_availability('123456')
    get_erp_rates('123456')
    get_est_travel_times('123456')
    get_faulty_traffic_lights('123456')
    get_road_openings('123456')
    get_road_works('123456')
    get_traffic_images('123456')
    get_traffic_incidents('123456')
    get_traffic_speed_bands('123456')
    get_variable_messages('123456')
    get_bicycle_parking('123456', '1.36666', '103.7666')
    get_geospatial('123456', 'RoadHump')
    get_facilities_maintenance('123456', 'NS1')