import pandas as pd 
import numpy as np 
#users data
#set data for reproducibility
np.random.seed(42)
#create data frame for 20 users
names=[
"Mary",
"Napoleon",
"Hill",
"Wambley",
"Ndege",
"Noel",
"Peter",
"John",
"Maryanne",
"Hillary",
"Marion",
"Claire",
"Cherry",
"Pine",
"Stone",
"Veronica",
"Esther",
"Andrew",
"James",
"Nelly"
]
#age
ages=np.random.randint(22,50,size=20)
#gender
gender=np.random.choice(["F","M"],size=20)
#marital status
marital_status=np.random.choice(["Married","Divorced","Single"],size=20)
#city
cities=np.random.choice(["Nairobi","Addis Ababa","Lagos","Dakar","Kampala","Mogadishu"],size=20)
#occupation
occupation=np.random.choice(["Teacher","Product Manager","Accountant","Data Analyst","Plumber"],size=20)
#salary
salary=np.random.randint(50000,300000,size=20)
#hobby
hobby=np.random.choice(["Travelling","Swimming","Reading novels","Watching movies"],size=20)
#data frame
users_data=pd.DataFrame({
    "Name":names,
    "Age":ages,
    "Gender":gender,
    "Marital Status":marital_status,
    "City":cities,
    "Occupation":occupation,
    "Salary":salary,
    "Hobby":hobby
})

#save to csv
users_data.to_csv("users_data.csv",index=True)
print("File saved as csv successfully")