from collections import Counter
import linearAlgebra as la
import math

# Central Tendencies
def mean(x):
    return sum(x)/len(x)

def median(x):
    """finds the middle-most value of x"""
    n = len(x)
    sorted_x = sorted(x)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_x[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_x[lo] + sorted_x[hi]) / 2

def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [i for i, v in counts.items() if i == max_count]


# Dispersion
def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    x_bar = mean(x)
    return [i - x_bar for i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return la.sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))


# Correlation
