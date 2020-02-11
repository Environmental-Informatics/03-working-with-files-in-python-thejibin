#!/usr/local/bin/python3.6
"""Created on 2020-02-06
by Jibin Joseph

Assignment 03 - Using Files and Simple Data Structures with Python


Modified to add comments
"""
## Import the required packages
import math

## Read the given data using the built-in file open function to variable called "lines

datafile=open("2008Male00006.txt",'r')
lines=datafile.readlines()
## Closes the open file
datafile.close()

## Create an empty list correponding to line numbers in given data
data=[0]*len(lines)

## Create a loop to which traverse all lines except the initial and final lines
## Split the lines using comma delimiter
## Convert columns of numbers into lists of the correct number type (int, float, complex).
for i in range(1,len(lines)-1):
    data[i]=lines[i].split(',')
    data[i][3]=int(data[i][3])
    for j in range(4,15):
        try:
            data[i][j]=float(data[i][j])
        except:
            data[i][j]=(data[i][j])

## Remove the initial and final lines of the data
data.pop(0)
data.pop(-1)

## Split and store the initial and final lines in data
lastline=lines[-1].strip().split(",")
head=lines[0].strip().split(",")

## Create a new dictionary
dict_data=dict()

## Create empty list
list_store=[[]]*15
for list_i in range(0,15):
   list_store[list_i]=[]

## Add the values to the list
for list_i in range(15):
    for list_j in range(14):
        list_store[list_i].append(data[list_j][list_i])

## Create the dictionary
for list_i in range(15):
    dict_data[head[list_i]]=list_store[list_i]

## Compute the mean or average of a list.
def average_dictlist(dict_list):
    """
    Function computes the mean or average of the data stored in dictionary as a list
    Input: a list
    """
    avg=sum(dict_list)/len(dict_list)
    return avg

##  Compute the cumulative sum of a list.
def cum_sum_dictlist(dict_list):
    """
    Function computes the cumulative sum of the data stored in dictionary as a list
    Input: a list
    """
    cum_sum=[]
    sum=0
    for i in range(len(dict_list)):
        sum=dict_list[i]+sum
        cum_sum.append(sum)
    return cum_sum
## Compute the distance between two points, when X and Y coordinates are provided as two lists, one of X-coordinates and one of Y-coordinates.
def distanceXandY(X,Y):
    """
    Function computes the distance traveled when X and Y coordinates are provided as lists
    Input: X,Y
    Use the distance euclidean distance formula
    """
    distanceXY=[0]*len(X)
    i=1
    while i<len(X):
        distanceXY[i]=math.sqrt((X[i]-X[i-1])**2 + (Y[i]-Y[i-1])**2)
        i+=1
    return distanceXY
## Add George's movement to the data dictionary using the key word "Distance"
dict_data.update({'Distance':distanceXandY(dict_data[' X'],dict_data[' Y'])})

## New header block in required format with blank line in between the header block and the next section of the file
header_block=['Raccoon name: George Number  ' + str(dict_data["George #"][0]) + '\n',
    'Average location: ' + str(average_dictlist(dict_data[" X"])) + ", " + str(average_dictlist(dict_data[" Y"])) +'\n',
    'Distance traveled: ' + str(cum_sum_dictlist(dict_data['Distance'])[-1])+ '\n',
    'Average energy level: ' + str(average_dictlist(dict_data['Energy Level'])) + '\n',
    'Raccoon end state: '+ lastline[0]+ '\n','\n']

## Create a new output file called "Georges_life.txt" (write mode)
## Also write the header block to the new file
filetowrite=open("Georges_life.txt",'w')
filetowrite.writelines(header_block)

## Creates a new dictionary with select contents of data dictionary
## Date, Time, X and Y coordinates, the Asleep flag, the behavior mode, and the distance traveled (in that order)
dict_data_new={keys:dict_data[keys] for keys in ('Day','Time',' X',' Y',' Asleep','Behavior Mode', 'Distance') if keys in dict_data}


## Create a loop with the keys to print the select contents to new TAB delimited section of the file
for key in dict_data_new.keys():
	filetowrite.write(str(key) + '\t')
## To start a new line
filetowrite.write('\n')

## Create a loop to traverse the dictionary and write the values with TAB delimited
for i in range(len(dict_data_new['Distance'])):
	for value in dict_data_new.values():
		filetowrite.write(str(value[i]) + '\t')
	filetowrite.write('\n')

## To close the file and immediately free up any system resources used
filetowrite.close()