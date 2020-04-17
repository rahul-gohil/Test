from point import points
from line  import Line, lines

triangles = []

class Triangle:
    
    def __init__(self, line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        
def makeTriangles(n):
    for i in range(1, n):
        triangles.append(Triangle(
            triangles[i - 1].line2,
            Line(points[i - 1], points[i]),
            lines[i]
        ))
        
def limitizeTriangle():
    for i in range(2, len(triangles) - 1):
        a = triangles[i + 1].line1.length() /\
            triangles[i].line1.length()
        b = triangles[i + 1].line2.length() /\
            triangles[i].line2.length()
        c = triangles[i + 1].line3.length() /\
            triangles[i].line3.length()
        if a == b and b == c:
            print(
                'Converged to Similarity between Triangles',
                'in Iteration', i
            )
            break
    else:
        print('Did not converge to similarity')
