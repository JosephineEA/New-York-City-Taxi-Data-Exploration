import pandas as pd
import os

def get_taxi_data(year, month, vehicles='yellow', columns=None, save=False, localpath=""):
    '''
    Downloads ride data from TLC for a given month,
    and returns it as a pandas DataFrame.
    
    NOTE: the data file can be several gigabytes! Use carefully.
    (See the 'columns' input below.)
    
    Input:
    - year (str): the year of the data we want (2009-2022)
    - month (str): the month of the data we want (01-12)
    - vehicles (str): the type of vehicles we're interested in.
        Must be one of 'yellow', 'green', 'fhv', 'fhvhv' (default 'yellow').
    - columns (list): list of specific columns we want to read (default None, which
        reads every column in the data file). Use this to load a subset of the data
        in your computer's memory.
    - save (bool): whether to save the file on disk for later use (to avoid having to
        re-download it every time). (default: False)
    
    Output:
    - df (pd.DataFrame): the data as a Pandas DataFrame.
    '''
    # Create the file name as per specifications
    filename = f'{vehicles}_tripdata_{year}-{month}.parquet'
    
    # Assume we will need to download the data
    download = True
    
    try:
        # If the data file is already in the folder, then this will work
        df = pd.read_parquet(localpath+filename, columns=columns)
        
    except FileNotFoundError:
        # The file isn't in the current folder; maybe it hasn't been saved yet
        print('File not in current folder; trying to download data...')
        
    except:
        # The file was found in the current folder, but maybe it was saved earlier
        # with fewer columns than what we need now. We need to re-download the data.
        print('File is in current folder, but may not contain all required columns.')
        print('Re-downloading data...')
        
    else:
        # If the command in the "try:" block has worked, then we don't need to download data
        download = False
    
    # If we need to download the data, append the URL to the file name, and read it
    if download:
        path = 'https://d37ci6vzurychx.cloudfront.net/trip-data/' + filename
        df = pd.read_parquet(path, columns=columns)
    
    # Save the file to the current folder
    if save:
        df.to_parquet(localpath+filename)
    
    return df
