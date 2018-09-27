# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# By example we can see county and purchased are categorial data

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
labelencoder_X=LabelEncoder()          #Country
X[:,3]=labelencoder_X.fit_transform(X[:,3])                                    # it will give 0,1,2 has no significance

####Dummy encoding ##
onehotencoder=OneHotEncoder(categorical_features = [3])                        # First county column
X=onehotencoder.fit_transform(X).toarray()


# Avoiding the dummy variable trap
X=X[:,1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = 0.2, 
                                                    random_state = 0)


# Fitting multiple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

#Predicting the test results

y_pred=regressor.predict(X_test)




