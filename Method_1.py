"""
Created on Mon May  6 17:44:33 2019
METHOD 1
@author: Ömer Faruk KARADAŞ

"""
import pandas as pd
from sklearn.model_selection import train_test_split

# This function find unique label from titles
def label(data):
    labell = []
    for i in range(len(data)):
        if (data[i] not in labell):
            labell.append(data[i])
    return sorted(labell)

"""
    IMPORTING DATA AND DIVIDING INTO TEST(%5) AND TRAIN DATA SETS
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
data = data.iloc[:, [0, 1, 4]]
train, test = train_test_split(data, test_size=0.05, random_state=1)

# Finding basic groupping information
sp = sorted(pd.unique(data.title))
# sp = label(data.title) # This gives all discrete titles
a = train.groupby('title').size()  # This count all titles
# Class prior for each titles
P_a = train.groupby('title').size().div(len(train))
b = train.groupby(['lat', 'lng', 'title'])['lat'].size()
# This counts discrete things happened in a unique street
c = train.groupby(['lat', 'lng'])['title'].size()

P_b = []
# This list will be used for probobality of case in c series
P_c = []
# This list will be used for probability of maximum case  in discrete streets
"""
    BAYES THEORY

    P(x,y|Ci)=P(Ci|x,y)*P(x,y)/( P(C0|x,y)*P(x,y)+P())
"""

j = 0
for i in range(len(c)-1):  # Probabilty of every stress
    local_sum = 0
    k = j
    while(c.index[i][0] == b.index[j][0] and c.index[i][1] == b.index[j][1]):
        local_sum = local_sum + (b.iat[j] / c.iat[i] * P_a[sp.index(b.index[j][2])])
        # Program will calculate sum of probability of every cases:Sum=evidence
        j = j+1
    while(c.index[i][0] == b.index[k][0] and c.index[i][1] == b.index[k][1]):
        P_b.append((b.iat[k] / c.iat[i] * P_a[sp.index(b.index[k][2])]) / local_sum)
        k = k+1
        # Probobality of discrete cases in a unique streets
"""
    Until this line, Algorithm has calculated the
    probability of every cases in every streets in TrainData
"""

P_all = pd.DataFrame([b.index, P_b]).transpose()
# All streets, all anonunses and all probobilities
"""
    A few example from Algoritm gives us probability of discrete cases
"""

print("probability of %s = %lf" % (P_all[0][15], 100*P_all[1][15]))
print("probability of %s = %lf" % (P_all[0][16], 100*P_all[1][16]))
print("probability of %s = %lf" % (P_all[0][17], 100*P_all[1][17]))

P_c = pd.DataFrame([b.index, P_b]).transpose()
count = 0
P_max = []
P_maxvalue = []
j = 0
for i in range(len(c)-1):  # probabilty of every stress
    maxx = 0
    while(c.index[i][0] == b.index[j][0] and c.index[i][1] == b.index[j][1]):
        if(P_b[j] > maxx):
            maxx = P_b[j]
            k = j
        j = j+1
    P_max.append(b.index[k][2])
    P_maxvalue.append(maxx)
P_c = pd.DataFrame([c.index, P_max, P_maxvalue]).transpose()
# P_c gives us maximun probability and case in a unique street
"""
    TEST DATA AND ACCURACY
"""
count = 0
# Test data discrete Streets
Tb = test.groupby(['lat', 'lng', 'title'])['lat'].size()
for i in range(len(Tb)):
    x = []
    x.extend(P_c[P_c[0] == (Tb.index[i][0], Tb.index[i][1])][1])
    if(x != []):
        if(Tb.index[i][2] == x[0]):
            count = count+1
            # Testing Truth of labeling

ac = count/i
print("accuracy = %f" % (100*ac))
# Accuracy

j = 0
for i in range(len(c)-1):  # Probabilty of every stress
    local_sum = 0
    k = j
    while(c.index[i][0] == b.index[j][0] and c.index[i][1] == b.index[j][1]):
        local_sum = local_sum + (b.iat[j] / c.iat[i] * P_a[sp.index(b.index[j][2])])
        # Program will calculate sum of probability of every cases:Sum=evidence
        j = j+1
    while(c.index[i][0] == b.index[k][0] and c.index[i][1] == b.index[k][1]):
        P_b.append((b.iat[k] / c.iat[i] * P_a[sp.index(b.index[k][2])]) / local_sum)
        k = k+1
        # Probobality of discrete cases in a unique streets
"""
    Until this line, Algorithm has calculated the
    probability of every cases in every streets in TrainData
"""

P_all = pd.DataFrame([b.index, P_b]).transpose()
# All streets, all anonunses and all probobilities
"""
    A few example from Algoritm gives us probability of discrete cases
"""

print("probability of %s = %lf" % (P_all[0][15], 100*P_all[1][15]))
print("probability of %s = %lf" % (P_all[0][16], 100*P_all[1][16]))
print("probability of %s = %lf" % (P_all[0][17], 100*P_all[1][17]))

P_c = pd.DataFrame([b.index, P_b]).transpose()
count = 0
P_max = []
P_maxvalue = []
j = 0
for i in range(len(c)-1):  # probabilty of every stress
    maxx = 0
    while(c.index[i][0] == b.index[j][0] and c.index[i][1] == b.index[j][1]):
        if(P_b[j] > maxx):
            maxx = P_b[j]
            k = j
        j = j+1
    P_max.append(b.index[k][2])
    P_maxvalue.append(maxx)
P_c = pd.DataFrame([c.index, P_max, P_maxvalue]).transpose()
# P_c gives us maximun probability and case in a unique street
"""
    TEST DATA AND ACCURACY
"""
count = 0
# Test data discrete Streets
Tb = test.groupby(['lat', 'lng', 'title'])['lat'].size()
for i in range(len(Tb)):
    x = []
    x.extend(P_c[P_c[0] == (Tb.index[i][0], Tb.index[i][1])][1])
    if(x != []):
        if(Tb.index[i][2] == x[0]):
            count = count+1
            # Testing Truth of labeling

ac = count/i
print("accuracy = %f" % (100*ac))
# Accuracy
