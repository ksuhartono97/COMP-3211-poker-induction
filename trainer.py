import csv
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import RandomOverSampler

from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

X = [] # the hands
y = [] # the predicted hand you should play
testX = []
testY = []
resultDataLR = []
resultDataMLP = []

ctr = 0

handArrCount = [0,0,0,0,0,0,0,0,0,0]

# Oversampling stuff

trainSet  = pd.read_csv('train.csv')

model_variables = ['S1', 'C1', 'S2', 'C2', 'S3', 'C3',
                   'S4', 'C4', 'S5', 'C5', 'hand']

trainingDataRelevant = trainSet[model_variables]

trainingEncoded = pd.get_dummies(trainingDataRelevant)

trainingFeatures, testFeatures, \
    trainingTarget, testTarget = train_test_split(trainingEncoded.drop(['hand'], axis=1),
                                                  trainingEncoded['hand'],
                                                  test_size=.1,
                                                  random_state=12)

xTrain, xVal, yTrain, yVal = train_test_split(trainingFeatures, trainingTarget,
                                              test_size= .1,
                                              random_state=12)

# sm = SMOTE(random_state=12, ratio="minority")
sm = RandomOverSampler(random_state=12, ratio="minority")

xTrainRes, yTrainRes = sm.fit_sample(xTrain, yTrain)

clfRf = RandomForestClassifier(n_estimators=25, random_state=12)
clfRf.fit(xTrainRes, yTrainRes)

print('Validation results')
print(clfRf.score(xVal, yVal))
# print(recall_score(yVal, clfRf.predict(xVal)))
print('\nTest Results')
print(clfRf.score(testFeatures, testTarget))
# print(recall_score(testTarget, clfRf.predict(testFeatures)))

# Old Code Area, for testing non oversampled
with open('train.csv', 'rb') as csvfile:
    fileReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(fileReader);
    for row in fileReader:
        # print row
        splitted = row[0].split(',')
        handList = splitted[:-1]
        handList = map(int, handList)
        # Appending the row data to respective arrays
        ctr = ctr+1
        if ctr < 5002 :
            X.append(np.array(handList))
            y.append(int(splitted[-1]))
            handArrCount[int(splitted[-1])] = handArrCount[int(splitted[-1])] + 1
        else :
            testX.append(np.array(handList))
            testY.append(int(splitted[-1]))


# with open('test.csv', 'rb') as csvfile:
#     testReadResult = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     next(testReadResult);
#     ctr = 0;
#     for row in testReadResult:
#         # print row
#         splitted = row[0].split(',')
#         handList = splitted[1:]
#         handList = map(int, handList)
#         # Appending the row data to respective arrays
#         testData.append(handList)
#         ctr= ctr+1
#         if ctr == 100:
#             break

lr = LogisticRegression(max_iter=10000)
lr.fit(X,y)

clf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X,y)

# print handArrCount

rf = RandomForestClassifier(n_estimators=25, random_state=12)
rf.fit(X, y)
print "Random forest, no oversampling"
print rf.score(testX, testY)

rf.fit(xTrainRes, yTrainRes)
print "Random forest, oversampling"
print rf.score(xVal, yVal)

resultDataRF = rf.predict(testX)

print resultDataRF

resultPanda = pd.DataFrame(data=resultDataRF, columns=['hand'])
print resultPanda.hand.value_counts()

# For generating the submission

# predictionX = []
#
# with open('test.csv', 'rb') as csvfile:
#     testReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     next(testReader);
#     for row in testReader:
#         splitted = row[0].split(',')
#         handList = splitted[1:]
#         predictionX.append(np.array(handList))
#
# resultDataRF = rf.predict(predictionX)
#
# #File Writing Part
# print "Test File Results"
# print resultDataRF
#
# resultPanda = pd.DataFrame(data=resultDataRF, columns=['hand'])
# print resultPanda.hand.value_counts()
# resultPanda.index += 1
# resultPanda.to_csv("submission.csv", index_label='id', columns=['hand'])

# resultDataLR = lr.predict(testX)
# resultDataMLP = clf.predict(testX)
#
# print "Logistic Regression, no oversampling"
# print lr.score(testX, testY)
#
# print "Logistic Regression, oversampling"
# lr.fit(xTrainRes, yTrainRes)
# print lr.score(testX, testY)
#
# print "Multi Layer Perceptron, no oversampling"
# print clf.score(testX, testY)
#
# print "Multi Layer Perceptron, oversampling"
# clf.fit(xTrainRes, yTrainRes)
# print clf.score(testX, testY)