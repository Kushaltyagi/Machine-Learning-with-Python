# -*- coding: utf-8 -*-
"""Data Standardization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mctM6KBihS0y1nLuNn1R_4XzlGl77CFT

Data Standardization:
 The process of standarising the data to a common format and common range
"""

import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# loading the dataset
dataset = sklearn.datasets.load_breast_cancer()

#loading data to pandas dataframe
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

df.head()

df.shape

x = df
y = dataset.target
print(x)

print(y)

"""Splitting data into training data and test data"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 3)

print(x.shape, x_train.shape, x_test.shape)

"""Standardize the data"""

print(dataset.data.std()) # if standard deviation is 1 or close to 1 it means all values in the data is in same range

scaler = StandardScaler()
scaler.fit(x_train)

x_train_standardized = scaler.transform(x_train)
print(x_train_standardized)

x_test_standardized = scaler.transform(x_test)
print(x_test_standardized)

print(x_train_standardized.std())

print(x_test_standardized.std())

