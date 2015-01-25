#!/usr/bin/env python3

mothers = []

class Node:
  def __init__(self, name, daughters=[]):
    self.name = name
    self.daughters = daughters 
    self.mothers = []

  def print_tree(self):
    print(self.name)
    for daughter in self.daughters:
      daughter.print_tree()

  def is_mother(self,relative):
    if self.name == relative:
      return True
    else:
      for daughter in self.daughters:
        if daughter.is_mother(relative):
          return True
        else:
          continue

  def find_closest_antecedent(self, relatives):
    global mothers
    if self.is_mother(relatives[0]) and self.is_mother(relatives[1]):
      mothers.append(self.name)
      for daughter in self.daughters:
        daughter.find_closest_antecedent(relatives)

i = int(input())

nodes = []
for line in range(i):
  names = input()
  names = names.strip().split(',')
  daughters = []
  for daughter in names[1:]:
    daughters.append(Node(daughter))
  node = Node(names[0],daughters)
  nodes.append(node)

nodes_to_remove = []
for j in range(len(nodes)):
  for i in range(len(nodes)):
    for daughter in range(len(nodes[i].daughters)):
      if nodes[j].name == nodes[i].daughters[daughter].name:
        nodes[i].daughters[daughter] = nodes[j]
        nodes_to_remove.append(nodes[j])

for i in range(len(nodes_to_remove)):
  nodes.remove(nodes_to_remove[i])

find_antecedent = input()
find_antecedent = find_antecedent.strip().split(',')

if find_antecedent[0] == find_antecedent[1]:
  print(find_antecedent[0])
else:
  nodes[0].find_closest_antecedent(find_antecedent)
  print(mothers[-1])

