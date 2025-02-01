#adding,selecting,filtering a dataframe

import pandas as pd

data1 = [['soap', 'lux', 50]]
data2 = [['shampooo', 'deedhi', 60]]
data3 = [['paste', 'colgate', 50]]

df1 = pd.DataFrame(data1,columns = ['item_category', 'item_name', 'units_sold'])
df2 = pd.DataFrame(data2,columns = ['item_category', 'item_name', 'units_sold'])
df4 = pd.DataFrame(data3,columns = ['item_category', 'item_name', 'units_sold'])
df3 = df1.append(df2)
df5 =df3.append(df4)

ans = input("\n Do you want to print the menu(y = yes/n =no): ")
while ans == 'y' or ans =="Y" :
      
            print("\n Quaterly SALES")
            print(" 1. Add a record ")
            print(" 2. Display the records")
            print(" 3.Query on category paste:")
            print(" 4.Exit")
            choice = int(input("enter your choice (1-4) :   "))
            if choice ==1:
                         item = input("Enter the item category : ")
                         name = input('Enter the item name: ')
                         units = int(input("Enter the units sold :"))
                         data4 = [[item,name,units]]
                         df6 = pd.DataFrame(data4,columns = ['item_category','item_name','units_sold'])
                         df7 = df5.append(df6,ignore_index = True)

            elif choice == 2:
                        print(df7)

            elif choice == 3:
                        print(df7.iloc[[2]])

            elif choice == 4:
                        exit()
            else:
                        break
else:
      print("\n please quit")
