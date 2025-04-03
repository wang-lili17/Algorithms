from collections import deque


def dungeonproblem(A, start, end):
    rows, cols = len(A), len(A[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if A[start[0]][start[1]] == '*' or A[end[0]][end[1]] == '*':
        return "Invalid start or end position. One of them is a stone."

    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1])])
    visited[start[0]][start[1]] = True

    while queue:
        r, c = queue.popleft()
        print(r, c, end=',')

        if (r, c) == end:
            return "Path found!"

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and A[nr][nc] != '*':
                queue.append((nr, nc))
                visited[nr][nc] = True

    return "No valid path found."


A = [
    ['0', '0', '*', '0'],
    ['*', '0', '*', '0'],
    ['0', '0', '0', '0'],
    ['0', '*', '0', '*']
]

start = (0, 0)
end = (2, 3)

print(dungeonproblem(A, start, end))