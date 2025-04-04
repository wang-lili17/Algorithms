def DAG_longest_path(graph,start):
  n=len(graph)
  topo_ordering=topological_ordering(graph)
  if topo_ordering is None:
    return None

  dist=[float("-inf")]*n
  dist[start]=0

  for u in topo_ordering:
    if dist[u]==float("-inf"):
      continue
    for v in range(n):
      if graph[u][v] == 1:
        dist[v] = max(dist[v], dist[u] + 1)

  return dist

from collections import deque

def topological_ordering(graph):
  n=len(graph)
  in_degree=[0]*n
  q=deque()
  for i in range(n):
    for j in range(n):
      if graph[i][j]==1:
        in_degree[j]+=1

  for i in range(n):
    if in_degree[i]==0:
      q.append(i)
  index=0
  order=[0]*n
  while q:
    a=q.popleft()
    order[index]=a

    for i in range(n):
      if graph[a][i]==1:
        in_degree[i]-=1
        if in_degree[i]==0:
          q.append(i)
    index+=1


  if index==n:
    return order
  else:
    return None

graph = [
    [0,0,1,1,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,1,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

start = 0
longest_distance = DAG_longest_path(graph,start)
print(longest_distance)


