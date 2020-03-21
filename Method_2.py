"""
Created on Mon May  6 23:00:43 2019
METHOD 2
@author: Faruk
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier

"""
    IMPORTING DATA and SPLITTING DATA
"""
data = pd.read_csv('911.csv')
"""
    Accuracy increasing method 1
"""
# Eliminating the prefix such that Fire,EMS ...
data = data.replace(["Fire: ", "EMS: ", 'Traffic: ', ' -'], '', regex=True)
"""
    Accuracy increasing method 2
"""
# Eliminating the rare case which are happened lower than 100 times


a = data.groupby('title').size()
for i in range(len(a)):
    if(a[i] < 100):
        data = data[data.title != a.index[i]]

"""
    Accuracy increasing method 3
"""
# Eliminating the outlayer boundary of data
data.loc[((data['lat'] < 39.00) | (data['lat'] > 41.00)) &
         ((data['lng'] < -77.00) | (data['lng'] > -74.00))]

"""
    Map of data
"""
plt.scatter(data.lat, data.lng)
plt.show()


X = data.iloc[:, [0, 1]]  # splitting lat and lng columns
y = data.iloc[:, 4]      # splitting title column
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05,
                                                    random_state=42)
"""
    Using Decision Tree classifier
"""

classifier = DecisionTreeClassifier(random_state=1)
classifier.fit(X_train, y_train)
"""
    Making Predictions
"""

y_pred = classifier.predict(X_test)
y_pred = pd.DataFrame(y_pred)
"""
    Creating Confusion matrix and Calculating accuracy
"""

accuracy = accuracy_score(y_test, y_pred)
print("Decision Tree accuracy= %lf" % (100*accuracy))
"""
    Using BernoulliNB classifier
"""

classifier = BernoulliNB()
classifier.fit(X_train, y_train)
"""
    Making Predictions
"""
y_pred = classifier.predict(X_test)
y_pred = pd.DataFrame(y_pred)
"""
    Creating Confusion matrix and Calculating accuracy
"""
confusionmatrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
print("BernoulliNB accuracy  = %lf" % (100*accuracy))
