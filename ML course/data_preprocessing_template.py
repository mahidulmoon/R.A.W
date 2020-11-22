import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder


#importing tha dataset
dataset = pd.read_csv('Data.csv')

#iloc[row,column]
x = dataset.iloc[:, :-1].values #independent values
y = dataset.iloc[:,-1:].values  #dependent values

#changing null/empty value with the mean value of the column
simp = SimpleImputer(missing_values = 'NaN', strategy = 'mean')
simp = SimpleImputer().fit(x[:, 1:3]) 
x[:, 1:3] = simp.transform(x[:, 1:3])

#envoding categorial data
lablerencoder_x = LabelEncoder()
x[:,0] = lablerencoder_x.fit_transform(x[:,0])

print(x)