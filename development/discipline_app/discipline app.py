
# coding: utf-8

# In[1]:


import pandas as pd
from enum import Enum
from datetime import datetime, timedelta
from IPython.display import display # Just for pretty display of dfs
from random import randint

# Check for '#testing'


# In[12]:


FIRST_RUN = False
RUN_TODAY = False


# In[3]:


def create_new_field(field, first_value):
    """Creates"""
    
    today = datetime.now().date()
    value = first_value
    
    df = pd.DataFrame({'Date' : [today], 'Value' : [first_value]})
    df.to_csv(field + ".csv")

def get_new_value_from_user(field):
    """Simply asks and returns value for a particular field from user."""
    return randint(0,10)   #testing

    print "Please enter a value for " + field
    val = input()
#     Do type checking here
    return val

def add_new_value(field, value):
    """Adds a value(with today's date) to the field and writes to the relevant file."""
    today = datetime.now().date()
    
# testing
    today = today + timedelta(randint(0,100))
    
    df = pd.read_csv(field + ".csv", index_col=0)
    
    new_entry = pd.Series({'Date' : today, 'Value' : value})
    df = df.append(new_entry, ignore_index=True)
    
    display(df.tail())
    df.to_csv(field + ".csv")



def update_next_check(field):
    df = pd.read_csv("Meta.csv")
    
    current_check_date = df[df['Field']==field].iloc[0] ['Next Check']
    update_frequency = df.loc[df['Field']==field, 'Check Frequency'].iloc[0]
    
    
    next_check = datetime.strptime(current_check_date, "%Y-%m-%d") + timedelta(days= update_frequency)
    next_check = next_check.date()
    
    df.loc[ df['Field']==field, 'Next Check'] = next_check
    
    df.to_csv("Meta.csv", index=False)    
    


# In[4]:


def first_time_setup():
    """Setting up for the first time!"""
    temp = datetime.now().date()

    FIELD = ["Football", "Strength_training", "Study", "Mobile_usage", "Screen_Unlock_times"]
    CHECK_FREQUENCY = [1, 1, 7, 7, 7] #In number of days
    NEXT_CHECK = [ temp, temp, temp, temp, temp]

    df = pd.DataFrame({'Field' : FIELD, 'Check Frequency' : CHECK_FREQUENCY, 'Next Check' : NEXT_CHECK})
    df = df[['Field', 'Check Frequency', 'Next Check']]
    df.to_csv('Meta.csv')
    
    for field in FIELD:
        create_new_field(field, 0) 
    


# In[5]:


if FIRST_RUN:
    first_time_setup()


# In[6]:


# Front End
# Run this part daily once
def daily_check():
    """This function runs daily to check for deadline and updates value in file after taking input from user."""
    if not RUN_TODAY:
        try:
            df = pd.read_csv("Meta.csv")
            FIELD = list(df['Field'])

            for i, field in enumerate(FIELD):
                if i>0:
                    break

                df_field = df.loc[ df['Field'] == field]

                today = str(datetime.now().date())
                next_check = df_field['Next Check'].iloc[0]

                next_check  = today

                if(next_check == today):
                    print "Appending value"
                    add_new_value(field, get_new_value_from_user(field))
                    update_next_check(field)

        except Exception as e:
            print "Probably this is your first run!!! "
            print "If not, there is some bug in code. Sorry man."

            print(e)


# In[21]:


daily_check()


# In[22]:


df = pd.read_csv("Football.csv", index_col=0)


# In[23]:


dates = list(df['Date'])
value = list(df['Value'])


# In[34]:


import matplotlib.pyplot as plt
# %matplotlib gtk


plt.plot(dates, value)
plt.xlabel('Value')
plt.ylabel('Date')
plt.show()

