import pandas as pd # data manupulation
import numpy as numpy
import  matplotlib.pyplot as plt #this library is for creating the visualization
import seaborn as sns # data visualization


df = pd.read_csv('data.csv')#I am loading my data
print(df.head())

# I used a dictionary for listing my Data
data = {
    'Province': ['Eastern Cape', 'Free State', 'Gauteng', 'KwaZulu-Natal', 'Mpumalanga','North West', 'Western Cape', 'Northern Cape'],
    'Voting Stations': [27, 20, 30, 32, 18, 18, 25, 18],
    'Expected': [1339, 954, 1793, 1843, 865, 993,1362, 1089]
}

print(df.isnull().sum())#this line checks the missing values of my data


# Creating DataFrame: I am converting my dictionary into panda Dataframe
df = pd.DataFrame(data)


plt.figure(figsize=(10, 6))# i am creating the visualization
sns.barplot(x='Province', y='Voting Stations', data=df, color='skyblue', label='Voting Stations')
sns.lineplot(x='Province', y='Expected', data=df, marker='o', color='orange', label='Expected Votes', linewidth=2)


plt.title('Voting Stations and Votes per Province', fontsize=16)#ploting the data
plt.xlabel('Province', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

