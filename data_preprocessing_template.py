# Data Preprocessing Template

# 1.1 Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1.2 Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values   # Except Dependednt so -1
y = dataset.iloc[:, 3].values      # Independent data column

# 1.3 Missing Dataset
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])

# 1.4 Categorial data
# By example we can see county and purchased are categorial data

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncode
labelencoder_X=LabelEncoder()          #Country
X[:,0]=labelencoder_X.fit_transform(X[:,0])                                    # it will give 0,1,2 has no significance

####Dummy encoding ##
onehotencoder=OneHotEncoder(categorical_features = [0])                          # First county column
X=onehotencoder.fit_transform(X).toarray()


"""
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""