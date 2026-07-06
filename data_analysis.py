import pandas as pd 
import matplotlib.pyplot as plt
#pd.read_csv() is a pandas function used to load data from a csv file into a dataframe for analysis and manipulation
data = pd.read_csv("matches.csv")
# return first 5 rows of the dataset by default
print(data.head())
# return last 5 rows of the dataset by default
print(data.tail())
#it is a pandas dataframe attribute that returns a tuple(rows,columns) used to determine the size of a dataset
#shape[0] - rows no , shape[1] - columns no
print(data.shape)
#data.info provide the summary of the dataframe 
print(data.info())
#generates descriptive statistics for the numeric columns in a dataframe
print(data.describe())
#fetching rows and columns using iloc
print(data['winner'])#single column fetching
print(data[['team1','team2','winner']])#multiple fetching
print(data.iloc[0])# single row fetch
print(data.iloc[1:11:2]) #multiple row
print(data.iloc[:,[4,5,10]])#both rows and columns
#filteing dataframe on a condition
mask = data['city']=='Hyderabad'
print(data[mask])
def get_city_match_count(city):
    mask = data['city'] == city
    return data[mask].shape[0]
print(get_city_match_count('Bangalore'))    
mask1 = data['city'] == 'Hyderabad'
mask2 = data['date']>'2010-01-01'
print(data[mask1 & mask2])
# Value_counts() function
print(data['winner'].value_counts())
# the plot function
print(data['winner'].value_counts().plot(kind='bar'))
plt.show()
data['toss_decision'].value_counts().plot(kind='pie')
plt.show()
#series operations
print(data['team2'].value_counts() + data['team1'].value_counts())
#the sort_values() method
print((data['team2'].value_counts() + data['team1'].value_counts()).sort_values(ascending = False))#inplace is used to do changes permanent
print(data.sort_values(['city','date']),ascending=[True,False])
#drop duplicates method
print(data.drop_duplicates(subset=['city']))
print(data.drop_duplicates(subset=['city','season']).shape)






