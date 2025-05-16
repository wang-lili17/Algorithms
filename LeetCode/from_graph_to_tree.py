A = [
  [0,1,0,1,0],
  [1,0,1,1,1],
  [0,1,0,0,1],
  [1,1,0,0,1],
  [0,1,1,1,0]
]

# A=[[0,0,0,0,0,0,0,1,0,1,0,1,0],
#    [0,0,0,0,0,0,0,0,1,0,1,0,0],
#    [0,0,0,1,0,0,0,0,0,0,0,0,1],
#    [0,0,1,0,1,0,0,1,0,0,0,0,0],
#    [0,0,0,1,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,1,0,0,0,0,0],
#    [0,0,0,0,0,1,0,1,0,0,0,0,0],
#    [1,0,0,1,0,0,1,0,0,0,0,1,0],
#    [0,1,0,0,0,0,0,0,0,1,0,0,1],
#    [1,0,0,0,0,0,0,0,1,0,1,0,0],
#    [0,1,0,0,0,0,0,0,0,1,0,0,0],
#    [1,0,0,0,0,0,0,1,0,0,0,0,0],
#    [0,0,1,0,0,0,0,0,1,0,0,0,0]
#    ]

def from_graph_to_tree(A,start):
  n=len(A)
  visited=[False]*n
  visited[start]=True
  stack=[start]
  tree_nodes=set()
  tree_edges=[]

  while stack:
    current=stack.pop()
    tree_nodes.add(current)
    for neighbor in range(n):
      if A[current][neighbor] and not visited[neighbor]:
        visited[neighbor]=True
        stack.append(neighbor)
        tree_nodes.add(neighbor)
        tree_edges.append((current,neighbor))
  return tree_nodes,tree_edges

nodes, edges= from_graph_to_tree(A, start=4)
print("Tree Nodes:", nodes)
print("Tree Edges:", edges)
