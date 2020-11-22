import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer


#importing tha dataset
dataset = pd.read_csv('Data.csv')

#iloc[row,column]
x = dataset.iloc[:, :-1].values #independent values
y = dataset.iloc[:,-1:].values  #dependent values


simp = SimpleImputer(missing_values = 'NaN', strategy = 'mean')
simp = SimpleImputer().fit(x[:, 1:3]) 
x[:, 1:3] = simp.transform(x[:, 1:3])


print(x)