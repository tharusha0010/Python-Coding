import os
import pandas as pd
os.system('cls')

data = {
    "Name": ["kamal" ,"Nimal","Amal"],
    "Age": [30,35,50]    
    }
df = pd.DataFrame(data , index = ["STUDENT01","STUDENT02","STUDENT03"])
print(df)

print("Access The Location")
print(df.loc["STUDENT02"])

#Add a new column
df["job"] = ["cook","N/A","cashier"]
print(df)

#Add a new row
new_row = pd.DataFrame([
    {"Name":"Sandy","Age":28,"job":"Engineer"},
    {"Name":"Ruwan","Age":60,"job":"Manager"}],
                       index = ["STUDENT04","STUDENT05"])
df = pd.concat([df,new_row])
print(df)