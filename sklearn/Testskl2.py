#ML-Linear Regression model
import pandas as pd
import numpy as np
import sklearn
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
boston_dataset = load_boston()

#store dataset in a dataframe
df_boston = pd.DataFrame(boston_dataset.data)
df_boston.columns = boston_dataset.feature_names

#define the target column (in this case prices of houses)
df_boston['Price'] = boston_dataset.target

print(df_boston.head())

#assign attributes/features to x-axis
X_features = boston_dataset.data

#assign target on Y axis
Y_target = boston_dataset.target

#To use sklearn lr model import its class & create an object called estimator to instantiate

from sklearn.linear_model import LinearRegression
lineReg = LinearRegression()

#fit data into estimator (ie model object lineReg)
lineReg.fit(X_features,Y_target)

#print the intercept
#%2f is used to round of decimal numbers to 2
print('the estimated intercept %.2f ' %lineReg.intercept_)

#print coefficients
print('the coefficients is %d ' %len(lineReg.coef_))

#use cross validation to train the model
#import cross validation class & split data for train & test

X_train,X_test,Y_train,Y_test = train_test_split(X_features,Y_target)


print(boston_dataset.data.shape)
print(X_train.shape, X_test.shape,Y_train.shape,Y_test.shape)

#fit training dataset into model
lineReg.fit(X_train,Y_train)

#mean square error or residual sum of sqaures
print('MSE value is %.2f ' % np.mean((lineReg.predict(X_test)-Y_test) ** 2))
y_pred = lineReg.predict(X_test)
print(y_pred)


#calc variance
#use score method, closer the value to 1, higher would be the accuracy
print('variance score is %.2f ' % lineReg.score(X_test,Y_test))

#import required libs for calculating MSE to test accuracy of model
#from sklearn import metrics
#print(np.sqrt(metrics.mean_squared_error(Y_test,y_pred)))







