import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


#importing tha dataset
dataset = pd.read_csv('G:\python\ML course\Data.csv')

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

#print(x)

#spliting dataset into the training
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
print(x_test)