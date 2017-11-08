import numpy as np
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

trainSet  = pd.read_csv('train.csv')
trainingEncoded = pd.get_dummies(trainSet)

x = trainingEncoded.drop(['hand'], axis=1)
y = trainingEncoded['hand']

clfRf = RandomForestClassifier(n_estimators=25, random_state=12)
clfRf.fit(x, y)

y = pd.DataFrame(data=y, columns=['hand'])
print y.hand.value_counts()

predicted = clfRf.predict(x)

precision, recall, fscore, support = score(y, predicted)

print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))
