# -*- coding: utf-8 -*-
"""Train Test Split.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XGTz2ln_rmhl_-eWed0yFHJS2Df1gakz

Importing Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection and Analysis

Diabetes Dataset
"""

# loading the dataset to pandas DataFrame
diabetes_dataset = pd.read_csv('/content/diabetes.csv')
diabetes_dataset.head()

diabetes_dataset.shape

diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

diabetes_dataset.groupby('Outcome').mean()

# separating the data and labels
 x = diabetes_dataset.drop(columns = 'Outcome', axis=1)
 y = diabetes_dataset['Outcome']
 print(x)
 print(y)

"""Data Standardization"""

scaler = StandardScaler()
scaler.fit(x)

standardized_data = scaler.transform(x)
print(standardized_data)

x = standardized_data
y = diabetes_dataset['Outcome']
print(x)
print(y)

"""Splitting the data in Training and Testing Data"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2)

print(x.shape, x_train.shape, x_test.shape)

