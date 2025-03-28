def orientation(p, q, r):
    det = (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])
    if det == 0:
        return 0
    return 1 if det > 0 else -1

def distance(p, q):

    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

def graham_scan(points):

    points.sort(key=lambda p: (p[1], p[0]))
    pivot = points[0]
    
    points = sorted(points[1:], key=lambda p: (orientation(pivot, (pivot[0] + 1, pivot[1]), p), -distance(pivot, p)))

    points.insert(0, pivot)
    
    stack = points[:2]
    for i in range(2, len(points)):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], points[i]) <= 0:
            stack.pop()
        stack.append(points[i])
    
    return stack

points = [(0, 0), (1, 1), (2, 2), (3, 0), (0, 3), (3, 3)]
convex_hull = graham_scan(points)
print("Convex Hull:", convex_hull)
