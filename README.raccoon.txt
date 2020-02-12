Metadata File
***
Assignment 03 : Using Files and Simple Data Structures with Python
The script is created as part of 
ABE 65100 Environmental Informatics
Semester: Spring 2020
Instructor: Prof Keith Cherkauer

Python Version: Python 3.6


DOUBTS:

1. What is the units of X and Y? Can it be assumed to metres

******* ******* ******* *******

SCRIPT OBJECTIVES:

1. Use Python's built-in file functions and methods to open, read and write the contents of data files; and
2. Use Python's built-in data structures to organize and summarize data.

******* ******* ******* *******

NAME OF PROCESSING SCRIPT:

Evaluate_Raccoon_Life.py

******* ******* ******* *******

DESCRIPTIONG OF THE PROCESSING BEING COMPLETED BY THE SCRIPT


Definition Blocks
***
1. Compute the mean/ average of values contained list assigned to a key of the dictionary
2. Compute the cumulative sum of values contained in the list
3. Compute the euclidean distance between two points from the X and Y coordinates

Main Code
***

1. The scripts reads the input file 2008Male00006.txt containing the output from a Raccoon behavior model which describes the movement of a simulated raccoon named George over the course of a day (The file is obtained in comma separted fomart with hourly data).
2. Firstly, the data is split using comma delimiter in to a list and few columns containing the numbers are converted from the default type into the correct type (int/float/complex) using try and except
3. Initial and final lines are removed from the calculation using pop method. Also the initial line is split using comma delimiter to serve as the key for the dictionary.
4. A dictionary is created with headers as key and values to the key as list of data values. 
5. Using the distance function, the distance from the previous point is calculated and updated in the dictionary as a list for new key called Distance.
6. A header block containing the parameter names and values of parameters (for Raccoon name, Average location, Distance traveled, Average energy level and Raccoon end state.
7. Further, a new dictionary is created (as a subset of earlier one) with selected parameters.
8. Additionally, a new text file (Georges_life.txt) is created in the same directory (in write mode) and the header block is written in to the file.
9. Now, the keys from the new dictionary are written to the text file as column headers with TAB separation
10. Later, the values corresponding to the keys from the new dictionary are written in to the file with TAB separation.

   
******* ******* ******* *******

NAMES OF THE INPUT AND OUTPUT FILES

Input: 2008Male00006.txt (same directory)
Output: Georges_life.txt (same directory)
