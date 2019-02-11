import numpy as np
import pandas as pd
dataset = pd.read_csv("/home/risana/Downloads/Signal-Processing--master/5.Py_Scripts/priya_inspiring_india.csv")
from sklearn.ensemble import AdaBoostClassifier
labels='label'
data_labels=dataset[labels]
data_features=dataset.drop(columns=['label'])
X=data_features
Y=data_labels
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=0)
logreg = AdaBoostClassifier()
Y_pred=logreg.fit(X_train,Y_train).predict(X_test)
print('Accuracy of AdaBoost classifier on train set :{:.2f}'.format(logreg.score(X_test,Y_test)))
Y_pred=logreg.predict(X_train)
print('Accuracy of AdaBoost classifier on test set :{:.2f}'.format(logreg.score(X_train,Y_train)))