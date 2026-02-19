import pandas as pd #importing pandas library
import numpy as np #importing numpy library
from io import StringIO #importing StringIO from io module for in memory file object

arr1 = np.arange(1,21).reshape(5,4) #Creating an array from 0 to 20
# print(arr1)
## Creating a Datafram

df = pd.DataFrame(data=arr1,index=['R1','R2','R3','R4','R5'],columns=['C1','C2','C3','C4']) #Creating a Dataframe from array with row and column labels
# print(df)
# print(df.head())  #Output: it will print the first 5 rows of the dataframe
# print(type(df))  #Output: <class 'pandas.core.frame.DataFrame'>
# print(df.info())  #Output: it will print the information about the dataframe like number of rows, columns, data types etc.

##Indexing and Slicing

# the example of series
# print(df['C2'])  #Output: it will print the column C2 

#the example of dataframe
# print(df[['C1','C3']])  #Output: it will print the columns C1 and C3

## Diff btwn seires and dataframe
# DATAFRAME: when we combine the multiple raw and columns together it will become dataframe
# SERIES: when we have single row or single column it will become series

# print(df['R1':'R3'])  #Output: it will print the rows R1 to R3
# print(df.loc['R1':'R3'])  #Output: it will print the rows R1 to R3

## why we use loc and iloc : because loc and iloc are used for more advanced indexing and slicing operations
## what if we don't use loc and iloc : we can still use the basic indexing and slicing methods but loc and iloc provide more flexibility and functionalitye from the array.

# print(df.loc['R2','C3'])  #Output: it will print the value at row R2 and column C3


# print(df.iloc[2:5,0:3]) # it means rows from index 2 to 4 and columns from index 0 to 2, [raw(start:stop), column(start:stop)] start is inclusive and stop is exclusive means the stop index will not be included in the output


## ASSIGNMENT
# print("Assignement Solution:")
# print(df.iloc[0:5,[0,3]]) # it means rows from index 0 to 4 and columns at index 0 and 3, [raw(start:stop), column(list of indices)] start is inclusive and stop is exclusive means the stop index will not be included in the output

#### PART 2


# pd.read_csv('Basic/sample.csv')  # it will read the csv file and create a dataframe

data=('Col1,Col2,Col3\n'
      'x,y,1\n'
      'a,b,2\n'
      'c,d,3\n')

# print(type(data))  #Output: <class 'str'>
# print(data)

## In memory file

StringIO(data)  # it will create an in memory file object from the string data
# print(type(StringIO(data)))  #Output: <class '_io.StringIO'>

# pd.read_csv(StringIO(data))  it will read the in memory file object and create a dataframe
# print(pd.read_csv(StringIO(data)))


### Datatyope in csv

data2=('Col1,Col2,Col3,Col4\n' 
       'x,y,1,4.5\n'
      'a,b,2,3.4\n'
      'c,d,3\n')

df2 = pd.read_csv(StringIO(data2))
# print(df2)

# print(df2.dtypes)  # it will print the data types of each column in the dataframe

data3 = ('index, a, b,c\n'
         '4, appple, bat, 5.4\n'
         '8, orange, cat, 60\n')

pd.read_csv(StringIO(data3), index_col=0)  # it will read the in memory file object and create a dataframe with the first column as index

# print(pd.read_csv(StringIO(data3), index_col=0))
# print(pd.read_csv(StringIO(data3)))



### Part 3

data4 = '{"employName": "Aditya", "email": "adi@gmail.com", "jobProfile": [{"title": "Team Leader", "title2": "Front-end Developer"}]}'

# print(type(data))  # it will return the type of data <class 'str'>

# print((data4))

print(pd.read_json(StringIO(data4)))  # read JSON string via StringIO so pandas treats it as data


df5 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['Row1', 'Row2'], 
                   columns=['Col1', 'Col2'])

print(df5)

print(df5.to_json())  # it will convert the dataframe to json string

