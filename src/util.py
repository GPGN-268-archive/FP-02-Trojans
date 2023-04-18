import pandas as pd

def get_small_bodies(filepath):
    
    """
    Takes in a filepath and returns a dataframe of small bodies
    
    Parameters
    ----------
    str: filepath
          Path to csv file containing small body dataset
          
    Returns
    -------
    pd.DataFrame: data
          Data frame containing small body orbital information
    """
    
    data = pd.read_csv("~/Downloads/sbdb_query_results.csv", low_memory=False)
    return data
    
def sort_by_type(data):
    
    """
    Takes in a dataframe of small body information and returns
    as a dictionary split by the type of small body.
    
    Parameters
    ----------
    pd.DataFrame: data
          Data frame containing small body orbital information
          
    Returns
    -------
    dict: output
          Dictionary of dataframes divided by small body type
          Keys are [TJN, CEN, OMB]
    """
          
    trojans = data[data["class"] == "TJN"]
    centaurs = data[data["class"] == "CEN"]
    outermb = data[data["class"] == "OMB"]
    
    return {"TJN":trojans, "CEN":centaurs, "OMB":outermb}