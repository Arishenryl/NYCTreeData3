
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
    print(Tree_data['spc_common'].unique())
def treeInfo(entry):
    #match the user input string to common species names of trees column.
    #TreeInfo
    for x in Tree_data['spc_common'][0:10]:
        r = re.findall(f"\s{entry}",str(x))
        print(r)
        matched_status=bool(r)
        print("Tree:", x, "match:", matched_status)
        if matched_status:
            name=r
            tree_amount+=1
            print('Entry:', name)
            print('Total number of trees:', tree_amount)
    #TreeInfo
    
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
    elif (userInput=='treeinfo'):
        treeInfo(userInput)
        pass
    elif (userInput=='nearby'):
        #nearby()
        pass
    elif (userInput=='quit'):
        exit()
    else:
        print('Command not understood. Please enter valid command.')
        

        
#Species/Borough
df = pd.read_csv('nyctreedata.csv')
print(df.columns)

#prints species entry results
print(results)
