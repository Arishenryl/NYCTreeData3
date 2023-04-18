data = read_data('nyctreedata.csv')
print('Welcome to the treequery program.')
print("To begin, try typing 'help' for the list of valid commands.\n")

while true: 
  command = input(' Enter a command: ')
  if command.lower() == 'help':
        print("Valid commands:")
        print("  treeinfo <tree_species_names>")
        print("    - Find information about one or more tree species")
        print("    - Example: treeinfo white oak")
        print("  quit")
        print("    - Quit the program")
    elif command.lower() == 'quit':
