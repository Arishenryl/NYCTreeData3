#NYC Tree Census Data 2015
#author @Liann Aris-Henry, @Aida Lita, @Gabriel Stewart-Guido
#To answer specific questions end-users may have about the NYC tree data by utilizing several original functions to organize and pull the necessary data from the CSV.
#date May 14th 2023
#Version #2 (file-reader error fixed and debugged)
#!/usr/bin/env python3
import csv
import math
import sys


# A function to get frequencies of the trees.
# in each borough.
def get_frequencies(trees, boroughs):
   frequencies = {
       'NYC': 0,
       'Manhattan': 0,
       'Bronx': 0,
       'Brooklyn': 0,
       'Queens': 0,
       'Staten Island': 0
   }
   for tree in trees:
       frequencies['NYC'] += 1
       if tree['borough'] in boroughs:
           frequencies[tree['borough']] += 1
   return frequencies
# A function to get the total number of trees in each borough.
def get_total_trees(trees):
   totals = {
       'NYC': 0,
       'Manhattan': 0,
       'Bronx': 0,
       'Brooklyn': 0,
       'Queens': 0,
       'Staten Island': 0
   }
   for tree in trees:
       totals['NYC'] += 1
       if tree['borough'] in totals:
           totals[tree['borough']] += 1
   return totals
# A helper function to get the zip codes in which a certain tree species can be found.
def get_zip_codes(trees):
   zip_codes = []
   for tree in trees:
       if tree['postcode'] not in zip_codes:
           zip_codes.append(tree['postcode'])
   return zip_codes

# Calculation function to compute the distance between two points
# given their latitude and longitude. Uses math library.
def haversine(lat1, lon1, lat2, lon2):
   R = 6371 # Radius of the earth in km
   dLat = math.radians(lat2 - lat1)
   dLon = math.radians(lon2 - lon1)
   a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
   c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
   d = R * c # Distance in km
   return d
# A helper function to get the borough containing the largest number of a certain tree species.
def get_largest_borough(frequencies):
   largest_borough = None
   largest_freq = 0
   for borough in frequencies:
       if frequencies[borough] > largest_freq and borough!='NYC':
           largest_freq = frequencies[borough]
           largest_borough = borough
   return (largest_borough, largest_freq)
# A function to match the tree species to the user's input.
def get_matching_species(trees, name):
   matching_trees = []
   for tree in trees:
       if name.lower() in tree['spc_common'].lower():
           matching_trees.append(tree)
   return matching_trees
#Function to get all trees within a certain distance from a certain location.
def get_nearby_trees(trees, lat, lon, dist):
   nearby_trees = []
   for tree in trees:
       if haversine(float(tree['latitude']), float(tree['longitude']), lat, lon) <= dist:
           nearby_trees.append(tree)
   return nearby_trees
#Function to get the unique tree species within a certain distance from a certain location.
def get_unique_nearby_trees(trees):
   unique_trees = []
   for tree in trees:
       if tree['spc_common'] not in unique_trees:
           unique_trees.append(tree['spc_common'])
   return unique_trees
#Function to get the frequency of each tree species within a certain distance from a certain location.
def get_nearby_frequencies(trees):
   frequencies = {}
   for tree in trees:
       if tree['spc_common'] in frequencies:
           frequencies[tree['spc_common']] += 1
       else:
           frequencies[tree['spc_common']] = 1
   return frequencies
# Main function.
def main():
    trees = []
   
#ERROR CHECKING
    if len(sys.argv) < 2:
        print("Error: No filename provided")
        sys.exit(1)

    #Attempt to open the file
    try:
        with open(sys.argv[1], newline='') as csvfile:
            # Check if file is a CSV
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                trees.append(row)
    except FileNotFoundError:
        print("Error: File not found or is not a CSV file.")
        sys.exit(1)
    
    
   # Welcome message.
    print('Welcome to the treequery program.')
    print('To begin, try typing \'help\' for the list of valid commands.')
    # Interactive loop.
    while True:
       command = input('\nEnter a command: ')
       # Help command.
       if command == 'help':
           print('\nThe valid commands are as follows:')
           print('listtrees - Get a list of common tree names')
           print('treeinfo <tree_species_name> - Get information about a species of tree')
           print('nearby <latitude> <longitude> <distance> - Get a list of information of all trees within a defined distance from some location')
           print('help - Get a help page about each command')
           print('quit - Quit the application')
            
       #List trees command.
       elif command == 'listtrees':
           unique_trees = []
           for tree in trees:
               if tree['spc_common'] not in unique_trees:
                   unique_trees.append(tree['spc_common'])
           unique_trees.sort()
           print('\n' + '\n'.join(unique_trees) + '\n')
            
       # Tree info command.
       elif command.startswith('treeinfo'):
           boroughs=['Manhattan', 'Bronx', 'Brooklyn','Queens','Staten Island']
           name = command.split(' ')[1]
           matching_trees = get_matching_species(trees, name)
           if len(matching_trees) > 0:
               total_num = len(matching_trees)
               zip_codes = get_zip_codes(matching_trees)
               borough= get_largest_borough(get_frequencies(matching_trees, boroughs))
            
               print('\nEntry: ' + name)
               print('Total number of such trees: ' + str(total_num))
               print('Zip codes in which this tree is found: ' + ', '.join(zip_codes))
               print('borough containing the largest number of such trees: ' + borough[0] + ', with ' + str(borough[1]))

               print('Popularity in NYC:')
               frequencies= get_frequencies(trees, boroughs)
               totals= get_total_trees(trees)
               #Get the value from the frequencies, and then divide by the total and *100

               frequencies = {
                    'NYC': 0,
                    'Manhattan': 0,
                    'Bronx': 0,
                    'Brooklyn': 0,
                    'Queens': 0,
                    'Staten Island': 0
                }
               
               for borough in boroughs:
                  tree_count=0
                  total=0
                  for tree in trees:
                      if tree['borough']==borough:
                          tree_count+=1
                      else:
                          total+=1
                  print(f"{borough}:{tree_count}({total}) {round(tree_count/total*100)}%")
                    
                    
           else:
               print('\nNo matching species found.\n')
       # Nearby command.
       elif command.startswith('nearby'):
           args = command.split(' ')
           if len(args) == 4:
               lat = float(args[1])
               lon = float(args[2])
               dist = float(args[3])
               nearby_trees = get_nearby_trees(trees, lat, lon, dist)
               if len(nearby_trees) > 0:
                   unique_trees = get_unique_nearby_trees(nearby_trees)
                   frequencies = get_nearby_frequencies(nearby_trees)
                   total_trees = get_total_trees(trees)
                   for tree in unique_trees:
                       freq = (frequencies[tree] / total_trees['NYC']) * 100
                       print('\n' + tree + ': ' + '%.2f' % freq + '%')
               else:
                   print('\nNo trees are present within this distance.\n')
           else:
               print('\nPlease enter the required arguments to use the nearby command. Use the \'help\' command to learn more details.\n')
       # Quit command.
       elif command == 'quit':
           print('\nGoodbye!\n')
           break
       # Invalid command.
       else:
           print('\nInvalid command. Please try again.\n')
if __name__ == '__main__':
   main()
