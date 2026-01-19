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
}
)
#set index
users_data.index=range(1,len(users_data)+1)
#save to csv
users_data.to_csv("users_data.csv",index=True)
print("File saved as csv successfully")

#calculate q1
Q1=users_data['Age'].quantile(0.25)
print("25th Percentile: ",Q1)
Q3=users_data['Age'].quantile(0.75)
print("75th Percentile: ",Q3)
IQR=Q3-Q1
print("Interquartile range: ",IQR)
#calculate lower boundary
lower_bound=Q1-(1.5*IQR)
print("Lower bound: ",lower_bound)
#upper bound
upper_bound=Q3+(1.5*IQR)
print("Upper bound: ",upper_bound)
#find out if there is any outlier
outlier=users_data[(users_data['Age']<lower_bound)|(users_data['Age']>upper_bound)]
print(f"\nOutlier: ,{outlier['Age'].tolist()}")