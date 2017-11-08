import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import TomekLinks

import matplotlib.pyplot as plt

trainSet  = pd.read_csv('train.csv')
trainingEncoded = pd.get_dummies(trainSet)
# 
# trainingFeatures, testFeatures, \
#     trainingTarget, testTarget = train_test_split(trainingEncoded.drop(['hand'], axis=1),
#                                                   trainingEncoded['hand'],
#                                                   test_size=.1,
#                                                   random_state=12)

xTrain, xVal, yTrain, yVal = train_test_split(trainingEncoded.drop(['hand'], axis=1),
                                              trainingEncoded['hand'],
                                              test_size=.1,
                                              random_state=12)

clfRf = RandomForestClassifier(n_estimators=25, random_state=12)
clfRf.fit(xTrain, yTrain)

# plt.plot(yTrain, 'ro')
# plt.show()

yOrigin = pd.DataFrame(data=yTrain, columns=['hand'])
print yOrigin.hand.value_counts()

predicted = clfRf.predict(xVal)

precision, recall, fscore, support = score(yVal, predicted)

print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))


print '=============================='
print '\nWith SMOTE Rebalanced Data'

sm = SMOTE(ratio="all", kind="regular", k_neighbors=3)
xSmote, ySmote = sm.fit_sample(xTrain, yTrain)

# yRandPanda = pd.DataFrame(data=ySmote, columns=['hand'])
# print yRandPanda.hand.value_counts()


# plt.plot(ySmote, 'ro')
# plt.show()

clfRf.fit(xSmote, ySmote)

predicted = clfRf.predict(xVal)

precision, recall, fscore, support = score(yVal, predicted)

print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))

print '=============================='
print '\nWith Random Rebalanced Data'

sm = RandomOverSampler(random_state=42, ratio="all")
xRand, yRand = sm.fit_sample(xTrain, yTrain)

# yRandPanda = pd.DataFrame(data=yRand, columns=['hand'])
# print yRandPanda.hand.value_counts()

clfRf.fit(xRand, yRand)

predicted = clfRf.predict(xVal)

precision, recall, fscore, support = score(yVal, predicted)

print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))

print '=============================='
print '\nWith Tomek Links Rebalanced Data'

tl = TomekLinks(random_state=12)
xTl, yTl = tl.fit_sample(xTrain, yTrain)

# yRandPanda = pd.DataFrame(data=yTl, columns=['hand'])
# print yRandPanda.hand.value_counts()

clfRf.fit(xTl, yTl)

predicted = clfRf.predict(xVal)

precision, recall, fscore, support = score(yVal, predicted)

print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))
