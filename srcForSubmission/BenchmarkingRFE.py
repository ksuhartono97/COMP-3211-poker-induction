
# coding: utf-8

# In[25]:


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


# In[3]:


# Generate Training Data
trainSet  = pd.read_csv('train.csv')
trainingEncoded = pd.get_dummies(trainSet)
x = trainingEncoded.drop(['hand'], axis=1)
y = trainingEncoded['hand']
xTrain, xVal, yTrain, yVal = train_test_split(x, 
                                              y,
                                              test_size=.1,
                                              random_state=12)


# In[4]:


# Convert to panda data frame for printing contents
pdTraining = pd.DataFrame(data=yTrain, columns=['hand'])
print pdTraining.hand.value_counts()


# In[5]:


# Print out the testing set contents
pdTest = pd.DataFrame(data=yVal, columns=['hand'])
print pdTest.hand.value_counts()


# In[6]:


# Make the classifier
model = RandomForestClassifier(n_estimators=30, random_state=12)


# In[7]:


# Fit the model with training data and do benchmarking with different number of attributes
rfe = RFE(model, 2)
rfe = rfe.fit(xTrain, yTrain)
# print rfe.support_
# print rfe.ranking_
rfePredicted = rfe.predict(xVal)

pdRfePredicted = pd.DataFrame(data=rfePredicted, columns=['hand'])
print pdRfePredicted.hand.value_counts()

print metrics.classification_report(yVal, pdRfePredicted)


# In[8]:


rfe = RFE(model, 3)
rfe = rfe.fit(xTrain, yTrain)
# print rfe.support_
# print rfe.ranking_
rfePredicted = rfe.predict(xVal)

pdRfePredicted = pd.DataFrame(data=rfePredicted, columns=['hand'])
print pdRfePredicted.hand.value_counts()

print metrics.classification_report(yVal, pdRfePredicted)


# In[9]:


rfe = RFE(model, 4)
rfe = rfe.fit(xTrain, yTrain)
# print rfe.support_
# print rfe.ranking_
rfePredicted = rfe.predict(xVal)

pdRfePredicted = pd.DataFrame(data=rfePredicted, columns=['hand'])
print pdRfePredicted.hand.value_counts()

print metrics.classification_report(yVal, pdRfePredicted)


# In[10]:


rfe = RFE(model, 5)
rfe = rfe.fit(xTrain, yTrain)
# print rfe.support_
# print rfe.ranking_
rfePredicted = rfe.predict(xVal)

pdRfePredicted = pd.DataFrame(data=rfePredicted, columns=['hand'])
print pdRfePredicted.hand.value_counts()

print metrics.classification_report(yVal, pdRfePredicted)


# In[11]:


rfe = RFE(model, 6)
rfe = rfe.fit(xTrain, yTrain)
# print rfe.support_
# print rfe.ranking_
rfePredicted = rfe.predict(xVal)

pdRfePredicted = pd.DataFrame(data=rfePredicted, columns=['hand'])
print pdRfePredicted.hand.value_counts()

print metrics.classification_report(yVal, pdRfePredicted)


# In[12]:


rfe = RFE(model, 7)
rfe = rfe.fit(xTrain, yTrain)
# print rfe.support_
# print rfe.ranking_
rfePredicted = rfe.predict(xVal)

pdRfePredicted = pd.DataFrame(data=rfePredicted, columns=['hand'])
print pdRfePredicted.hand.value_counts()

print metrics.classification_report(yVal, pdRfePredicted)


# In[13]:


rfe = RFE(model, 8)
rfe = rfe.fit(xTrain, yTrain)
# print rfe.support_
# print rfe.ranking_
rfePredicted = rfe.predict(xVal)

pdRfePredicted = pd.DataFrame(data=rfePredicted, columns=['hand'])
print pdRfePredicted.hand.value_counts()

print metrics.classification_report(yVal, pdRfePredicted)


# In[14]:


rfe = RFE(model, 9)
rfe = rfe.fit(xTrain, yTrain)
# print rfe.support_
# print rfe.ranking_
rfePredicted = rfe.predict(xVal)

pdRfePredicted = pd.DataFrame(data=rfePredicted, columns=['hand'])
print pdRfePredicted.hand.value_counts()

print metrics.classification_report(yVal, pdRfePredicted)


# In[15]:


rfe = RFE(model, 10)
rfe = rfe.fit(xTrain, yTrain)
# print rfe.support_
# print rfe.ranking_
rfePredicted = rfe.predict(xVal)

pdRfePredicted = pd.DataFrame(data=rfePredicted, columns=['hand'])
print pdRfePredicted.hand.value_counts()

print metrics.classification_report(yVal, pdRfePredicted)


# In[16]:


# Create a new classifier, using pipeline
# Using RFE for feature selection and final classification model using RF
clf = Pipeline([
    ('feature_selection', RFE(model, 6)),
    ('classification', RandomForestClassifier(n_estimators=30))
])
clf.fit(xTrain, yTrain)


# In[17]:


# Predict the result
pipePredicted = clf.predict(xVal)

pdPipePredicted = pd.DataFrame(data=pipePredicted, columns=['hand'])
print pdPipePredicted.hand.value_counts()

# Print out the score report
print metrics.classification_report(yVal, pdPipePredicted)

