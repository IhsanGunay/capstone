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
# <h1 align=center><font size = 5>Assignment: SQL Notebook for Peer Assignment</font></h1>
#
# Estimated time needed: **60** minutes.
#
# ## Introduction
#
# Using this Python notebook you will:
#
# 1.  Understand the Spacex DataSet
# 2.  Load the dataset  into the corresponding table in a Db2 database
# 3.  Execute SQL queries to answer assignment questions
#

# %% [markdown]
# ## Overview of the DataSet
#
# SpaceX has gained worldwide attention for a series of historic milestones.
#
# It is the only private company ever to return a spacecraft from low-earth orbit, which it first accomplished in December 2010.
# SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars wheras other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage.
#
# Therefore if we can determine if the first stage will land, we can determine the cost of a launch.
#
# This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.
#
# This dataset includes a record for each payload carried during a SpaceX mission into outer space.
#

# %% [markdown]
# ### Connect to the database
#
# Let us first load the SQL extension and establish a connection with the database
#

# %%
# %load_ext sql

# %%
# %config SqlMagic.autopandas = True
# %config SqlMagic.feedback = False
# %config SqlMagic.displaycon = False

# %%
# %sql duckdb:///:memory:

# %%
import pandas as pd
import duckdb

c = duckdb.connect()

# %%
data = pd.read_csv('Spacex.csv', parse_dates=['Date'])

# %%
data = data.rename(columns={"Landing _Outcome":"Landing_Outcome"})

# %% [markdown]
# ## Tasks
#
# Now write and execute SQL queries to solve the assignment tasks.
#
# ### Task 1
#
# ##### Display the names of the unique launch sites  in the space mission
#

# %% language="sql"
# SELECT * 
# FROM data
# LIMIT 7

# %% language="sql"
# SELECT Launch_site
# from data
# group by launch_site

# %% [markdown]
# ### Task 2
#
# ##### Display 5 records where launch sites begin with the string 'CCA'
#

# %% language="sql"
# select * 
# from data
# where launch_site LIKE 'CCA%'
# limit 5

# %% [markdown]
# ### Task 3
#
# ##### Display the total payload mass carried by boosters launched by NASA (CRS)
#

# %% language="sql"
# select sum(PAYLOAD_MASS__KG_)
# from data
# where customer like '%NASA%'

# %% [markdown]
# ### Task 4
#
# ##### Display average payload mass carried by booster version F9 v1.1
#

# %% language="sql"
# select avg(payload_mass__kg_)
# from data
# where booster_version like 'F9 v1.1%'

# %% [markdown]
# ### Task 5
#
# ##### List the date when the first successful landing outcome in ground pad was acheived.
#
# *Hint:Use min function*
#

# %% language="sql"
# SELECT date
# from data
# where landing_outcome like 'Success%'
# limit 1

# %% [markdown]
# ### Task 6
#
# ##### List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000
#

# %% language="sql"
# SELECT booster_version, payload_mass__kg_, landing_outcome
# from data
# where landing_outcome like 'Success (drone ship)'
#     and payload_mass__kg_ > 4000
#     and payload_mass__kg_ < 6000

# %% [markdown]
# ### Task 7
#
# ##### List the total number of successful and failure mission outcomes
#

# %% language="sql"
# select count(*), landing_outcome
# from data
# group by landing_outcome

# %% [markdown]
# ### Task 8
#
# ##### List the   names of the booster_versions which have carried the maximum payload mass. Use a subquery
#

# %% language="sql"
# select booster_version
# from data
# where payload_mass__kg_ = (select max(payload_mass__kg_)
#                            from data)

# %% [markdown]
# ### Task 9
#
# ##### List the failed landing_outcomes in drone ship, their booster versions, and launch site names for in year 2015
#

# %% language="sql"
# SELECT booster_version, launch_site, landing_outcome, date
# from data
# where landing_outcome like 'Failure (drone ship)'

# %% [markdown]
# ### Task 10
#
# ##### Rank the count of landing outcomes (such as Failure (drone ship) or Success (ground pad)) between the date 2010-06-04 and 2017-03-20, in descending order
#

# %% language="sql"
# select count(*), landing_outcome
# from data
# where date > '2010-06-04'
# and date < '2017-03-20'
# group by landing_outcome

# %% [markdown]
# ### Reference Links
#
# *   <a href ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20String%20Patterns%20-%20Sorting%20-%20Grouping/instructional-labs.md.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01&origin=www.coursera.org">Hands-on Lab : String Patterns, Sorting and Grouping</a>
#
# *   <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Built-in%20functions%20/Hands-on_Lab__Built-in_Functions.md.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01&origin=www.coursera.org">Hands-on Lab: Built-in functions</a>
#
# *   <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sub-queries%20and%20Nested%20SELECTs%20/instructional-labs.md.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01&origin=www.coursera.org">Hands-on Lab : Sub-queries and Nested SELECT Statements</a>
#
# *   <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-3-SQLmagic.ipynb?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01">Hands-on Tutorial: Accessing Databases with SQL magic</a>
#
# *   <a href= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-4-Analyzing.ipynb?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01">Hands-on Lab: Analyzing a real World Data Set</a>
#

# %% [markdown]
# ## Author(s)
#
# <h4> Lakshmi Holla </h4>
#

# %% [markdown]
# ## Other Contributors
#
# <h4> Rav Ahuja </h4>
#

# %% [markdown]
# ## Change log
#
# | Date       | Version | Changed by    | Change Description        |
# | ---------- | ------- | ------------- | ------------------------- |
# | 2021-10-12 | 0.4     | Lakshmi Holla | Changed markdown          |
# | 2021-08-24 | 0.3     | Lakshmi Holla | Added library update      |
# | 2021-07-09 | 0.2     | Lakshmi Holla | Changes made in magic sql |
# | 2021-05-20 | 0.1     | Lakshmi Holla | Created Initial Version   |
#

# %% [markdown]
# ## <h3 align="center"> © IBM Corporation 2021. All rights reserved. <h3/>
#
