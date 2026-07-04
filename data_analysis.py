import pandas as pd 
#pd.read_csv() is a pandas function used to load data from a csv file into a dataframe for analysis and manipulation
data = pd.read_csv("matches.csv")
# return first 5 rows of the dataset by default
#print(data.head())
# return last 5 rows of the dataset by default
#print(data.tail())
#it is a pandas dataframe attribute that returns a tuple(rows,columns) used to determine the size of a dataset
#shape[0] - rows no , shape[1] - columns no
#print(data.shape)
#data.info provide the summary of the dataframe 
#print(data.info())
#generates descriptive statistics for the numeric columns in a dataframe
#print(data.describe())
#fetching rows and columns using iloc
#print(data['winner'])#single column fetching
#print(data[['team1','team2','winner']])#multiple fetching
print(data.iloc[0])# single row fetch
print(data.iloc[1:11:2]) #multiple row
print(data.iloc[:,[4,5,10]])#both rows and columns
