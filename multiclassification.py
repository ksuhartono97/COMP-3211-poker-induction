import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import svm

df = pd.read_csv('balence.csv')
X = df.drop(['hand'], axis = 1)
y = df['hand']

one_class_svm_y = y.apply(lambda v: -1 if v==0 else 1)
X_train, X_test, y_train, y_test = train_test_split(X, one_class_svm_y, test_size=0.4, random_state=42)

for i in range(1, 10):
    gamma = i*0.1
    print(gamma)
    clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma= gamma)
    clf.fit(X_train)
    y_pred = clf.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
