import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importing tha dataset
dataset = pd.read_csv('Data.csv')

#iloc[row,column]
x = dataset.iloc[:, :].values
print(x)