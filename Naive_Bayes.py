#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


Cancer=pd.read_csv('NCHS_-_Potentially_Excess_Deaths_from_the_Five_Leading_Causes_of_Death.csv')


# In[3]:


Cancer


# In[4]:


print(Cancer.head())
print(Cancer.tail())
print(Cancer.shape)
(Cancer.describe())


# In[5]:


#converting Categorical Features into numeric feature
from sklearn.preprocessing import LabelEncoder


# In[6]:


convert=LabelEncoder()


# In[7]:


Cancer['Cause of Death']=convert.fit_transform(Cancer['Cause of Death'].astype(str))


# In[8]:


Cancer.drop(['State','State FIPS Code','Year'],axis=1,inplace=True)
Cancer.drop(['Age Range'],axis=1,inplace=True)


# In[9]:


Cancer['Benchmark']=convert.fit_transform(Cancer['Benchmark'].astype(str))
Cancer['Locality']=convert.fit_transform(Cancer['Locality'].astype(str))


# In[10]:


Cancer


# In[11]:


Cancer.isnull().any()


# In[12]:


Cancer.isnull().any()
Cancer = Cancer.fillna(method='ffill')


# In[13]:


Cancer.info()


# In[14]:


Cancer.hist(bins=50,figsize=(20,15))


# In[15]:


import seaborn as sns


# In[16]:


def corr(x):
    corrmat=x.corr()
    print(corrmat)
    f, ax=plt.subplots(figsize=(12,9))
    sns.heatmap(corrmat,vmax=1,vmin=-1,square=True);


# In[17]:


corr(Cancer)


# In[18]:


X=Cancer.drop('Cause of Death',axis=1).values


# In[19]:


X


# In[20]:


y=Cancer['Cause of Death'].values


# In[21]:


y


# In[22]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=(0.20),random_state=42)


# In[23]:


X_train.shape


# In[24]:


X_train


# In[ ]:





# In[25]:


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()


# In[26]:


X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


# In[27]:


from sklearn.naive_bayes import BernoulliNB


# In[28]:


classi=BernoulliNB()


# In[29]:


classi.fit(X_train,y_train)


# In[30]:


y_predict=classi.predict(X_test)


# In[31]:


from sklearn.metrics import confusion_matrix
Con=confusion_matrix(y_test,y_predict)


# In[32]:


Con


# In[33]:


Conf_matrix=confusion_matrix(y_test,y_predict)
sns.heatmap(Conf_matrix,annot=True)


# In[ ]:





# In[34]:


from sklearn import metrics
print("Accuracy of Model:",metrics.accuracy_score(y_test, y_predict))


# In[35]:


print('Accuracy of Model on training set: {:.2f} \n'.format(classi.score(X_train, y_train)))
print('Accuracy of Model on test set: {:.2f} \n' .format(classi.score(X_test, y_test)))


# In[ ]:




