# -*- coding: utf-8 -*-
"""Handling Missing Value.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VgNcNEjAqXOoq6kzEkQGtOKPi4s0GeHk

Methods to Handle Missing Value:

*   Imputation
*   Dropping

Importing the Libraries
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading the dataset to Pandas Dataframe
dataset = pd.read_csv('/content/Placement_Dataset.csv')

dataset.head()

dataset.shape

dataset.isnull().sum()

"""Central Tendencies:

*   Mean
*   Median
*   Mode


"""

# analyse the distribution of data in the salary
 fig, ax = plt.subplots(figsize = (8,8))
 sns.distplot(dataset.salary)

"""Replace the missing value with median values"""

dataset['salary'].fillna(dataset['salary'].median(), inplace = True)
# dataset['salary'].fillna(dataset['salary'].mean(), inplace = True)

dataset.isnull().sum()

"""Dropping Method"""

salary_dataset = pd.read_csv('/content/Placement_Dataset.csv')

salary_dataset.isnull().sum()

# drop missing value rows
salary_dataset = salary_dataset.dropna(how = 'any')

salary_dataset.isnull().sum()

salary_dataset.shape

