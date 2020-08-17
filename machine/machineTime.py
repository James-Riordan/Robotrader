from sklearn import svm
from sklearn.model_selection import train_test_split

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
import random

from convertData import convertData

def shuffleData(X, y):
  temp = list(zip(X, y)) 
  random.Random(4).shuffle(temp) 
  X, y = zip(*temp) 
  return X, y

def rbfRegression(X, y):
  x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

  clf = svm.SVR(kernel='rbf', C=.01, gamma=.01, epsilon=0.1)
  clf.fit(x_train, y_train)
  prediction = clf.predict(x_test)
  error = 0
  length = len(prediction)
  totalGain = 0
  for i in range(0, len(prediction)):
    if(y_test[i]!=0):
      error += abs((prediction[i]- y_test[i])/y_test[i])*100
      posNeg = prediction[i]/y_test[i]
      # if positive, it's a gain since the prediction and the test are in same direction
      print(posNeg/abs(posNeg))
      totalGain += posNeg / abs(posNeg) * abs(prediction[i] - y_train[i])
    else:
      length -= 1
  error = error/length
  print(error, totalGain)

  return

def getMachineData(dfs, days = 7):
  X, y = [], []
  
  for count, df in enumerate(dfs):
    start = dt.datetime(2020, 7, 1)
    for lp in range(1000):
      try:
        startY = df.loc[start]['Close']
        endY = df.loc[start + dt.timedelta(days=days)]['Close'] #Open or close?
        dayX = startY - df.loc[start - dt.timedelta(days=1)]['Close']
        weekX = startY - df.loc[start - dt.timedelta(days=7)]['Close']
        monthX = startY - df.loc[start - dt.timedelta(days=30)]['Close']
        X.append([dayX, dayX, weekX, monthX])
        y.append(endY - startY)
      except:
        pass
      start = start - dt.timedelta(days=1)

  X, y = shuffleData(X, y)
  
  return rbfRegression(X, y)

 

