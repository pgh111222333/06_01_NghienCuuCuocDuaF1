import pandas as pd 
from data.data_loader import load_data

def load_less_data():
    df = load_data()
    return df