import math
import numpy as np

def map_value(value, in_min, in_max, out_min, out_max):
    return np.interp(value, (in_min, in_max), (out_min, out_max))

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])
