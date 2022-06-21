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

# %%
# !pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3
# !pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24
# !pip install ipython-sql==0.3.9

# %%
# %load_ext sql

# %%
# %sql ibm_db_sa://qjk12884:{PasswordHere}@ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:31321/bludb?security=SSL

# %%
# %sql SELECT TABSCHEMA, TABNAME, CREATE_TIME FROM SYSCAT.TABLES WHERE TABSCHEMA= 'QJK12884'

# %%
# %sql SELECT COLNAME, TYPENAME, LENGTH FROM SYSCAT.COLUMNS WHERE TABNAME = 'CHICAGO_PUBLIC_SCHOOLS'

# %%
# %sql SELECT COLNAME, TYPENAME, LENGTH FROM SYSCAT.COLUMNS WHERE TABNAME = 'CENSUS_DATA'

# %%
# %sql SELECT COLNAME, TYPENAME, LENGTH FROM SYSCAT.COLUMNS WHERE TABNAME = 'CHICAGO_CRIME_DATA'

# %%
# %sql SELECT DISTINCT(description) FROM CHICAGO_CRIME_DATA

# %% [markdown]
# ## Part 1
#
# ### Problem 1
#
# ##### How many Elementary Schools are in the dataset?

# %%
# %sql SELECT COUNT(*) FROM CHICAGO_PUBLIC_SCHOOLS WHERE "Elementary, Middle, or High School" = 'ES'

# %% [markdown]
# ### Problem 2
#
# ##### What is the highest Safety Score?
#

# %%
# %sql SELECT MAX(SAFETY_SCORE) FROM CHICAGO_PUBLIC_SCHOOLS

# %% [markdown]
# ### Problem 3
#
# ##### Which schools have the highest Safety Score?
#

# %% language="sql"
# SELECT NAME_OF_SCHOOL, SAFETY_SCORE
# FROM CHICAGO_PUBLIC_SCHOOLS
# WHERE SAFETY_SCORE =
#  (SELECT MAX(SAFETY_SCORE) FROM CHICAGO_PUBLIC_SCHOOLS)

# %% [markdown]
# ### Problem 4
#
# ##### What are the top 10 schools with the highest "Average Student Attendance"?

# %% language="sql"
# SELECT NAME_OF_SCHOOL, AVERAGE_STUDENT_ATTENDANCE
# FROM CHICAGO_PUBLIC_SCHOOLS
# ORDER BY AVERAGE_STUDENT_ATTENDANCE
# DESC NULLS LAST LIMIT 10 

# %% [markdown]
# ### Problem 5
#
# ##### Retrieve the list of 5 Schools with the lowest Average Student Attendance sorted in ascending order based on attendance

# %% language="sql"
# SELECT NAME_OF_SCHOOL, AVERAGE_STUDENT_ATTENDANCE
# FROM CHICAGO_PUBLIC_SCHOOLS
# ORDER BY AVERAGE_STUDENT_ATTENDANCE
# LIMIT 5

# %% [markdown]
# ### Problem 6
#
# ##### Now remove the '%' sign from the above result set for Average Student Attendance column
#

# %% language="sql"
# SELECT NAME_OF_SCHOOL, REPLACE(AVERAGE_STUDENT_ATTENDANCE, '%', '')
# FROM CHICAGO_PUBLIC_SCHOOLS
# ORDER BY AVERAGE_STUDENT_ATTENDANCE
# LIMIT 5

# %% [markdown]
# ### Problem 7
#
# ##### Which Schools have Average Student Attendance lower than 70%?

# %% language="sql"
# SELECT NAME_OF_SCHOOL, AVERAGE_STUDENT_ATTENDANCE 
# FROM CHICAGO_PUBLIC_SCHOOLS
# WHERE DECIMAL ( REPLACE(AVERAGE_STUDENT_ATTENDANCE, '%', '') ) < 70
# ORDER BY AVERAGE_STUDENT_ATTENDANCE

# %% [markdown]
# ### Problem 8
#
# ##### Get the total College Enrollment for each Community Area

# %% language="sql"
# SELECT COMMUNITY_AREA_NAME, SUM(COLLEGE_ENROLLMENT) AS TOTAL_ENROLLMENT
# FROM CHICAGO_PUBLIC_SCHOOLS
# GROUP BY COMMUNITY_AREA_NAME 

# %% [markdown]
# ### Problem 9
#
# ##### Get the 5 Community Areas with the least total College Enrollment  sorted in ascending order

# %% language="sql"
# SELECT COMMUNITY_AREA_NAME, SUM(COLLEGE_ENROLLMENT) AS TOTAL_ENROLLMENT
# FROM CHICAGO_PUBLIC_SCHOOLS
# GROUP BY COMMUNITY_AREA_NAME
# ORDER BY TOTAL_ENROLLMENT ASC
# LIMIT 5

# %% [markdown]
# ### Problem 10
#
# ##### List 5 schools with lowest safety score.

# %% language="sql"
# SELECT NAME_OF_SCHOOL, SAFETY_SCORE
# FROM CHICAGO_PUBLIC_SCHOOLS
# ORDER BY SAFETY_SCORE
# LIMIT 5

# %% [markdown]
# ### Problem 11
#
# ##### Get the hardship index for the community area which has College Enrollment of 4368

# %% language="sql"
# SELECT CD.COMMUNITY_AREA_NAME, CD.HARDSHIP_INDEX 
# FROM CENSUS_DATA CD, CHICAGO_PUBLIC_SCHOOLS CPS 
# WHERE CD.COMMUNITY_AREA_NUMBER = CPS.COMMUNITY_AREA_NUMBER
#       AND COLLEGE_ENROLLMENT = 4368

# %% [markdown]
# ### Problem 12
#
# ##### Get the hardship index for the community area which has the school with the  highest enrollment.

# %% language="sql"
# SELECT COMMUNITY_AREA_NAME, HARDSHIP_INDEX
# FROM CENSUS_DATA
# WHERE COMMUNITY_AREA_NUMBER =
#     (SELECT COMMUNITY_AREA_NUMBER
#      FROM CHICAGO_PUBLIC_SCHOOLS 
#      WHERE COLLEGE_ENROLLMENT =
#          (SELECT MAX(COLLEGE_ENROLLMENT) FROM CHICAGO_PUBLIC_SCHOOLS))

# %% [markdown]
# ## Part 2

# %% [markdown]
# ### Problem 1
# ##### Find the total number of crimes recorded in the CRIME table.

# %% language="sql"
# SELECT COUNT(*) AS TOTAL_NUMBER_OF_CRIMES
# FROM CHICAGO_CRIME_DATA

# %% [markdown]
# ### Problem 2
# ##### List community areas with per capita income less than 11000.

# %% language="sql"
# SELECT COMMUNITY_AREA_NAME, PER_CAPITA_INCOME
# FROM CENSUS_DATA
# WHERE PER_CAPITA_INCOME < 11000

# %% [markdown]
# ### Problem 3
# ##### List all case numbers for crimes involving minors?

# %% language="sql"
# SELECT CASE_NUMBER, PRIMARY_TYPE, DESCRIPTION
# FROM CHICAGO_CRIME_DATA
# WHERE DESCRIPTION LIKE '%MINOR%'

# %% [markdown]
# ### Problem 4
# ##### List all kidnapping crimes involving a child?(children are not considered minors for the purposes of crime analysis)

# %% language="sql"
# SELECT CASE_NUMBER, PRIMARY_TYPE, DESCRIPTION
# FROM CHICAGO_CRIME_DATA
# WHERE PRIMARY_TYPE = 'KIDNAPPING'
#     AND DESCRIPTION LIKE '%CHILD%'

# %% [markdown]
# ### Problem 5
# ##### What kind of crimes were recorded at schools?

# %% language="sql"
# SELECT DISTINCT(PRIMARY_TYPE)
# FROM CHICAGO_CRIME_DATA
# WHERE LOCATION_DESCRIPTION LIKE '%SCHOOL%'

# %% [markdown]
# ### Problem 6
# ##### List the average safety score for all types of schools.

# %% language="sql"
# SELECT "Elementary, Middle, or High School", AVG(SAFETY_SCORE) AS AVG_SAFETY_SCORE
# FROM CHICAGO_PUBLIC_SCHOOLS
# GROUP BY "Elementary, Middle, or High School"

# %% [markdown]
# ### Problem 7
# ##### List 5 community areas with highest % of households below poverty line.

# %% language="sql"
# SELECT COMMUNITY_AREA_NAME, PERCENT_HOUSEHOLDS_BELOW_POVERTY
# FROM CENSUS_DATA
# ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC
# LIMIT 5

# %% [markdown]
# ### Problem 8
# ##### Which community area(number) is most crime prone?

# %% language="sql"
# SELECT COMMUNITY_AREA_NUMBER, COUNT(*) AS CRIME_COUNT
# FROM CHICAGO_CRIME_DATA
# GROUP BY COMMUNITY_AREA_NUMBER
# ORDER BY CRIME_COUNT DESC
# LIMIT 1

# %% [markdown]
# ### Problem 9
# ##### Use a sub-query to find the name of the community area with highest hardship index.

# %% language="sql"
# SELECT COMMUNITY_AREA_NAME, HARDSHIP_INDEX
# FROM CENSUS_DATA
# WHERE HARDSHIP_INDEX = (
#     SELECT MAX(HARDSHIP_INDEX)
#     FROM CENSUS_DATA)

# %% [markdown]
# ### Problem 10
# ##### Use a sub-query to determine the Community Area Name with most number of crimes?

# %% language="sql"
# SELECT COMMUNITY_AREA_NAME
# FROM CENSUS_DATA
# WHERE COMMUNITY_AREA_NUMBER = (
#     SELECT COMMUNITY_AREA_NUMBER
#     FROM CHICAGO_CRIME_DATA
#     GROUP BY COMMUNITY_AREA_NUMBER
#     ORDER BY COUNT(*) DESC
#     LIMIT 1)

# %% [markdown]
# ## Part 3
#
# ### Problem 1
#
# #### List the case number, type of crime and community area for all crimes in community area number 18.

# %% language="sql"
# SELECT CASE_NUMBER, PRIMARY_TYPE, COMMUNITY_AREA_NAME
# FROM CHICAGO_CRIME_DATA A
# INNER JOIN CENSUS_DATA B
# ON A.COMMUNITY_AREA_NUMBER = B.COMMUNITY_AREA_NUMBER
# WHERE A.COMMUNITY_AREA_NUMBER = 18

# %% [markdown]
# ### Problem 2
#
# #### List all crimes that took place at a school. Include case number, crime type and community name.

# %% language="sql"
# SELECT CASE_NUMBER, PRIMARY_TYPE, COMMUNITY_AREA_NAME
# FROM CHICAGO_CRIME_DATA A
# LEFT OUTER JOIN CENSUS_DATA B
# ON A.COMMUNITY_AREA_NUMBER = B.COMMUNITY_AREA_NUMBER
# WHERE A.LOCATION_DESCRIPTION LIKE '%SCHOOL%'

# %% [markdown]
# ### Problem 3
#
# #### For the communities of Oakland, Armour Square, Edgewater and CHICAGO list the associated community_area_numbers and the case_numbers.

# %% language="sql"
# SELECT COMMUNITY_AREA_NAME, B.COMMUNITY_AREA_NUMBER, CASE_NUMBER
# FROM CHICAGO_CRIME_DATA A
# FULL OUTER JOIN CENSUS_DATA B
# ON A.COMMUNITY_AREA_NUMBER = B.COMMUNITY_AREA_NUMBER
# WHERE B.COMMUNITY_AREA_NAME IN ('Oakland', 'Armour Square', 'Edgewater', 'CHICAGO')

# %% [markdown]
# ## Part 4
#
# ### Problem 1
#
# #### Write and execute a SQL query to list the school names, community names and average attendance for communities with a hardship index of 98.
#

# %% language="sql"
# SELECT NAME_OF_SCHOOL, A.COMMUNITY_AREA_NAME, AVERAGE_STUDENT_ATTENDANCE
# FROM CHICAGO_PUBLIC_SCHOOLS A
# LEFT OUTER JOIN CENSUS_DATA B
# ON A.COMMUNITY_AREA_NUMBER = B.COMMUNITY_AREA_NUMBER
# WHERE B.HARDSHIP_INDEX = 98

# %% [markdown]
# ### Problem 2
#
# #### Write and execute a SQL query to list all crimes that took place at a school. Include case number, crime type and community name.
#

# %% language="sql"
# SELECT CASE_NUMBER, PRIMARY_TYPE, COMMUNITY_AREA_NAME
# FROM CHICAGO_CRIME_DATA A
# LEFT OUTER JOIN CENSUS_DATA B
# ON A.COMMUNITY_AREA_NUMBER = B.COMMUNITY_AREA_NUMBER
# WHERE A.LOCATION_DESCRIPTION LIKE '%SCHOOL%'

# %% [markdown]
# ### Problem 3
#
# #### Write and execute a SQL statement to create a view showing the columns listed in the following table, with new column names as shown in the second column.
# | Column name in CHICAGO_PUBLIC_SCHOOLS | Column name in view |
#
# |-------------------------|-------------------------|
#
# | NAME_OF_SCHOOL | School_Name |
#
# | Safety_Icon |	Safety_Rating |
#
# | Family_Involvement_Icon |	Family_Rating |
#
# | Environment_Icon |	Environment_Rating |
#
# | Instruction_Icon |	Instruction_Rating |
#
# | Leaders_Icon |	Leaders_Rating |
#
# | Teachers_Icon |	Teachers_Rating |

# %% language="sql"
# CREATE VIEW SCHOOL_DASHBOARD AS
# SELECT NAME_OF_SCHOOL AS "School_Name",
#        SAFETY_ICON AS "Safety_Rating",
#        FAMILY_INVOLVEMENT_ICON AS "Family_Rating",
#        ENVIRONMENT_ICON AS "Environment_Rating",
#        INSTRUCTION_ICON AS "Instruction_Rating",
#        LEADERS_ICON AS "Leaders_Rating",
#        TEACHERS_ICON AS "Teachers_Rating"
# FROM CHICAGO_PUBLIC_SCHOOLS

# %% [markdown]
# ### Problem 2
#
# #### Write and execute a SQL statement that returns just the school name and leaders’ icon from the view. 

# %% language="sql"
# SELECT "School_Name", "Leaders_Rating"
# FROM SCHOOL_DASHBOARD
# LIMIT 5

# %% [markdown]
# ## Part 3
#
# ### Problem 1
# #### Write the structure of a query to create or replace a stored procedure called UPDATE_LEADERS_SCORE that takes a in_School_ID parameter as an integer and a in_Leader_Score parameter as an integer. Don't forget to use the #SET TERMINATOR statement to use the @ for the CREATE statement terminator.

# %% language="sql"
# --#SET TERMINATOR @
# CREATE OR REPLACE PROCEDURE UPDATE_LEADERS_SCORE ( 
#     IN in_School_ID INTEGER, IN in_Leader_SCORE INTEGER)
#
# LANGUAGE SQL
#
# BEGIN 
#     
# END
# @

# %% [markdown]
# ### Problem 2
#
# #### Inside your stored procedure, write a SQL statement to update the Leaders_Score field in the CHICAGO_PUBLIC_SCHOOLS table for the school identified by in_School_ID to the value in the in_Leader_Score parameter.

# %% language="sql"
# --#SET TERMINATOR @
# CREATE OR REPLACE PROCEDURE UPDATE_LEADERS_SCORE( 
# IN in_School_ID INTEGER, IN in_Leader_Score INTEGER )
#
# LANGUAGE SQL  
# MODIFIES SQL DATA             
#
# BEGIN
# 	UPDATE CHICAGO_PUBLIC_SCHOOLS
# 	SET LEADERS_SCORE = in_Leader_Score
# 	WHERE SCHOOL_ID = in_School_ID;
# END
# @ 

# %% [markdown]
# ### Problem 3
#
# #### Inside your stored procedure, write a SQL IF statement to update the Leaders_Icon field in the CHICAGO_PUBLIC_SCHOOLS table for the school identified by in_School_ID using the following information. 

# %% language="sql"
# --#SET TERMINATOR @
# CREATE OR REPLACE PROCEDURE UPDATE_LEADERS_SCORE( 
# IN in_School_ID INTEGER, IN in_Leader_Score INTEGER )
#
# LANGUAGE SQL  
# MODIFIES SQL DATA             
#
# BEGIN
# 	UPDATE CHICAGO_PUBLIC_SCHOOLS
# 	SET LEADERS_SCORE = in_Leader_Score
# 	WHERE SCHOOL_ID = in_School_ID;
# 	
# 	IF in_Leader_Score > 0 AND in_Leader_Score < 20 THEN
# 	
# 		UPDATE CHICAGO_PUBLIC_SCHOOLS
# 		SET LEADERS_ICON = 'Very Weak'
# 		WHERE SCHOOL_ID = in_School_ID;
#
# 	ELSEIF in_Leader_Score < 40 THEN
# 	
# 		UPDATE CHICAGO_PUBLIC_SCHOOLS
# 		SET LEADERS_ICON = 'Weak'
# 		WHERE SCHOOL_ID = in_School_ID;
#
# 	ELSEIF in_Leader_Score < 60 THEN
# 	
# 		UPDATE CHICAGO_PUBLIC_SCHOOLS
# 		SET LEADERS_ICON = 'Average'
# 		WHERE SCHOOL_ID = in_School_ID;
#
# 	ELSEIF in_Leader_Score < 80 THEN
#
# 		UPDATE CHICAGO_PUBLIC_SCHOOLS
# 		SET LEADERS_ICON = 'Strong'
# 		WHERE SCHOOL_ID = in_School_ID;
#
# 	ELSEIF in_Leader_Score < 100 THEN
# 		
# 		UPDATE CHICAGO_PUBLIC_SCHOOLS
# 		SET LEADERS_ICON = 'Very Strong'
# 		WHERE SCHOOL_ID = in_School_ID;
#
# 	END IF;
# END
# @

# %% [markdown]
# ### Problem 4
#
# #### Write a query to call the stored procedure, passing a valid school ID and a leader score of 50, to check that the procedure works as expected.

# %% language="sql"
# CALL UPDATE_LEADERS_SCORE(610281, 50)

# %%
--#SET TERMINATOR @
CREATE OR REPLACE PROCEDURE UPDATE_LEADERS_SCORE( 
IN in_School_ID INTEGER, IN in_Leader_Score INTEGER )

LANGUAGE SQL  
MODIFIES SQL DATA             

BEGIN
	UPDATE CHICAGO_PUBLIC_SCHOOLS
	SET LEADERS_SCORE = in_Leader_Score
	WHERE SCHOOL_ID = in_School_ID;
	
	IF in_Leader_Score > 0 AND in_Leader_Score < 20 THEN
	
		UPDATE CHICAGO_PUBLIC_SCHOOLS
		SET LEADERS_ICON = 'Very Weak'
		WHERE SCHOOL_ID = in_School_ID;

	ELSEIF in_Leader_Score < 40 THEN
	
		UPDATE CHICAGO_PUBLIC_SCHOOLS
		SET LEADERS_ICON = 'Weak'
		WHERE SCHOOL_ID = in_School_ID;

	ELSEIF in_Leader_Score < 60 THEN
	
		UPDATE CHICAGO_PUBLIC_SCHOOLS
		SET LEADERS_ICON = 'Average'
		WHERE SCHOOL_ID = in_School_ID;

	ELSEIF in_Leader_Score < 80 THEN

		UPDATE CHICAGO_PUBLIC_SCHOOLS
		SET LEADERS_ICON = 'Strong'
		WHERE SCHOOL_ID = in_School_ID;

	ELSEIF in_Leader_Score < 100 THEN
		
		UPDATE CHICAGO_PUBLIC_SCHOOLS
		SET LEADERS_ICON = 'Very Strong'
		WHERE SCHOOL_ID = in_School_ID;

	ELSE
		ROLLBACK WORK;
		
	END IF;
END
@  
