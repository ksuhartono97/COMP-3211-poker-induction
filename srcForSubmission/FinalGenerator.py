
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score
from sklearn.feature_selection import RFE
from sklearn.pipeline import Pipeline
# from imblearn.combine import SMOTETomek
# from imblearn.over_sampling import SMOTE
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC


# In[2]:


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


# In[3]:


#Printing out the hand distribution values
pdY = pd.DataFrame(data=y, columns=['hand'])
print "Data distribution for the hand"
print pdY.hand.value_counts()


# In[4]:


# Trying out SMOTE and Tomek Chains for over and under sampling of data
# smt = SMOTETomek(random_state=42, smote=SMOTE(random_state=12, ratio='all', k_neighbors=4))
# smt = SMOTE(random_state=12, ratio='all', k_neighbors=4)
# x, y = smt.fit_sample(x, y)
# Not a lot of improvement


# In[5]:


# Chi2 reduced the score by a lot too, even with the best k
# chi2 = SelectKBest(chi2, k=7)
# xTrain = chi2.fit_transform(xTrain, yTrain);
# xVal = chi2.transform(xVal);


# In[6]:


#Generate the model for RFE
model = RandomForestClassifier(n_estimators= 140, max_features= 'auto',random_state= 22337, criterion= 'gini')


# In[7]:


#Create our classifier
clf = Pipeline([
    ('feature_selection', RFE(model, 5)),
    ('classification', RandomForestClassifier(n_estimators= 140, max_features= 'auto',random_state= 22337, criterion= 'gini'))
])
#Fit the dataset to the classifier
clf.fit(xTrain, yTrain)


# In[8]:


#Doing the prediction (testing split)
pipePredicted = clf.predict(xVal)

#Labelling the result
pdPipePredicted = pd.DataFrame(data=pipePredicted, columns=['hand'])

#Printing test metrics
print pdPipePredicted.hand.value_counts()
print metrics.classification_report(yVal, pdPipePredicted)


# In[9]:


# Printout the confusion matrix
print confusion_matrix(yVal, pdPipePredicted)


# In[10]:


# Here on is submission generation, only run if needed (don't run over this point), if on .py file, may want to comment this part
# Open and encode the test dataset
testSet  = pd.read_csv('test.csv')
testEncoded = pd.get_dummies(testSet)
testX = testEncoded.drop(['id'], axis=1)


# In[11]:


#Refit with whole set
clf.fit(x, y)


# In[12]:


# Predict the result
resultDataRF = clf.predict(testX)


# In[13]:


# Construct a csv file for submission to kaggle
pdResultDataRF = pd.DataFrame(data=resultDataRF, columns=['hand'])
pdResultDataRF.index += 1
print pdResultDataRF.hand.value_counts()
pdResultDataRF.to_csv("submission.csv", index_label='id', columns=['hand'])

