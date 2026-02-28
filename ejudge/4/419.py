import math
import sys

# Read input
R = float(sys.stdin.readline())
Ax, Ay = map(float, sys.stdin.readline().split())
Bx, By = map(float, sys.stdin.readline().split())

# Distances
OA = math.hypot(Ax, Ay)
OB = math.hypot(Bx, By)
AB = math.hypot(Ax - Bx, Ay - By)

# Distance from center to segment AB
# If segment crosses circle interior → need arc path
def dist_point_to_segment(px, py, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        return math.hypot(px - x1, py - y1)

    t = ((px - x1)*dx + (py - y1)*dy) / (dx*dx + dy*dy)
    t = max(0.0, min(1.0, t))

    closest_x = x1 + t*dx
    closest_y = y1 + t*dy

    return math.hypot(px - closest_x, py - closest_y)


d = dist_point_to_segment(0, 0, Ax, Ay, Bx, By)

# Case 1: straight path is valid
if d >= R - 1e-12:
    print("{:.10f}".format(AB))
    sys.exit()

# Case 2: path touches circle

# Tangent lengths
tA = math.sqrt(OA*OA - R*R)
tB = math.sqrt(OB*OB - R*R)

# Angle between OA and OB
cos_phi = (OA*OA + OB*OB - AB*AB) / (2*OA*OB)
cos_phi = max(-1.0, min(1.0, cos_phi))
phi = math.acos(cos_phi)

# Tangent angles
alpha = math.acos(R / OA)
beta = math.acos(R / OB)

# Arc angle
theta = phi - alpha - beta

# Total length
answer = tA + tB + R * theta

print("{:.10f}".format(answer))