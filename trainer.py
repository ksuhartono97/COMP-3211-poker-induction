import csv
import numpy as np
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

with open('train.csv', 'rb') as csvfile:
    trainReadResult = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(trainReadResult);
    for row in trainReadResult:
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

print handArrCount

resultDataLR = lr.predict(testX)
resultDataMLP = clf.predict(testX)

print lr.score(testX, testY)
print clf.score(testX, testY)
