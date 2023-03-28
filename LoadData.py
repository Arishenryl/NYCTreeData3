
import sys
import pandas as pd

#sys.argv contains name of our script (argument 0) and all the arguments
file=str(sys.argv[1])

#Using pandas library to load CSV file into pandas 'DataFrame'
Tree_data= pd.read_csv(file)


#Functions
def getHelp():
    #Part 2 code here
def listTrees():
    #Part 3 code here
def treeInfo():
    #TreeInfo
#Interactive loop that it is central control for the program
flag=True

while flag:
    userInput=input()
    if (userInput=='help'):
        pass
        #getHelp() command to display information about each command

    elif (userInput=='listtrees'):
        #listTrees()
    elif (userInput=='treeinfo'):
        #treeInfo
    elif (userInput=='nearby'):
        #nearby()
    elif (userInput=='quit'):
        exit()
    else:
        print('Command not understood. Please enter valid command.')
