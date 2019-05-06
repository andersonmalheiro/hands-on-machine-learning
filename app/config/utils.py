import os
import pandas as pd

def getHousingData():
  df = pd.read_csv('../datasets/housing.csv')
  return df