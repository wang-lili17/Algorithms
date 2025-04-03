def Bellman_Ford(graph,v,source):
  D=[float("inf")]*v
  D[source]=0
  for i in range(v-1):
    for u,v_vertex,w in graph:
      if D[u]!=float("inf") and D[u]+w<D[v_vertex]:
        D[v_vertex]=D[u]+w

  negative_affected_nodes=[False]*v
  for u,v_vertex,w in graph:
    if D[u]!=float("inf") and D[u]+w<D[v_vertex]:
      negative_affected_nodes[v_vertex]=True
  for i in range(v-1):
    for u,v_vertex,w in graph:
      if negative_affected_nodes[u]:
        negative_affected_nodes[v_vertex]=True

    result=[]
    for i in range(len(D)):
      if negative_affected_nodes[i]:
        result.append("Negative cycle")
      else:
        result.append(D[i])
    return result


v = 10
source = 0
graph = [
    [0, 1, 5], [1, 2, 20], [1, 5, 30], [1, 6, 60],
    [2, 3, 10], [2, 4, 75], [3, 2, -15], [4, 9, 100],
    [5, 4, 25], [5, 6, 5], [5, 8, -50], [6, 7, 50], [7, 8, -10]
]
answer=Bellman_Ford(graph,v,source)
print(answer)