
# coding: utf-8

# In[1]:


import sklearn.datasets
import numpy as np
import random
import pandas as pd
import sklearn.metrics as metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import ExtraTreesClassifier


# In[2]:


# Open the training dataset
trainSet  = pd.read_csv('train.csv')
trainingEncoded = pd.get_dummies(trainSet)
x = trainingEncoded.drop(['hand'], axis=1)
y = trainingEncoded['hand']


# In[3]:


# Construct the parameters that we want
paramgrid = {"n_estimators": [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140],
             "criterion":["gini","entropy"],
             "max_features":["auto","sqrt","log2"],
             "random_state":np.arange(1,100000),
            }
             
random.seed(12)


# In[7]:


# Run the evolutionary search (this part takes a really long time)
from evolutionary_search import EvolutionaryAlgorithmSearchCV
cv = EvolutionaryAlgorithmSearchCV(estimator=RandomForestClassifier(),
                                   params=paramgrid,
                                   scoring="accuracy",
                                   cv=StratifiedKFold(n_splits=5),
                                   verbose=1,
                                   population_size=100,
                                   gene_mutation_prob=0.1,
                                   gene_crossover_prob=0.5,
                                   tournament_size=4,
                                   generations_number=9,
                                   n_jobs=-1)
cv.fit(x, y)

