
# coding: utf-8

# In[59]:


import numpy as np
import pandas as pd
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC


# In[2]:


trainSet  = pd.read_csv('train.csv')
trainingEncoded = pd.get_dummies(trainSet)
x = trainingEncoded.drop(['hand'], axis=1)
y = trainingEncoded['hand']

xTrain, xVal, yTrain, yVal = train_test_split(x,
                                              y,
                                              test_size=.1,
                                              random_state=12)


# In[3]:


testY = pd.DataFrame(data=yVal, columns=['hand'])
print testY.hand.value_counts()


# In[39]:


clfRf = RandomForestClassifier(n_estimators=10, random_state=12)
clfRf.fit(xTrain, yTrain)


# In[40]:


rfPredicted = clfRf.predict(xVal)


# In[41]:


print metrics.classification_report(yVal, rfPredicted)


# In[12]:


mlpClf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1, max_iter=2000)
mlpClf.fit(xTrain, yTrain)


# In[14]:


mlpPredicted = mlpClf.predict(xVal)


# In[15]:


print metrics.classification_report(yVal, mlpPredicted)


# In[25]:


svcClf = SVC()
svcClf.fit(xTrain,yTrain)


# In[26]:


svcPredicted = svcClf.predict(xVal)


# In[28]:


print metrics.classification_report(yVal, svcPredicted)


# In[32]:


abClf = AdaBoostClassifier()
abClf.fit(xTrain, yTrain)


# In[33]:


abPredicted = abClf.predict(xVal)


# In[35]:


print metrics.classification_report(yVal, abPredicted)


# In[43]:


bgClf = BaggingClassifier()
bgClf.fit(xTrain, yTrain)


# In[44]:


bgPredicted = bgClf.predict(xVal)


# In[45]:


print metrics.classification_report(yVal, bgPredicted)


# In[47]:


etClf = ExtraTreesClassifier()
etClf.fit(xTrain, yTrain)


# In[48]:


etPredicted = etClf.predict(xVal)


# In[49]:


print metrics.classification_report(yVal, etPredicted)


# In[58]:


gbcClf = GradientBoostingClassifier()
gbcClf.fit(xTrain, yTrain)


# In[60]:


gbcPredicted = gbcClf.predict(xVal)


# In[62]:


print metrics.classification_report(yVal, gbcPredicted)
