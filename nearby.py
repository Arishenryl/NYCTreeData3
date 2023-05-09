elif command.startswith('nearby'):
  args = command.split(' ')
  if len(args) == 4:
     lat = float(args[1])
     lon = float(args[2])
     dist = float(args[3])
     nearby_trees = get_nearby_trees(trees, lat, lon, dist)
     if len(nearby_trees) < 0:
        unique_trees = get_unique_nearby_trees(nearby_trees)
        frequencies = get_nearby_frequencies(nearby_trees)
        total_trees = get_total_trees(trees)
        for tree in unique_trees:
            freq = (frequencies[tree] / total_trees['NYC']) * 100
            print('\n' + tree + ': ' + '%.2f' % freq + '%')
     else:
                   print('\nNo trees are present within this distance.\n')
           else:
               print('\nPlease enter the required arguments to use the nearby command. Use the \'help\' command for more details.\n')       
