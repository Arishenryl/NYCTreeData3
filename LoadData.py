
import sys
import pandas as pd
import re
from math import radians, cos, sin, sqrt

#sys.argv contains name of our script (argument 0) and all the arguments
file=str(sys.argv[1])

#Using pandas library to load CSV file into pandas 'DataFrame'
Tree_data= pd.read_csv(file)
tree_list= Tree_data.groupby('spc_common')

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

def format_info(matches):
    pass
def treeInfo2(entry): 
    matched_list=[]
    for x in Tree_data['spc_common'].unique():
        if x is entry:
            matched_list.append(x)
    
def formatInfo(matched_trees):
    for x in matched_trees:
        print(f"Entry: {x}")
        total=0
        for tree in Tree_data['spc_common']:
            if x==tree:
                total+=1
        print(f"Total number of trees:{total} ")
    
        #NEED to print percentage of matched tree of all trees in NYC. Also print percentages corresponding to each borough.
      
            
def treeInfo(entry):
    boros=['NYC','Manhattan', 'Queens', 'Bronx','Brooklyn','Staten Island']
    #match the user input string to common species names of trees column.
    #TreeInfo
    entry.lower()
    matched=[]
    for x in Tree_data['spc_common'].unique(): 
        TEXT = entry
        print(x)
       
        if (str(x) in TEXT):
            matched.append(x)
        else:
            continue
    freqa=freq(matched, boros)

def frequencies(trees,boroughs):
    freq = {
        'NYC':0,
        'Manhattan':0,
        'Queens':0,
        'Bronx':0,
        'Staten Island':0,
        'Brooklyn':0,
    }      
    for each in trees:
        freq['NYC']+=1
        if each['borough'] in boroughs:
            freq[each['borough']] +=1
    return freq

def nearby(input):
    pass
    
#Interactive loop that it is central control for the program
flag=True

while flag:
    print('** NYC TREE DATA Searcher **')
    userInput=input()
    if (userInput=='help'):
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
