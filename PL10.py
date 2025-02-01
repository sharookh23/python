#APPLICATION OF SERIES & DATAFRAMES
import pandas as pd
import numpy as np
student  = {
      'eng' : ([11.0,25.0,13.0,np.NaN]),
      'maths' : ([21,0,3,24])}

df1=pd.DataFrame(student,index=['Ram','Allah','Jesus','Buddha'])

df1['IP']=([25,20,15,18])

df1['Total']=df1['eng']+df1['maths']+df1['IP']
print("shape : ",df1.shape)
print("oclumns: ",df1.columns)
print(df1)
