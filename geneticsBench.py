import numpy as np
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.model_selection import train_test_split
from gplearn.genetic import SymbolicRegressor
import matplotlib.pyplot as plt
trainSet  = pd.read_csv('train.csv')
trainingEncoded = pd.get_dummies(trainSet)

trainingFeatures, testFeatures, \
    trainingTarget, testTarget = train_test_split(trainingEncoded.drop(['hand'], axis=1),
                                                  trainingEncoded['hand'],
                                                  test_size=.1,
                                                  random_state=12)

xTrain, xVal, yTrain, yVal = train_test_split(trainingFeatures, trainingTarget,
                                              test_size= .25,
                                              random_state=12)

est_gp = SymbolicRegressor(population_size=1000,
                           generations=20, stopping_criteria=0.01,
                           p_crossover=0.7, p_subtree_mutation=0.1,
                           p_hoist_mutation=0.05, p_point_mutation=0.1,
                           max_samples=0.9, verbose=1,
                           parsimony_coefficient=0.01, random_state=0)

est_gp.fit(xTrain, yTrain)

predicted = est_gp.predict(xVal)

# print predicted
plt.plot(predicted)
plt.plot(yVal)
plt.show()

# precision, recall, fscore, support = score(yVal, predicted)
