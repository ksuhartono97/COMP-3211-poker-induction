import numpy as np
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC

trainSet  = pd.read_csv('train.csv')
trainingEncoded = pd.get_dummies(trainSet)

# trainingFeatures, testFeatures, \
#     trainingTarget, testTarget = train_test_split(trainingEncoded.drop(['hand'], axis=1),
#                                                   trainingEncoded['hand'],
#                                                   test_size=.1,
#                                                   random_state=12)

xTrain, xVal, yTrain, yVal = train_test_split(trainingEncoded.drop(['hand'], axis=1),
                                              trainingEncoded['hand'],
                                              test_size= .25,
                                              random_state=12)

clfRf = SVC()
clfRf.fit(xTrain, yTrain)

predicted = clfRf.predict(xVal)

print confusion_matrix(predicted, yVal)
