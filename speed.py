def speed_count(distance,time):
    speed = distance/time
    print(f"{speed:.2f}")
    return speed

import math

def triangle_calc(a, b):
    c = math.sqrt(math.pow(a,2)+math.pow(b, 2))
    print(f"przeciwprostokatna wynosi {c:.2f}")
    return c