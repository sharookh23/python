import pandas as pd
dict1={ 'Max_temp' : [40,31,35,28,30],
              'Min_temp' : [32,27,25,22,23],
            'Rainfall' : [23.1,36.2,41.2,37.3,45.0] }

df=pd.DataFrame(dict1,index=['Delhi' , 'Banglore' , 'Chennai' , 'Mumbai' , 'Kolkata' ] )
ans = input("\n Do you want to print the menu(y = yes/ n = no):  ")
while ans == "y" or ans == "Y" :
      print("\n DataFrame operations")
      print(" 1.Display first two rows:  ")
      print(" 2.Rename  column maxtemp ")
      print(" 3.Rename row Kolkata to Kerala")
      print(" 4.Add a new column covid")
      print(" 5.Drop the column rainfall")
      print(" 6.Drop row chennai")

      choice  =  int(input("Enter your choice:  "))
      if choice==1:
                  print(df.head(2))

      elif choice==2:
                  df.rename(columns={'Max_temp':'Maximum_temp'} , inplace=True)
                  print(df)

      elif choice==3:
                  df.rename(index={'Kolkata' : 'Kerala'} , inplace =True)
                  print(df)
      elif choice==4:
                  Data=[800,200,400,400,1000]
                  df["Covid"]=Data
                  print(df)

      elif choice==5:
                  df.pop('Rainfall')
                  print(df)

      elif choice==6:
                  df.drop(labels="Chennai", axis=0, inplace=True)
                  print(df)

      else:
                  break
else:
      print("\n Please quit, Thank you")
