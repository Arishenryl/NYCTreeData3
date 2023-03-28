
import sys
import pandas as pd

#sys.argv contains name of our script (argument 0) and all the arguments
file=str(sys.argv[1])

#Using pandas library to load CSV file into pandas 'DataFrame'
Tree_data= pd.read_csv(file)


#Functions
def getHelp():
#beginning of help command file; basically a "man" page
print ("listtrees: can help one get a list of common tree names.")
#treeinfo command help file description
print ("treeinfo: can get information about a species of tree. One input argument is required to run the code.")
#nearby command help  file description 
print ("nearby: can get a list of information of all trees within a defined distance from some location. Various input arguments are required to run the code.")
#how to quit the help command application
print ("quit: command quits the application.")

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
