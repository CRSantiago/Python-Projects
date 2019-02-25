
# coding: utf-8

# In[5]:


import csv
from collections import*


# In[14]:


average_call_dict = {'EMS': [], 'AUTOMATIC ALARM': [], 'TRAFFIC': [], 'MUTUAL AID': [], 'FIRE':[], 'UNKNOWN':[],
                        'HAZMAT': [], 'PUBLIC SERVICE': []}

f = open('fire_clean.csv')
reader = csv.DictReader(f)
for row in reader:
    times = row['duration']
    timeSplit = times.split(':')
     
    hours = timeSplit[0]
    minutes = timeSplit[1]
    seconds = timeSplit[2]
    
    hoursSeconds = (int(hours) * 3600)
    minutesSeconds = (int(minutes) * 60)
    total = hoursSeconds + minutesSeconds + int(seconds)
    
    if(row['type'] == 'EMS'): 
        average_call_dict['EMS'].append(total)
        
    if(row['type'] == 'AUTOMATIC ALARM'): 
        average_call_dict['AUTOMATIC ALARM'].append(total)
        
    if(row['type'] == 'TRAFFIC'): 
        average_call_dict['TRAFFIC'].append(total)
        
    if(row['type'] == 'MUTUAL AID'):
        average_call_dict['MUTUAL AID'].append(total)
        
    if(row['type'] == 'FIRE'): 
        average_call_dict['FIRE'].append(total)
        
    if(row['type'] == 'UNKNOWN'): 
        average_call_dict['UNKNOWN'].append(total)
  
    if(row['type'] == 'HAZMAT'): 
        average_call_dict['HAZMAT'].append(total)
      
    if(row['type'] == 'PUBLIC SERVICE'): 
        average_call_dict['PUBLIC SERVICE'].append(total)
      
    

    
print("Average length of call, by type: ")
for keys, values in average_call_dict.items():
    average_call_dict[keys] = sum(values) / float(len(values))
    
print(average_call_dict)

f = open('fire_clean.csv')
reader = csv.DictReader(f)
description_list = []
for rows in reader:
    description_list.append(row['description'])

Counter(description_list).most_common()

