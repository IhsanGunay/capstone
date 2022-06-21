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
# <img src = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%201/images/IDSNlogo.png" width = 400>
#
# # From Problem to Approach
#
# Estimated time needed: **20** minutes
#
# ## Objectives
#
# After completing this lab you will be able to:
#
# -   Have a Business Understanding of case studies
# -   Analytically approach problems
#

# %% [markdown]
# ## Table of Contents
#
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#
# 1.  [Business Understanding](#0)<br>
# 2.  [Analytic Approach](#2) <br>
#     </div>
#     <hr>
#

# %% [markdown]
# # Business Understanding <a id="0"></a>
#

# %% [markdown]
# This is the **Data Science Methodology**, a flowchart that begins with business understanding.
#

# %% [markdown]
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%201/images/lab1_fig1_flowchart_business_understanding.png" width=500>
#

# %% [markdown]
# #### Why is the business understanding stage important?
#

# %% [raw]
# Your Answer: 
#
#

# %% [markdown]
# <details><summary>Click here for the solution</summary>
#
# ```python
#     #The correct answer is:
#     It helps clarify the goal of the entity asking the question.
# ```
#
# </details>
#

# %% [markdown]
# #### Looking at this diagram, we immediately spot two outstanding features of the data science methodology.
#

# %% [markdown]
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%201/images/lab1_fig2_datascience_methodology_flowchart.png" width = 500> 
#

# %% [markdown]
# #### What are they?
#

# %% [raw]
# Your Answer: 
# 1.
# 2.

# %% [markdown]
# <details><summary>Click here for the solution</summary>
#
# ```python
#     #The correct answer is:
#     # 1. The flowchart is highly iterative.
#     #2. The flowchart never ends. 
# ```
#
# </details>
#

# %% [markdown]
# #### Now let's illustrate the data science methodology with a case study.
#

# %% [markdown]
# Say, we are interested in automating the process of figuring out the cuisine of a given dish or recipe. Let's apply the business understanding stage to this problem.
#

# %% [markdown]
# #### Q. Can we predict the cuisine of a given dish using the name of the dish only?
#

# %% [raw]
# Your Answer:
#
#

# %% [markdown]
# <details><summary>Click here for the solution</summary>
#
# ```python
#     #The correct answer is:
#     No.
# ```
#
# </details>
#

# %% [markdown]
# #### Q. For example, the following dish names were taken from the menu of a local restaurant in Toronto, Ontario in Canada.
#
# #### 1. Beast
#
# #### 2. 2 PM
#
# #### 3. 4 Minute
#

# %% [markdown]
# #### Are you able to tell the cuisine of these dishes?
#

# %% [raw]
# Your Answer:
#
#

# %% [markdown]
# <details><summary>Click here for the solution</summary>
#
# ```python
#     #The correct answer is:
#     The cuisine is <strong>Japanese</strong>. Here are links to the images of the dishes: 
#   
#     Beast: https://ibm.box.com/shared/static/5e7duvewfl5bk4317sna5skvdhrehro2.png
#             
#     2PM: https://ibm.box.com/shared/static/d9xuzqm8cq76zxxcc0f9gdts4iksipyk.png
#     
#     4 Minute: https://ibm.box.com/shared/static/f1fwvvwn4u8rx8tghep6zyj5pi6a8v8k.png
#
#             Photographs by Avlxyz: https://commons.wikimedia.org/wiki/Category:Photographs_by_Avlxyz
#                         
# ```
#
# </details>
#

# %% [markdown]
# #### Q. What about by appearance only? Yes or No.
#

# %% [raw]
# Your Answer:
#
#

# %% [markdown]
# <details><summary>Click here for the solution</summary>
#
# ```python
#     #The correct answer is:
#     No, especially when it comes to countries in close geographical proximity such as Scandinavian countries, or Asian countries.
#     
# ```
#
# </details>
#

# %% [markdown]
# At this point, we realize that automating the process of determining the cuisine of a given dish is not a straightforward problem as we need to come up with a way that is very robust to the many cuisines and their variations.
#

# %% [markdown]
# #### Q. What about determining the cuisine of a dish based on its ingredients?
#

# %% [raw]
# Your Answer:
#
#

# %% [markdown]
# <details><summary>Click here for the solution</summary>
#
# ```python
#     #The correct answer is:
#     Potentially yes, as there are specific ingredients unique to each cuisine.
#
# ```
#
# </details>
#

# %% [markdown]
# As you guessed, yes determining the cuisine of a given dish based on its ingredients seems like a viable solution as some ingredients are unique to cuisines. For example:
#

# %% [markdown]
# -   When we talk about **American** cuisines, the first ingredient that comes to one's mind (or at least to my mind =D) is beef or turkey.
#
# -   When we talk about **British** cuisines, the first ingredient that comes to one's mind is haddock or mint sauce.
#
# -   When we talk about **Canadian** cuisines, the first ingredient that comes to one's mind is bacon or poutine.
#
# -   When we talk about **French** cuisines, the first ingredient that comes to one's mind is bread or butter.
#
# -   When we talk about **Italian** cuisines, the first ingredient that comes to one's mind is tomato or ricotta.
#
# -   When we talk about **Japanese** cuisines, the first ingredient that comes to one's mind is seaweed or soy sauce.
#
# -   When we talk about **Chinese** cuisines, the first ingredient that comes to one's mind is ginger or garlic.
#
# -   When we talk about **indian** cuisines, the first ingredient that comes to one's mind is masala or chillis.
#

# %% [markdown]
# #### Accordingly, can you determine the cuisine of the dish associated with the following list of ingredients?
#

# %% [markdown]
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%201/lab1_fig3_ingredients.png" width=600>
#

# %% [raw]
# Your Answer:
#
#

# %% [markdown]
# <details><summary>Click here for the solution</summary>
#
# ```python
#     #The correct answer is:
#     Japanese since the recipe is most likely that of a sushi roll.
#
# ```
#
# </details>
#

# %% [markdown]
# # Analytic Approach <a id="2"></a>
#

# %% [markdown]
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%201/images/lab1_fig4_flowchart_analytic_approach.png" width=500>
#

# %% [markdown]
# #### So why are we interested in data science?
#

# %% [markdown]
# Once the business problem has been clearly stated, the data scientist can define the analytic approach to solve the problem. This step entails expressing the problem in the context of statistical and machine-learning techniques, so that the entity or stakeholders with the problem can identify the most suitable techniques for the desired outcome. 
#

# %% [markdown]
# #### Why is the analytic approach stage important?
#

# %% [raw]
# Your Answer:
#
#

# %% [markdown]
# <details><summary>Click here for the solution</summary>
#
# ```python
#     #The correct answer is:
#     Because it helps identify what type of patterns will be needed to address the question most effectively.
#
# ```
#
# </details>
#

# %% [markdown]
# #### Let's explore a machine learning algorithm, decision trees, and see if it is the right technique to automate the process of identifying the cuisine of a given dish or recipe while simultaneously providing us with some insight on why a given recipe is believed to belong to a certain type of cuisine.
#

# %% [markdown]
# This is a decision tree that a naive person might create manually. Starting at the top with all the recipes for all the cuisines in the world, if a recipe contains **rice**, then this decision tree would classify it as a **Japanese** cuisine. Otherwise, it would be classified as not a **Japanese** cuisine.
#

# %% [markdown]
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%201/images/lab1_fig5_decision_tree_3.png" width=500>
#

# %% [markdown]
# #### Is this a good decision tree?  Yes or  No, and why?
#

# %% [raw]
# Your Answer:
#
#

# %% [markdown]
# <details><summary>Click here for the solution</summary>
#
# ```python
#     #The correct answer is:
#     No, because a plethora of dishes from other cuisines contain rice. Therefore, using rice as the ingredient in the Decision node to split on is not a good choice.
#     
# ```
#
# </details>
#

# %% [markdown]
# #### In order to build a very powerful decision tree for the recipe case study, let's take some time to learn more about decision trees.
#

# %% [markdown]
# -   Decision trees are built using recursive partitioning to classify the data.
# -   When partitioning the data, decision trees use the most predictive feature (ingredient in this case) to split the data.
# -   **Predictiveness** is based on decrease in entropy - gain in information, or _impurity_.
#

# %% [markdown]
# #### Suppose that our data is comprised of green triangles and red circles.
#

# %% [markdown]
# The following decision tree would be considered the optimal model for classifying the data into a node for green triangles and a node for red circles.
#

# %% [markdown]
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%201/images/lab1_fig6_decision_tree_5.png" width=400>
#

# %% [markdown]
# Each of the classes in the leaf nodes are completely pure – that is, each leaf node only contains datapoints that belong to the same class.
#

# %% [markdown]
# On the other hand, the following decision tree is an example of the worst-case scenario that the model could output. 
#

# %% [markdown]
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%201/images/lab1_fig7_decision_tree_2.png" width=500>
#

# %% [markdown]
# Each leaf node contains datapoints belonging to the two classes resulting in many datapoints ultimately being misclassified.
#

# %% [markdown]
# #### A tree stops growing at a node when:
#
# -   Pure or nearly pure.
# -   No remaining variables on which to further subset the data.
# -   The tree has grown to a preselected size limit.
#

# %% [markdown]
# #### Here are some characteristics of decision trees:
#

# %% [markdown]
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%201/images/lab1_fig8_decision_trees_table.png" width=800>
#

# %% [markdown]
# Now let's put what we learned about decision trees to use. Let's try and build a much better version of the decision tree for our recipe problem.
#

# %% [markdown]
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%201/images/lab1_fig9_decision_tree_4.png" width = 500>
#

# %% [markdown]
# I hope you agree that the above decision tree is a much better version than the previous one. Although we are still using **Rice** as the ingredient in the first _decision node_, recipes get divided into **Asian Food** and **Non-Asian Food**. **Asian Food** is then further divided into **Japanese** and **Not Japanese** based on the **Wasabi** ingredient. This process of splitting _leaf nodes_ continues until each _leaf node_ is pure, i.e., containing recipes belonging to only one cuisine.
#

# %% [markdown]
# Accordingly, decision trees is a suitable technique or algorithm for our recipe case study.
#

# %% [markdown]
# ### Thank you for completing this lab!
#
# This notebook was created by Alex Aklson. I hope you found this lab session interesting. Feel free to contact me if you have any questions!
#

# %% [markdown]
# This notebook is part of a course called _The Data Science Method_. If you accessed this notebook outside the course, you can take this course, online by clicking [here](https://cocl.us/DS0103EN-Exercise-From-Problem-to-Approach).
#

# %% [markdown]
# ## Author
#
# <a href="https://www.linkedin.com/in/joseph-s-50398b136/" target="_blank">Joseph Santarcangelo</a>
#
# ## Change Log
#
# | Date (YYYY-MM-DD) | Version | Changed By | Change Description                 |
# | ----------------- | ------- | ---------- | ---------------------------------- |
# | 2020-09-25        | 2.1     | Lakshmi    | Fixed Typo errors                  |
# | 2020-08-27        | 2.0     | Lavanya    | Moved lab to course repo in GitLab |
#
# <hr>
#
# ## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
#
