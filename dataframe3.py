import pandas as pd
student={'name' : ['rinku', 'rinu', 'ajay', 'pankaj', 'adithya'], 'english': [67,68,75,88,99], 'econ': [78,67,89,90,78], 'ip' : [79,88,98,90,78]}
df=pd.DataFrame(student,index=['sno1', 'sno2', 'sno3', 'sno4', 'sno5'])
print ("dataframe for student with labelled index")
print(df)
