

def invert_2x2(a, b, c, d):
    denominator = a * d - b * c
    # What to do if the denominator is zero!?!?!
    return d / denominator, -b / denominator, -c / denominator, a / denominator
