import pandas as pd
import numpy as np
import sklearn
from app.config.utils import getHousingData

housing_data = getHousingData()

print(housing_data.head())
