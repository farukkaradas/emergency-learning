# emergency-learning

Emergency-911 Calls dataset taken from kaggle database. You can use this link to download the database

https://www.kaggle.com/mchirico/montcoalert

Given a new location (latitude-longitude pair), calculated the probability of the occurrence of a specific type of emergency (e.g. VEHICLE ACCIDENT). 
Calculations made for all the emergency types. As a result, prepare a descriptive summary for the new location with respect to the probability of emergency types. Please be reminded that types of emergency can be found in title feature. 

### Problem Description and Data analysis:
Emergency (911) Calls: Fire, Traffic, EMS for Montgomery County, PA.  
“911.csv” data includes columns; **lat**: Latitude, **lng**: Longitude, **desc**: Description of Emergency, **zip**: ZIP Code, **title**: Title of Emergency, **timestamp**:  Date and time of the call, **twp**: Town, **addr**: Address

  - Data includes 423909 different cases

  - Data includes 141 discrete titles like; 
    EMS: ABDOMINAL PAINS, EMS: ACTIVE SHOOTER, EMS: ALLERGIC REACTION…

  - Data includes 22753 discrete locations like;
   (39.9549715, -75.2580431), (39.9553309, -75.1567877), (39.9564971, -75.2480644)…

The most common call titles can be find on "a" array in Method_1 and Method_2

Addresses and reasons for receiving 911 calls most frequently; (in code, array b)

As you can see in b array , there are a lot of traffic accidents to certain addresses. In these locations we have identified, we can associate a lot of traffic accidents with incorrect engineering. Identify locations like this and help solve the problem in these regions.



### Base Methods:
After the preliminary analysis of the data, I followed two different methods; these methods are to write a program that I can use Naive Bayes and to use the ready codes in the **“Sklearn library”**. You can see these methods as **“Method_1” and “Method_2”**. In the Method_1 method, I aimed to calculate the possibilities of each situation using Naive Bayes method. There were problems that I encountered when I applied “Naive Bayes” method separately for each street. One of these problems is that there are only very few calls in some streets in train data. This reduces predictability on the streets. The second problem I have encountered is that some of the call heads are very few in the entire data set. This problem reduces the predictability of these titles.
  - Method_1: Accuracy= 19.424227. 

At Method_1, you can reach the probability values of all events on all streets

In Method_2, I used the “**Bernoulli Naive Bayes Classifier**” and “**Decision Tree Classifier**” I added from Sklearn, but the Accuracy values I had were quite small.
 
  - Method_2: **BernoulliNB Classifier accuracy**= 23.0421, **Decision Tree Classifier accuracy**= 28.311946

BernoulliNB makes all the predictions as vehicle accidents. This can be attributed to the fact that there is a 23% chance of an accident. As can be seen, the Bernoulli method for this example is unusable. In contrast to Bernoulli, Decision Tree classifier gives more accurate estimates of higher accuracy.
### Methods for Increasing accuracy:
I used three methods to increase accuracy. The first is to separate the classes that are less than the threshold value that I set. With this method, I have removed the titles that are difficult to predict in the data. After this method Accuracy increased quite small in Method_2. The second was to delete the prefixes such as **"Fire, Traffic, EMS"** in the Data headers. I've combined multiple calls to multiple departments with this method. As shown below, after this method Accuracy changed.

 - Method_1: Accuracy= 21.77, 
 - Method_2: **BernoulliNB Classifier accuracy**= 23.0421, **Decision Tree Classifier accuracy**= 28.311946

The third method was to delete out layer of dataset. We will achieve more accurate results by eliminating incorrect entries with this method

### Results and Discussion
Final accuracy score was as shown below
  - Method_1: Accuracy= 22.87,
  - Method_2: **BernoulliNB accuracy**  = 28.991736, **Decision Tree accuracy**= 32.462810

Due to the deviation of the data set, a low accuracy value was obtained. Since both streets are not actually a pattern, I couldn't reach the accuracy I want but I applied a few methods to increase this accuracy. Some of them were successful and some failed. For a more specific question it is possible to find meaningful things in this data.
