import sys
import csv
import math

def getHelp():
    
#beginning of help command file; basically a "man" page
    print ("listtrees: can help one get a list of common tree names.")
#treeinfo command help file description
    print ("treeinfo: can get information about a species of tree. One input argument is required to run the code.")
#nearby command help  file description 
    print ("nearby: can get a list of information of all trees within a defined distance from some location. Various input arguments are required to run the code.")
#how to quit the help command application
    print ("quit: command quits the application.")



def haversine(lat1,lon1,lat2,lon2):
    Earth_radius = 6371
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1))*math.cos(math.radians(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = Earth_radius * c  #Distance
    return distance

#Function for getting amount of trees in each borough

def totals(trees):
    #TOTALS
    total_counts = {
        'NYC':0,
        'Manhattan':0,
        'Queens':0,
        'Bronx':0,
        'Staten Island':0,
        'Brooklyn':0,
    } 
    for each in trees:
        total_counts['NYC'] += 1
        if each['borough'] in total_counts:
            total_counts[each['borough']] += 1
    return totals

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

# A function for getting te zip codes in which a certain tree species can be found.

def get_zipcodes(trees):
    zip_list=[]
    for tree in trees:
        if tree['zip_city'] not in zip_list:
            zip_list.append(tree['zip_city'])
        
    return zip_list

#Get average diameter of a certain tree species

def find_avgDiameter(trees):
    sum=0
    for tree in trees:
        sum+=float(tree['diameter'])

    return sum/len(trees)

#A function to get the borough which contains the largest number of a ceratin tree
def top_boro(frequencies):
    top_boro= None
    top_freq= 0
    for borough in frequencies:
        if frequencies[borough] > top_freq:
            top_freq=frequencies[borough]
            top_boro=borough
        return (top_boro,top_freq)

#A function to identify the trees that match to the user inputted string.
def MatchInput(trees, name):
    matched=[]
    for tree in trees:
        if name.lower() in tree['spc_common'].lower():
            matched.append(tree)
    
    return matched

#A function to get all trees within a certain distance from a certain location.

def find_nearby(trees, lat,lon, dist):
    trees_nearby = []
    for tree in trees:
        if haversine(float(tree['latitude']),float(tree['longitude']),lat,lon)<=dist:
            trees_nearby.append(tree)
    return trees_nearby

#A helper function to get the UNIQUE LIST OF species within a certain distance from a certain location.

def find_unique_nearby(trees):
    unique_trees=[]
    for tree in trees:
        if tree['spc_common'] not in unique_trees:
            unique_trees.append(tree['spc_common'])
    return unique_trees

def find_nearby_freqs(trees):
    frequencies={}
    for tree in trees:
        if tree['spc_common'] in frequencies:
            frequencies[tree['spc_common']]+=1
        else:
            frequencies[tree['spc_common']]+=1
    return frequencies

def main():
    #Take commad line argument
    file = sys.argv[1]
    #Create trees list --> Use pandas read_csv() to read every row into the 'trees' list.
    trees=[]
    with open(file) as csv_file:
        csv_reader= csv.DictReader(csv_file)
        for row in csv_reader:
            trees.append(row)
    
    print("#########################\nNYC TREE DATA SEARCH\n#########################")
    flag=True
    while flag:
        command=input('Enter a command:')
        if (command=='help'):
            getHelp() #command to display information about each command

        elif (command=='listtrees'):
            unique_trees=[]
            for tree in trees:
                if tree['spc_common'] not in unique_trees:
                    unique_trees.append(tree['spc_common'])
            unique_trees.sort()
            print(unique_trees)

        elif (command.startswith('treeinfo')):
            name = command.split(" ")[1]
            matched=MatchInput(trees, name)
            if len(matched)>0:
                total=len(matched)
                zipcodes= get_zipcodes(matched)
                boroughs = top_boro(frequencies(matched, boroughs))
                avg_diameter= find_avgDiameter(matched)


                #Code to output the info to the display ( in the console )
                print('\nENTRY:',name)
                print('\nTOTAL # of matched trees:',str(total))
                print('\nZIP CODES in which the tree can be found:'+ ','.join(zipcodes))
                print('\nBOROUGH containing largest number of trees:', boroughs[0], 'with', boroughs[1])
                print(f'\nAverage diameter: {round(avg_diameter,2)}')
            else:
                print('\nNO MATCHES FOUND :(')


        elif (command.startswith('nearby')):
            args = command.split(' ')
            if len(args)==4:
                lat = float(args[1])
                lon = float(args[2])
                dist =float(args[3])
                nearby=find_nearby(trees,lat,lon,dist)
                if len(nearby)>0:
                    unique_trees=find_unique_nearby(trees, lat,lon,dist)
                    freqs=find_nearby_freqs(nearby)
                    total_trees=totals(trees)
                    for tree in unique_trees:
                        frequency=(frequencies[tree]/total_trees['NYC'] * 100)

                        print('\nTree:', round(frequency,2))
                else:
                    print('No trees are present this area.')
            else:
                print('You typed something wrong or something is missing. Please try again. Type help for details.')
        
        elif (command.lower() == 'quit' or 'stop'):
            print('Exiting program...')
            exit()
        else:
            print('\nINVALID COMMAND. Try again or try help page by typing: help')
if __name__ == '__main__':
    main()





        
  
