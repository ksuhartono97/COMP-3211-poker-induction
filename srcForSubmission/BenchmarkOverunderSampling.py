
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score
from sklearn.feature_selection import RFE
from sklearn.pipeline import Pipeline
from imblearn.combine import SMOTETomek
from imblearn.over_sampling import SMOTE
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC


# In[12]:


#Importing the training dataset
trainSet  = pd.read_csv('train.csv')
#Encoding the dataset (as per standards)
trainingEncoded = pd.get_dummies(trainSet)
x = trainingEncoded.drop(['hand'], axis=1)
y = trainingEncoded['hand']
#Splitting the datasets to independent training and test splits for later use (randomly)
xTrain, xVal, yTrain, yVal = train_test_split(x, 
                                              y,
                                              test_size=.1,
                                              random_state=12)


# In[13]:


# Trying out SMOTE and Tomek Chains for over and under sampling of data
# smt = SMOTETomek(random_state=42, smote=SMOTE(random_state=12, ratio='all', k_neighbors=4))
smt = SMOTE(random_state=12, ratio='all', k_neighbors=4)
xTrain, yTrain = smt.fit_sample(xTrain, yTrain)


# In[14]:


#Generate the model for RFE
model = RandomForestClassifier(n_estimators= 140, max_features= 'auto',random_state= 22337, criterion= 'gini')


# In[15]:


#Create our classifier
clf = Pipeline([
    ('feature_selection', RFE(model, 5)),
    ('classification', RandomForestClassifier(n_estimators= 140, max_features= 'auto',random_state= 22337, criterion= 'gini'))
])
#Fit the dataset to the classifier
clf.fit(xTrain, yTrain)


# In[16]:


#Doing the prediction (testing split)
smotePred = clf.predict(xVal)

#Labelling the result
pdSmotePred= pd.DataFrame(data=smotePred, columns=['hand'])

#Printing test metrics
print pdSmotePred.hand.value_counts()
print metrics.classification_report(yVal, pdSmotePred)


# In[18]:


# Trying out SMOTE and Tomek Chains for over and under sampling of data
smtTmk = SMOTETomek(random_state=42, smote=SMOTE(random_state=12, ratio='all', k_neighbors=4))
# smt = SMOTE(random_state=12, ratio='all', k_neighbors=4)
xTrain, yTrain = smtTmk.fit_sample(xTrain, yTrain)


# In[19]:


#Create our classifier
clf2 = Pipeline([
    ('feature_selection', RFE(model, 5)),
    ('classification', RandomForestClassifier(n_estimators= 140, max_features= 'auto',random_state= 22337, criterion= 'gini'))
])
#Fit the dataset to the classifier
clf2.fit(xTrain, yTrain)


# In[20]:


#Doing the prediction (testing split)
smtTmkPred = clf2.predict(xVal)

#Labelling the result
pdSmtTmkPred= pd.DataFrame(data=smtTmkPred, columns=['hand'])

#Printing test metrics
print pdSmtTmkPred.hand.value_counts()
print metrics.classification_report(yVal, pdSmtTmkPred)

