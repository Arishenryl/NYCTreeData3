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

      elif command.startswith('treeinfo'):
        input_str = ' '.join(command.split()[1:])
        if input_str:
            species_names = parse_input(input_str)
            for species_name in species_names:
                results = compute_all_tree_info(data, species_name)
                if not results:
                    print("No matches found for '{}'".format(species_name))
                else:
                    print("Entry: {}".format(species_name))
                    for result in results:
                        print("Total number of such trees: {}".format(result['total']))
                        print("Zip codes in which this tree is found: {}".format(result['zip_codes']))
                        print("Borough containing the largest number of such trees: {}, with
{}".format(result['largest_borough'], result['largest_borough_count']))                
                        print("Average diameter: {:.2f}".format(result['avg_diameter']))
                    overall_results = compute_overall_tree_info(data)
