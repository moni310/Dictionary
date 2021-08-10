data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
     {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

dic={}
for key,value in data.items():
    if value not in dic.values():
        dic[key]=value
print(dic)
