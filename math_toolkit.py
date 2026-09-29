# ============================================================
# math_toolkit.py
# ------------------------------------------------------------
# Your own small math library for Machine Learning, built from
# scratch (no NumPy). It gathers every function from Parts 1-5:
#   - Vectors
#   - Matrices
#   - Statistics
#   - Correlation
#   - Probability
# Import it with:  import math_toolkit as mt
# ============================================================

import math


# ----------------------------
# Vectors
# ----------------------------

# Add two vectors element by element and return the result.
def vector_add(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]


# Subtract vector v2 from v1 element by element.
def vector_subtract(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]


# Return the dot product (sum of the products of matching elements).
def dot_product(v1, v2):
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total


# Return the magnitude (length) of a vector: sqrt of sum of squares.
def magnitude(v):
    total = 0
    for value in v:
        total += value ** 2
    return math.sqrt(total)


# ----------------------------
# Matrices
# ----------------------------

# Add two matrices of the same size element by element.
def matrix_add(m1, m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result


# Multiply two matrices using the row-by-column rule (nested loops).
def matrix_multiply(m1, m2):
    rows_m1 = len(m1)
    cols_m1 = len(m1[0])
    cols_m2 = len(m2[0])
    result = []
    for i in range(rows_m1):
        row = []
        for j in range(cols_m2):
            cell = 0
            for k in range(cols_m1):
                cell += m1[i][k] * m2[k][j]
            row.append(cell)
        result.append(row)
    return result


# Return the transpose of a matrix (turn its rows into columns).
def transpose(m):
    rows = len(m)
    cols = len(m[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(m[i][j])
        result.append(new_row)
    return result


# ----------------------------
# Statistics
# ----------------------------

# Return the mean (average) of a list of numbers.
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


# Return the median (middle value), handling an even count correctly.
def calculate_median(numbers):
    ordered = sorted(numbers)
    n = len(ordered)
    middle = n // 2
    if n % 2 == 1:
        return ordered[middle]
    else:
        return (ordered[middle - 1] + ordered[middle]) / 2


# Return the variance (the average of the squared differences from the mean).
def calculate_variance(numbers):
    mean_value = calculate_mean(numbers)
    squared_diffs = [(value - mean_value) ** 2 for value in numbers]
    return sum(squared_diffs) / len(numbers)


# Return the standard deviation (the square root of the variance).
def calculate_std(numbers):
    return math.sqrt(calculate_variance(numbers))


# ----------------------------
# Correlation
# ----------------------------

# Return Pearson's correlation coefficient between two lists (a value from -1 to 1).
def calculate_correlation(x, y):
    n = len(x)
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    covariance = 0
    for i in range(n):
        covariance += (x[i] - mean_x) * (y[i] - mean_y)
    covariance = covariance / n
    std_x = calculate_std(x)
    std_y = calculate_std(y)
    if std_x == 0 or std_y == 0:
        return 0
    return covariance / (std_x * std_y)


# ----------------------------
# Probability
# ----------------------------

# Return the probability of a simple event (favorable outcomes / total outcomes).
def simple_probability(favorable, total):
    return favorable / total


# Return the probability of several independent events all happening (product of their probabilities).
def independent_events(probabilities):
    result = 1
    for probability in probabilities:
        result *= probability
    return result


# Return the conditional probability P(A | B) = count of (A and B) / count of B.
def conditional_probability(count_a_and_b, count_b):
    return count_a_and_b / count_b
