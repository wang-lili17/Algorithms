def cross_product(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

def jarvis_march(points):
    start = min(points, key=lambda p: (p[1], p[0]))
    
    hull = []
    p = start
    
    while True:
        
        hull.append(p)
        q = points[0]
        
        for r in points:
            if r == p:
                continue

            if q == p or cross_product(p, q, r) > 0: 
                q = r

        if q == start:
            break

        p = q
    
    return hull

points = [(0, 0), (1, 1), (2, 2), (2, 0), (0, 2), (3, 3), (1, 2)]
hull = jarvis_march(points)
print("Convex Hull:", hull)
