def floydwarshall(A):
    n = len(A)
    dp = [[A[i][j] for j in range(n)] for i in range(n)]
    next_node = [[-1 if A[i][j] == float("inf") else j for j in range(n)] for i in range(n)]
    for i in range(n):
        if A[i][i] != float("inf"):
            next_node[i][i] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] != float("inf") and dp[k][j] != float("inf"):
                    if dp[i][j] > dp[i][k] + dp[k][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]
                        next_node[i][j] = next_node[i][k]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] != float("inf") and dp[k][j] != float("inf") and dp[k][k] < 0:
                    dp[i][j] = float("-inf")
                    next_node[i][j] = -1

    return dp, next_node


def getPath(next_node, u, v):
    if next_node[u][v] == -1:
        return []

    path = [u]
    while u != v:
        u = next_node[u][v]
        if u == -1:
            return []
        path.append(u)

    return path


A = [
    [0, 4, 1, 9],
    [3, 0, 6, 11],
    [4, 1, 0, 2],
    [6, 5, 4, 0]

]
distances, next_matrix = floydwarshall(A)
print("Shortest distances:")
for row in distances:
    print(row)
print("Next nodes:")
for row in next_matrix:
    print(row)

source = 0
destination = 3
path = getPath(next_matrix, source, destination)
print("Shortest path", path)

has_negative_cycle = any(distances[i][i] < 0 for i in range(len(A)))
print("Graph contains negative cycles:", has_negative_cycle)
