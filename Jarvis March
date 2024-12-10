def cross_product(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

def jarvis_march(points):

    start = min(points, key=lambda point: (point[1], point[0]))
    convex_hull = []
    
    current_point = start
    while True:
        convex_hull.append(current_point)
        next_point = points[0] 
        
        for candidate in points:
            if candidate == current_point:
                continue
            if cross_product(current_point, next_point, candidate) > 0:  
                next_point = candidate
        
        current_point = next_point
        if current_point == start:
            break
    
    return convex_hull


points = [(0, 0), (2, 1), (1, 2), (2, 3), (3, 0), (3, 3), (4, 1)]
convex_hull = jarvis_march(points)
print("Convex Hull:", convex_hull)
