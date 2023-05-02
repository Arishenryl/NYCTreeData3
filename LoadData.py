import sys
import pandas as pd
import re

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
    print(Tree_data['spc_common'].unique().sorted())

def formatInfo(matched_trees):
#below is untested and buggy code. 
    for x in matched_trees:
        grouped_zipcode=Tree_data.groupby(['zipcode']).get_group(x)
        grouped_boro=Tree_data.groupby(['boroname']).get_group(x)
        boroMax=grouped_boro.max()
        print(f"Entry: {x}")
        print(f"Total number of trees: ")
        print(f"Zip codes in which this tree is found: {grouped_zipcode}")
        print(f"Borough containing the largest number of trees: {boroMax}")
  
def treeInfo(entry):
    #match the user input string to common species names of trees column.
    #TreeInfo
    entry.lower()
    matched=[]
    for x in Tree_data['spc_common'].unique(): 
        TEXT = entry
       
        if (str(x) in TEXT):
            matched.append(x)
        else:
            continue
    formatInfo(matched)
       
    
#Interactive loop that it is central control for the program
flag=True

while flag:
    print('** NYC TREE DATA Searcher **')
    userInput=input()
    if (userInput=='help'):
        pass
        getHelp() #command to display information about each command

    elif (userInput=='listtrees'):
        listTrees()
        pass
    elif ('treeinfo ' in userInput):
        treeInfo(userInput)
        pass
    elif (userInput=='nearby'):
        #nearby()
        pass
    elif (userInput=='quit'):
        exit()
    else:
        print('Command not understood. Please enter valid command.')
