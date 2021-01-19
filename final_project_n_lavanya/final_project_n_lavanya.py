import requests
import json
import os
import pandas as pd
import datetime

def get_bus_arrivals(api_key, bus_stop_code, service_no = ''):
    """
    Returns a Pandas DataFrame containing detailed service information (first stop, last stop, peak / offpeak frequency of dispatch) for all buses in operation at the time of request.
    
    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    bus_stop_code: str
        Character input; this is the bus stop reference code for the bus stop you are requesting data for.
    
    service_no: str
        Character input; this is the bus service number(s) you are requesting data for.
        By default, this is set to an empty string to provide data for all bus services at the requested bus stop.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing detailed service information (first stop, last stop, peak / offpeak frequency of dispatch) for all buses in operation at the time of request.
    
    Examples
    --------
    >>> get_bus_arrivals([YOUR_API_KEY], '55269')
    >>> get_bus_arrivals([YOUR_API_KEY], '83139', '15')
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    assert isinstance(bus_stop_code, str), "Please ensure that the bus stop code is entered as a string."
    assert isinstance(api_key, str), "Please ensure that the bus service number is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get(f'http://datamall2.mytransport.sg/ltaodataservice/BusArrivals?BusStopCode={bus_stop_code}&ServiceNo={service_no}', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['Services'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_bus_services(api_key):
    """
    Returns a Pandas DataFrame containing detailed service information (first stop, last stop, peak / offpeak frequency of dispatch) for all bus services.
    
    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing detailed service information (first stop, last stop, peak / offpeak frequency of dispatch) for all bus services.
    
    Examples
    --------
    >>> get_bus_services([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusServices', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_bus_routes(api_key):
    """
    Returns a Pandas DataFrame containing detailed route information (all bus stops along each route, first/last bus timings for each stop) for all services.

    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing detailed route information (all bus stops along each route, first/last bus timings for each stop) for all services.
    
    Examples
    --------
    >>> get_bus_routes([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusRoutes', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_bus_stops(api_key):
    """
    Returns a Pandas DataFrame containing detailed information (bus stop code, location coordinates) for all bus stops currently being serviced by buses.

    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing detailed information (bus stop code, location coordinates) for all bus stops currently being serviced by buses.
    
    Examples
    --------
    >>> get_bus_stops([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/BusStops', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_pass_vol_bus(api_key, date = (datetime.date.today().replace(day = 1) - datetime.timedelta(days = 1)).strftime("%Y%m")):
    """
    Returns a Pandas DataFrame containing tap in and tap out passenger volume by weekdays and weekends for individual bus stops for up to the last 3 months.
    
    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    date: str
        Character input; this is the starting date of the data.
        By default, this is set such that the last 1 month of data is returned.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing tap in and tap out passenger volume by weekdays and weekends for individual bus stop for up to the last 3 months.
    
    Examples
    --------
    >>> get_pass_vol_bus([YOUR_API_KEY])
    >>> get_pass_vol_bus([YOUR_API_KEY], '202011')
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    assert isinstance(date, str), "Please ensure that the date is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get(f'http://datamall2.mytransport.sg/ltaodataservice/PV/Bus?Date={date}', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_pass_vol_odbus(api_key, date = (datetime.date.today().replace(day = 1) - datetime.timedelta(days = 1)).strftime("%Y%m")):
    """
    Returns a Pandas DataFrame contianing number of trips by weekdays and weekends from origin to destination bus stops for up to the last 3 months.
    
    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    date: str
        Character input; this is the starting date of the data.
        By default, this is set such that the last 1 month of data is returned.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing number of trips by weekdays and weekends from origin to destination bus stops for up to the last 3 months.
    
    Examples
    --------
    >>> get_pass_vol_odbus([YOUR_API_KEY])
    >>> get_pass_vol_odbus([YOUR_API_KEY], '202011')
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    assert isinstance(date, str), "Please ensure that the date is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get(f'http://datamall2.mytransport.sg/ltaodataservice/PV/ODBus?Date={date}', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_pass_vol_odtrain(api_key, date = (datetime.date.today().replace(day = 1) - datetime.timedelta(days = 1)).strftime("%Y%m")):
    """
    Returns a Pandas DataFrame containing number of trips by weekdays and weekends from origin to destination train stations for up to the last 3 months.
    
    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    date: str
        Character input; this is the starting date of the data.
        By default, this is set such that the last 1 month of data is returned.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing number of trips by weekdays and weekends from origin to destination train stations for up to the last 3 months.
    
    Examples
    --------
    >>> get_pass_vol_odtrain([YOUR_API_KEY])
    >>> get_pass_vol_odtrain([YOUR_API_KEY], '202011')
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    assert isinstance(date, str), "Please ensure that the date is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get(f'http://datamall2.mytransport.sg/ltaodataservice/PV/ODTrain?Date={date}', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_pass_vol_train(api_key, date = (datetime.date.today().replace(day = 1) - datetime.timedelta(days = 1)).strftime("%Y%m")):
    """
    Returns a Pandas DataFrame containing tap in and tap out passenger volume by weekdays and weekends for individual train stations for up to the last 3 months.
    
    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    date: str
        Character input; this is the starting date of the data.
        By default, this is set such that the last 1 month of data is returned.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing tap in and tap out passenger volume by weekdays and weekends for individual train stations for up to the last 3 months.
    
    Examples
    --------
    >>> get_pass_vol_train([YOUR_API_KEY])
    >>> get_pass_vol_train([YOUR_API_KEY], 202011)
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    assert isinstance(date, str), "Please ensure that the date is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get(f'http://datamall2.mytransport.sg/ltaodataservice/PV/Train?Date={date}', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_taxi_availability(api_key):
    """
    Returns a Pandas DataFrame containing location coordinates of all Taxis that are currently available for hire at the time of request. "Hired" or "Busy" taxis are not included.

    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing location coordinates of all Taxis that are currently available for hire at the time of request.
    
    Examples
    --------
    >>> get_taxi_availability([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/Taxi-Availability', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_taxi_stands(api_key):
    """
    Returns a Pandas DataFrame containing detailed information of Taxi stands, such as location and whether is it barrier free, at the time of request.

    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key, at the time of request.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing detailed information of Taxi stands, such as location and whether is it barrier free.
    
    Examples
    --------
    >>> get_taxi_stands([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/TaxiStands', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_train_service_alerts(api_key):
    """
    Returns a Pandas DataFrame containing detailed information on train service unavailability during scheduled operating hours, such as affected line and stations etc., at the time of request.

    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing detailed information on train service unavailability during scheduled operating hours, such as affected line and stations etc., at the time of request.
    
    Examples
    --------
    >>> get_train_service_alerts([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/TrainServiceAlerts', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_carpark_availability(api_key):
    """
    Returns a Pandas DataFrame containing number of available lots for HDB, LTA and URA carpark data at the time of request.

    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing number of available lots for HDB, LTA and URA carpark data at the time of request.
    
    Examples
    --------
    >>> get_car_park_availability([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/CarParkAvailabilityv2', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    r_json_df[['Latitude', 'Longitude']] = r_json_df.Location.str.split(expand = True).drop([2, 3], axis = 1)
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_erp_rates(api_key):
    """
    Returns a Pandas DataFrame containing ERP rates of all vehicle types across all timings for each zone.

    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing ERP rates of all vehicle types across all timings for each zone.
    
    Examples
    --------
    >>> get_erp_rates([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/ERPRates', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_est_travel_times(api_key):
    """
    Returns a Pandas DataFrame containing estimated travel times of expressways (in segments) at the time of request.

    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing estimated travel times of expressways (in segments) at the time of request.
    
    Examples
    --------
    >>> get_est_travel_times([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/EstTravelTimes', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_faulty_traffic_lights(api_key):
    """
    Returns a Pandas DataFrame containing alerts of traffic lights that are currently faulty, or currently undergoing scheduled maintenance at the time of request.

    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing alerts of traffic lights that are currently faulty, or currently undergoing scheduled maintenance at the time of request.
    
    Examples
    --------
    >>> get_faulty_traffic_lights([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/FaultyTrafficLights', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_road_openings(api_key):
    """
    Returns a Pandas DataFrame containing all planned road openings at the time of request.

    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing all planned road openings at the time of request.
    
    Examples
    --------
    >>> get_road_openings([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/RoadOpenings', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_road_works(api_key):
    """
    Returns a Pandas DataFrame containing all road works being / to be carried out at the time of request.

    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing all road works being / to be carried out at the time of request.
    
    Examples
    --------
    >>> get_road_works([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/RoadWorks', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_traffic_images(api_key):
    """
    Returns a Pandas DataFrame containing links to images of live traffic conditions along expressways and Woodlands & Tuas Checkpoints at the time of request.

    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing links to images of live traffic conditions along expressways and Woodlands & Tuas Checkpoints at the time of request.
    
    Examples
    --------
    >>> get_traffic_images([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/Traffic_Imagesv2', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_traffic_incidents(api_key):
    """
    Returns a Pandas DataFrame containing incidents currently happening on the roads, such as Accidents, Vehicle Breakdowns, Road Blocks, Traffic Diversions etc., at the time of request.
    
    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing incidents currently happening on the roads, such as Accidents, Vehicle Breakdowns, Road Blocks, Traffic Diversions etc., at the time of request.
    
    Examples
    --------
    >>> get_traffic_incidents([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/TrafficIncidents', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_traffic_speed_bands(api_key):
    """
    Returns a Pandas DataFrame containing traffic speeds on expressways and arterial roads, expressed in speed bands at the time of request.
    
    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing traffic speeds on expressways and arterial roads, expressed in speed bands at the time of request.
    
    Examples
    --------
    >>> get_traffic_speed_bands([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/TrafficSpeedBandsv2', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    r_json_df[['Latitude', 'Longitude']] = r_json_df.Location.str.split(expand = True).drop([2, 3], axis = 1)
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_variable_messages(api_key):
    """
    Returns a Pandas DataFrame containing traffic advisories (via variable message services) concerning current traffic conditions that are displayed on EMAS signboards along expressways and arterial roads at the time of request.
    
    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing traffic advisories (via variable message services) concerning current traffic conditions that are displayed on EMAS signboards along expressways and arterial roads at the time of request.
    
    Examples
    --------
    >>> get_variable_messages([YOUR_API_KEY])
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get('http://datamall2.mytransport.sg/ltaodataservice/VMS', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_bicyle_parking(api_key, lat, long, dist = '0.5'):
    """
    Returns a Pandas DataFrame containing bicycle parking locations within a radius at the time of request.
    
    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    lat: str
        Character input; this is the latitude of the point of search.
        
    long: str
        Character input, this is the longitude of the point of search.
        
    dist: str
        Character input, this is the radius of search in kilometres.
        By default, this is set to 0.5.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing bicycle parking locations within a radius at the time of request.
    
    Examples
    --------
    >>> get_bicycle_parking([YOUR_API_KEY], '1.36666', '103.76666')
    >>> get_bicycle_parking([YOUR_API_KEY], '1.36666', '103.76666', '2.0')
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    assert isinstance(lat, str), "Please ensure that the latitude is entered as a string."
    assert isinstance(long, str), "Please ensure that the longitude is entered as a string."
    assert isinstance(distance, str), "Please ensure that the distance is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get(f'http://datamall2.mytransport.sg/ltaodataservice/BicycleParkingv2?Lat={lat}&Long={long}&Dist={dist}', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_geospatial(api_key, ID):
    """
    Returns a Pandas DataFrame containing SHP files of the requested geospatial layer at the time of request.
    
    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    ID: str
        Character input; this refers to the name of the geospatial layer.
        Please refer to Annex E in https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf for list of allowed IDs.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing SHP files of the requested geospatial layer at the time of request.
    
    Examples
    --------
    >>> get_geospatial([YOUR_API_KEY], 'RoadHump')
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    assert isinstance(ID, str), "Please ensure that the ID is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get(f'http://datamall2.mytransport.sg/ltaodataservice/GeospatialWholeIsland?ID={ID}', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df

def get_facilities_maintenance(api_key, station_code):
    """
    Returns a Pandas DataFrame containing pre-signed links to JSON file containing facilities maintenance schedules of the particular station at the time of request.
    
    Parameters
    ----------
    api_key: str
        Character input.
        Please visit https://datamall.lta.gov.sg/content/datamall/en/request-for-api.html to obtain your own API key.
    
    station_code: str
        Character input; this is the code for the train station data is requested for.
    
    Returns
    -------
    Pandas DataFrame
        The output is a dataframe containing pre-signed links to JSON file containing facilities maintenance schedules of the particular station at the time of request.
    
    Examples
    --------
    >>> get_facilities_maintenance([YOUR_API_KEY], 'NS1')
    
    """
    assert isinstance(api_key, str), "Please ensure that the API key is entered as a string."
    assert isinstance(station_code, str), "Please ensure that the ID is entered as a string."
    headers = {'AccountKey': api_key, 'accept': 'application/json'}
    r = requests.get(f'http://datamall2.mytransport.sg/ltaodataservice/FacilitiesMaintenance?StationCode={station_code}', headers = headers)
    assert r.status_code == 200, "Request is unsuccessful. Please ensure that the API key is valid."
    r_json = r.json()
    r_json_df = pd.DataFrame(r_json['value'])
    now = datetime.datetime.now()
    r_json_df['Date and Time Accessed'] = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Status Code: {r.status_code}. Request is successful.')
    return r_json_df