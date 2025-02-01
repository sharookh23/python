#ROW & COLUMN OPERTATIONS ON DATAFRAME
import pandas as pd
year ={'2015' : [256,452,635,965],
       '2016': [745,785,478,547],
       '2017' : [452,474,725,854],
       '2018' : [1021,958,528,425]}
df=pd.DataFrame(year, index =['Qtr1','Qtr2','Qtr3','Qtr4'])

ans = input("\n Do you mwant to print the menu(y = yes/n = no): ")
while ans =='y' or ans =='Y' :
      print("\n Row & column opertions")
      print(" 1.Create & Display Dataframe")
      print(" 2.Delete details of Qtr2 ")
      print(" 3.Rename Qtr1 as Quater1")
      print(" 4.Add a new column 2019")
      print(" 5.Add a new row ")

      choice = int(input("Enter your choice : "))
      if choice==1:
            print(df)
      elif choice==2:
            df.drop(index="Qtr2",axis=0,inplace=True)
            print(df)
      elif choice==3:
            df.rename(index={'Qtr1':'Quater1'},inplace=True)
            print(df)
      elif choice==4:
            year={'2015' : [256,452,635,965],
                  '2016': [745,785,478,547],
                  '2017' : [452,474,725,854],
                  '2018' : [1021,958,528,425]}
            df=pd.DataFrame(year,index = ['Qtr1','Qtr2','Qtr3','Qtr4'])
            df['2019'] = [524,639,785,458]
            print(df)
      elif choice==5:
            newrow={'2015' : 1000, '2016' : 500, '2017' : 400, '2018' : 100 , '2019' : 700 }
            df=df.append(newrow,ignore_index=True)
            print(df)
      else:
            break

else:
      print("\n please quit")
      
