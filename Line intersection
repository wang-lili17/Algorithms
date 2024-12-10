def are_lines_intersecting(line1, line2):
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2
    
    
    d = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    
    if d == 0:
        return False  
    
    
    t = ((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3)) / d
    u = ((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) / d
    
  
    if 0 <= t <= 1 and 0 <= u <= 1:
        return True
    return False

line1 = [(5, 3), (8, 5)]
line2 = [(4, 2), (1, 5)]

result = are_lines_intersecting(line1, line2)
print("Lines intersect" if result else "Lines do not intersect")

2

def are_lines_intersecting(line1, line2):

    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2
    
    
    determinant = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    
    if determinant != 0:
        return True
    return False

line1= [(5, 3), (8, 5)] 
line2= [(4, 2), (1, 5)]

y=are_lines_intersecting(line1, line2)
print ("Lines intersect" if y else "Lines do not intersect")
