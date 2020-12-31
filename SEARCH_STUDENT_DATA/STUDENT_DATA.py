

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# In[53]:
"""
Q1.Read the given CSV file share with an assignment and use any python data structure
   (DataFrames, ndArray etc) to load the data into the system.

Answer:- Below is the code (line no. 21 and 22) for reading the marks from the CSV file that has been shared.The data 
        is read into DataFrame using 'read_csv' function from pandas library.
"""

df=pd.DataFrame()
df=pd.read_csv("2CS404_sessional_assignment.csv", engine='python')
#print(df)

"""
Q2.Fill the missing values of p6, p7, p8, p9 and p10. You can use any techniques to fill the missing
   value for all students.
Answer:- To fill the missing values of practical 6-10 we have stored random values in them using random.randint() 
         function. The range of the random marks generated are set to be from 1 to 10.
         Below is the Code for the same.
"""
df['Practical6']=np.random.randint(0,11,size=(len(df),1))
df['Practical7']=np.random.randint(0,11,size=(len(df),1))
df['Practical8']=np.random.randint(0,11,size=(len(df),1))
df['Practical9']=np.random.randint(0,11,size=(len(df),1))
df['Practical10']=np.random.randint(0,11,size=(len(df),1))
#print(df)


"""
Q3. Generate the random marks for sessional , innovative assignment ,viva and SEE exam filed.
    Marks range is given in the above tables.
Answer:- For the given components the same method random.randint() is used to generate the marks.The range of marks for 
         sessional(0-40), innovative assignment(0-30) ,Viva(0-25), SEE(0-100).
"""

df['Sessional']=np.random.randint(0,41,size=(len(df),1))
df['Innovative_Assignment']=np.random.randint(0,31,size=(len(df),1))
df['Viva']=np.random.randint(0,26,size=(len(df),1))
df['SEE']=np.random.randint(0,101,size=(len(df),1))
#print(df)


# In[67]:
"""
Q4.Make a list of students who obtain the less than 40% marks in any of components means CE,
   LPW and SEE in Django HMTL table.
Answer:- We calculate all the components CE,SEE,LPW as per the guidelines given in question paper, and store the 
         total in respective coloumns in dataframe for each student.
         df['CE_TOTAL']= CE total as per the ,]marking scheme
         df['LPW_TOTAL']=LPW total as per the marking scheme
         df['SEE']=SEE marks
         
         The furthur code  and answer for DJANGO HTML TABLE part is in view.py
"""

df_CE=df[['Rollno','ClassTestMark','Sessional','Innovative_Assignment']]
df_CE['CE_TOTAL']=df_CE.loc[:,['ClassTestMark','Sessional','Innovative_Assignment']].sum(axis=1)
df['CE_TOTAL']=df_CE['CE_TOTAL']

df_LPW=df[['Practical1','Practical2','Practical3','Practical4','Practical5','Practical6','Practical7','Practical8','Practical9','Practical10','Viva']]
df_LPW['LPW_TOTAL']=(df_LPW[['Practical1','Practical2','Practical3','Practical4','Practical5','Practical6','Practical7','Practical8','Practical9','Practical10']].sum(axis=1))*0.75
df_LPW['LPW_TOTAL']=df_LPW[['LPW_TOTAL','Viva']].sum(axis=1)
df['LPW_TOTAL']=df_LPW["LPW_TOTAL"]

df_FAIL=df[(df.SEE<40) | (df.CE_TOTAL<40) | (df.LPW_TOTAL<40)]
df_PASS=(df[(df.SEE>40) & (df.CE_TOTAL>40) & (df.LPW_TOTAL>40)])
#print(df_FAIL)




