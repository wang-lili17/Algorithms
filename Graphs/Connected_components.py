def DFS_component(A,start,visited):
  visited[start]=True
  stack=[start]
  component=[]

  while stack:
    current=stack.pop()
    component.append(current)

    for neighbor in range(len(A[current])):
      if A[current][neighbor]==1 and not visited[neighbor]:
        visited[neighbor]=True
        stack.append(neighbor)

  return component

def find_connected_components(A):
    visited = [False] * len(A)
    components = []

    for node in range(len(A)):
        if not visited[node]:
            component = DFS_component(A, node, visited)
            components.append(component)

    return components

graph = [
  [0, 1, 0, 0, 0, 0],
  [1, 0, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 1],
  [0, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0]
]

components = find_connected_components(graph)
print("Connected Components:", components)
