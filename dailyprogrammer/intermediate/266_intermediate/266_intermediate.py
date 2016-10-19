import itertools, math

# INCOMPLETE SOLUTION, DO NOT ATTEMPT TO RUN

class Node:
  def __init__(self, n_id, connected_to):
    self.connected_to = connected_to
    self.n_id = n_id

  def add_connection(self, node):
    if node not in self.connected_to:
      self.connected_to.append(node)
      #node.add_connection(self)

  def connections(self):
    return self.connected_to

  def distance_to_all_nodes(self, searched_list, current_weight = 0):
    # Include the starting node in the "already seen" list
    if self not in searched_list:
      searched_list.append(self)

    end = []

    # There are edge cases when a node is the "end point"
    if len(self.connected_to) == 0:
      end.append(current_weight)

    # Otherwise, search and check according to the "already seen" list
    for node in self.connected_to:
      if node in searched_list:
        end.append(current_weight)
      else:
        # Since this method returns an array, .extend is used as to not have multi-dimensional arrays
        end.extend(node.distance_to_all_nodes(searched_list + [node], current_weight + 1))

    return end

  def __str__(self):
    return "[ID#{}] Connected: {}".format(self.n_id, ', '.join([str(i.n_id) for i in self.connected_to]))
  __repr__ = __str__

with open('./input') as f:
  # Read input
  lines = f.read().splitlines()

  # Calculate baseline data
  node_count = int(lines[0])
  node_conns = lines[1:]

  # Generate empty nodes
  nodes = [Node(i+1, []) for i in range(0, node_count)]

  # Start filling in connections for empty nodes
  for line in node_conns:
    f, t = [int(index) for index in line.split()]
    nodes[f - 1].add_connection(nodes[t - 1])

  # Filter out any unused nodes
  nodes = list(filter(lambda x: len(x.connected_to) != 0, nodes))

  values = [node.distance_to_all_nodes([]) for node in nodes]
  filtered_values = list(filter(lambda x: all(val != 0 for val in x), values))
  print(filtered_values)

  
  #nodes = [[int(coord) for coord in node.split()] for node in lines[1:]]
  
  # Logic portion

