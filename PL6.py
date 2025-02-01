#USAGE OF RENAME ().HEAD()&TAIL() - dataframes

import pandas as pd
ans = input("\n Do you want to print the menu(y=yes/n=no):  ")
while ans =='y' or ans =='Y' :

      print("\n DataFrame operations")
      print(" 1.Add the records")
      print(" 2.display details of all records")
      print(" 3.diplay first 3 rows & last 3 rows")
      print(" 4.Rename any column of your choice: ")
      print(" 5.Exit")
      choice = int(input("Enter your choice:  "))
      if choice ==1:
            n=int(input("Enter how many records u want to enter : "))
            data1=([])
            for a in range(n):
                  animal1=input("Enter the name of animal: ")
                  uniqid1=int(input("Enter the id of aimal: "))
                  water=int(input("Enter the amount of water neeeded: "))
                  newrow={'animal':animal1, 'uniqid':uniqid1, 'water_need':water}
                  data1.append(newrow)
            df2=pd.DataFrame(data1)
      elif choice ==2:
            print("zoo")
            print(df2)
      elif choice ==3:

            print(df2.head(2))
            print(df2.tail(3))

      elif choice ==4:
            y=input("Enter the column to be renamed:  ")
            df2.rename(columns={y:'name'},inplace=True)
            print(df2)
      elif choice ==5:

            exit()
      else:
            break
else:
       print("\n please quit")
            
