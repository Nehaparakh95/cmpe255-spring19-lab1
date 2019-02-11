import statistics
from fractions import Fraction as fr


def mean_num_friends(x):
    return sum(x) / len(x)


def median_num_friends(x):
    x.sort()

    # Find the median.
    length = len(x)
    if (length % 2 == 0):
        median = (x[(length) // 2] + x[(length) // 2 - 1]) / 2
    else:
        median = x[(length - 1) // 2]

    # Display the result.
    return median


num_friends = [100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print(mean_num_friends(num_friends))

print(median_num_friends(num_friends))