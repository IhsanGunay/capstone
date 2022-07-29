# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
#

# %% [markdown]
# # **Space X  Falcon 9 First Stage Landing Prediction**
#

# %% [markdown]
# ## Assignment:  Machine Learning Prediction
#

# %% [markdown]
# Estimated time needed: **60** minutes
#

# %% [markdown]
# Space X advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against space X for a rocket launch.   In this lab, you will create a machine learning pipeline  to predict if the first stage will land given the data from the preceding labs.
#

# %% [markdown]
# ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/landing\_1.gif)
#

# %% [markdown]
# Several examples of an unsuccessful landing are shown here:
#

# %% [markdown]
# ![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/crash.gif)
#

# %% [markdown]
# Most unsuccessful landings are planed. Space X; performs a controlled landing in the oceans.
#

# %% [markdown]
# ## Objectives
#

# %% [markdown]
# Perform exploratory  Data Analysis and determine Training Labels
#
# *   create a column for the class
# *   Standardize the data
# *   Split into training data and test data
#
# \-Find best Hyperparameter for SVM, Classification Trees and Logistic Regression
#
# *   Find the method performs best using test data
#

# %% [markdown]
#

# %% [markdown]
# ***
#

# %% [markdown]
# ## Import Libraries and Define Auxiliary Functions
#

# %% [markdown]
# We will import the following libraries for the lab
#

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier


# %% [markdown]
# This function is to plot the confusion matrix.
#

# %%
def plot_confusion_matrix(y, y_predict):
    "this function plots the confusion matrix"
    from sklearn.metrics import confusion_matrix

    cm = confusion_matrix(y, y_predict)
    ax = plt.subplot()
    sns.heatmap(cm, annot=True, ax=ax)
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title('Confusion Matrix')
    ax.xaxis.set_ticklabels(['did not land', 'land'])
    ax.yaxis.set_ticklabels(['did not land', 'landed'])


# %% [markdown]
# ## Load the dataframe
#

# %% [markdown]
# Load the data
#

# %%
data = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")  # noqa: E501

data.head()

# %%
X = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_3.csv')  # noqa: E501

X.head()

# %% [markdown]
# ## TASK  1
#

# %% [markdown]
# Create a NumPy array from the column <code>Class</code> in <code>data</code>, by applying the method <code>to_numpy()</code>  then
# assign it  to the variable <code>Y</code>,make sure the output is a  Pandas series (only one bracket df\['name of  column']).
#

# %%
y = data['Class'].to_numpy()

# %% [markdown]
# ## TASK  2
#

# %% [markdown]
# Standardize the data in <code>X</code> then reassign it to the variable  <code>X</code> using the transform provided below.
#

# %%
X = StandardScaler().fit_transform(X)

# %% [markdown]
# We split the data into training and testing data using the  function  <code>train_test_split</code>.   The training data is divided into validation data, a second set used for training  data; then the models are trained and hyperparameters are selected using the function <code>GridSearchCV</code>.
#

# %% [markdown]
# ## TASK  3
#

# %% [markdown]
# Use the function train_test_split to split the data X and Y into training and test data. Set the parameter test_size to  0.2 and random_state to 2. The training data and test data should be assigned to the following labels.
#

# %% [markdown]
# <code>X_train, X_test, Y_train, Y_test</code>
#

# %%
X_train, X_test, Y_train, Y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=2)

# %% [markdown]
# we can see we only have 18 test samples.
#

# %%
Y_test.shape

# %% [markdown]
# ## TASK  4
#

# %% [markdown]
# Create a logistic regression object  then create a  GridSearchCV object  <code>logreg_cv</code> with cv = 10.  Fit the object to find the best parameters from the dictionary <code>parameters</code>.
#

# %%
parameters = {'C': [0.01, 0.1, 1],
              'penalty': ['l2'],
              'solver': ['lbfgs']}

lr = LogisticRegression()
logreg_cv = GridSearchCV(lr, parameters).fit(X_train, Y_train)

# %% [markdown]
# We output the <code>GridSearchCV</code> object for logistic regression. We display the best parameters using the data attribute <code>best_params\_</code> and the accuracy on the validation data using the data attribute <code>best_score\_</code>.
#

# %%
print("tuned hpyerparameters :(best parameters) ", logreg_cv.best_params_)
print("accuracy :", logreg_cv.best_score_)

# %% [markdown]
# ## TASK  5
#

# %% [markdown]
# Calculate the accuracy on the test data using the method <code>score</code>:
#

# %%
logreg_cv.score(X_test, Y_test)

# %% [markdown]
# Lets look at the confusion matrix:
#

# %%
yhat = logreg_cv.predict(X_test)
plot_confusion_matrix(Y_test, yhat)

# %% [markdown]
# Examining the confusion matrix, we see that logistic regression can distinguish between the different classes.  We see that the major problem is false positives.
#

# %% [markdown]
# ## TASK  6
#

# %% [markdown]
# Create a support vector machine object then  create a  <code>GridSearchCV</code> object  <code>svm_cv</code> with cv - 10.  Fit the object to find the best parameters from the dictionary <code>parameters</code>.
#

# %%
parameters = {'kernel': ('linear', 'rbf', 'poly', 'rbf', 'sigmoid'),
              'C': np.logspace(-3, 3, 5),
              'gamma': np.logspace(-3, 3, 5)}
svm = SVC()

# %%
svm_cv = GridSearchCV(svm, parameters).fit(X_train, Y_train)

# %%
print("tuned hpyerparameters :(best parameters) ", svm_cv.best_params_)
print("accuracy :", svm_cv.best_score_)

# %% [markdown]
# ## TASK  7
#

# %% [markdown]
# Calculate the accuracy on the test data using the method <code>score</code>:
#

# %%
svm_cv.score(X_test, Y_test)

# %% [markdown]
# We can plot the confusion matrix
#

# %%
yhat = svm_cv.predict(X_test)
plot_confusion_matrix(Y_test, yhat)

# %% [markdown]
# ## TASK  8
#

# %% [markdown]
# Create a decision tree classifier object then  create a  <code>GridSearchCV</code> object  <code>tree_cv</code> with cv = 10.  Fit the object to find the best parameters from the dictionary <code>parameters</code>.
#

# %%
parameters = {'criterion': ['gini', 'entropy'],
              'splitter': ['best', 'random'],
              'max_depth': [2*n for n in range(1, 10)],
              'min_samples_leaf': [1, 2, 4],
              'min_samples_split': [2, 5, 10]}

tree = DecisionTreeClassifier()

# %%
tree_cv = GridSearchCV(tree, parameters).fit(X_train, Y_train)

# %%
print("tuned hpyerparameters :(best parameters) ", tree_cv.best_params_)
print("accuracy :", tree_cv.best_score_)

# %% [markdown]
# ## TASK  9
#

# %% [markdown]
# Calculate the accuracy of tree_cv on the test data using the method <code>score</code>:
#

# %%
tree_cv.score(X_test, Y_test)

# %% [markdown]
# We can plot the confusion matrix
#

# %%
yhat = tree_cv.predict(X_test)
plot_confusion_matrix(Y_test, yhat)

# %% [markdown]
# ## TASK  10
#

# %% [markdown]
# Create a k nearest neighbors object then  create a  <code>GridSearchCV</code> object  <code>knn_cv</code> with cv = 10.  Fit the object to find the best parameters from the dictionary <code>parameters</code>.
#

# %%
parameters = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
              'p': [1, 2]}

knn = KNeighborsClassifier()

# %%
knn_cv = GridSearchCV(knn, parameters).fit(X_train, Y_train)


# %%
print("tuned hpyerparameters :(best parameters) ", knn_cv.best_params_)
print("accuracy :", knn_cv.best_score_)

# %% [markdown]
# ## TASK  11
#

# %% [markdown]
# Calculate the accuracy of tree_cv on the test data using the method <code>score</code>:
#

# %%
knn_cv.score(X_test, Y_test)

# %% [markdown]
# We can plot the confusion matrix
#

# %%
yhat = knn_cv.predict(X_test)
plot_confusion_matrix(Y_test, yhat)

# %% [markdown]
# ## TASK  12
#

# %% [markdown]
# Find the method performs best:
#

# %%
import matplotlib.pyplot as plot

plot.bar(['Logistic Regression',
          'SVM',
          'Decision Tree',
          'KNeighbors'],
        [logreg_cv.score(X_test, Y_test),
          svm_cv.score(X_test, Y_test),
          tree_cv.score(X_test, Y_test),
          knn_cv.score(X_test, Y_test)])

plot.show()

# %% [markdown]
# ## Authors
#

# %% [markdown]
# <a href="https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
#

# %% [markdown]
# ## Change Log
#

# %% [markdown]
# | Date (YYYY-MM-DD) | Version | Changed By    | Change Description      |
# | ----------------- | ------- | ------------- | ----------------------- |
# | 2021-08-31        | 1.1     | Lakshmi Holla | Modified markdown       |
# | 2020-09-20        | 1.0     | Joseph        | Modified Multiple Areas |
#

# %% [markdown]
# Copyright © 2020 IBM Corporation. All rights reserved.
#
