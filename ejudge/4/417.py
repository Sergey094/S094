import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1
a = dx*dx + dy*dy

# Коэффициенты квадратного уравнения At^2 + Bt + C = 0
b = 2*(x1*dx + y1*dy)
c = x1*x1 + y1*y1 - r*r

disc = b*b - 4*a*c

if disc <= 0:
    # Нет пересечения или касание в одной точке
    if x1*x1 + y1*y1 <= r*r and x2*x2 + y2*y2 <= r*r:
        length = math.hypot(dx, dy)
    else:
        length = 0.0
else:
    sqrt_disc = math.sqrt(disc)
    t1 = (-b - sqrt_disc)/(2*a)
    t2 = (-b + sqrt_disc)/(2*a)
    t_start = max(0.0, min(t1, t2))
    t_end = min(1.0, max(t1, t2))
    if t_start > t_end:
        length = 0.0
    else:
        x_start = x1 + dx*t_start
        y_start = y1 + dy*t_start
        x_end = x1 + dx*t_end
        y_end = y1 + dy*t_end
        length = math.hypot(x_end - x_start, y_end - y_start)

print(f"{length:.10f}")