# ============================================================
# Math for Machine Learning - Parts 1 to 5 (with tests)
# ------------------------------------------------------------
# Each function is implemented from scratch (no NumPy) and
# tested on the example from the assignment. Run with:
#   python parts_1_to_5.py
# ============================================================

import math


# ============================================================
# PART 1 - VECTORS (by hand)
# ============================================================

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


# ============================================================
# PART 2 - MATRICES (by hand)
# ============================================================

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


# ============================================================
# PART 3 - BASIC STATISTICS (by hand)
# ============================================================

# Return the mean (average) of a list of numbers.
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


# Return the median (middle value), handling an even count correctly.
def calculate_median(numbers):
    ordered = sorted(numbers)
    n = len(ordered)
    middle = n // 2
    if n % 2 == 1:                       # odd count -> single middle value
        return ordered[middle]
    else:                                # even count -> average of the two middle values
        return (ordered[middle - 1] + ordered[middle]) / 2


# Return the variance (the average of the squared differences from the mean).
def calculate_variance(numbers):
    mean_value = calculate_mean(numbers)
    squared_diffs = [(value - mean_value) ** 2 for value in numbers]
    return sum(squared_diffs) / len(numbers)


# Return the standard deviation (the square root of the variance).
def calculate_std(numbers):
    return math.sqrt(calculate_variance(numbers))


# ============================================================
# PART 4 - CORRELATION
# ============================================================

# Return Pearson's correlation coefficient between two lists (a value from -1 to 1).
def calculate_correlation(x, y):
    n = len(x)
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    # Covariance: average of the products of the paired differences from the means.
    covariance = 0
    for i in range(n):
        covariance += (x[i] - mean_x) * (y[i] - mean_y)
    covariance = covariance / n
    std_x = calculate_std(x)
    std_y = calculate_std(y)
    if std_x == 0 or std_y == 0:         # avoid division by zero
        return 0
    return covariance / (std_x * std_y)


# ============================================================
# PART 5 - INTRODUCTION TO PROBABILITY
# ============================================================

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


# ============================================================
# TESTS - run every part on its example from the assignment
# ============================================================

def test_part1():
    print("===== PART 1: VECTORS =====")
    v1 = [3, 4]
    v2 = [1, 2]
    print(f"v1 = {v1}, v2 = {v2}")
    print(f"vector_add(v1, v2)      = {vector_add(v1, v2)}       (by hand: [4, 6])")
    print(f"vector_subtract(v1, v2) = {vector_subtract(v1, v2)}       (by hand: [2, 2])")
    print(f"dot_product(v1, v2)     = {dot_product(v1, v2)}          (by hand: 3*1 + 4*2 = 11)")
    print(f"magnitude(v1)           = {magnitude(v1)}         (by hand: sqrt(9+16) = 5.0)")


def test_part2():
    print("\n===== PART 2: MATRICES =====")
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    print(f"m1 = {m1}, m2 = {m2}")
    print(f"matrix_add(m1, m2)      = {matrix_add(m1, m2)}   (by hand: [[6, 8], [10, 12]])")
    print(f"matrix_multiply(m1, m2) = {matrix_multiply(m1, m2)}   (by hand: [[19, 22], [43, 50]])")
    print(f"transpose(m1)           = {transpose(m1)}     (by hand: [[1, 3], [2, 4]])")


def test_part3():
    print("\n===== PART 3: STATISTICS =====")
    grades = [85, 90, 78, 92, 88, 76, 95]
    print(f"grades = {grades}")
    mean_value = calculate_mean(grades)
    median_value = calculate_median(grades)
    variance_value = calculate_variance(grades)
    std_value = calculate_std(grades)
    print(f"Mean               = {mean_value:.2f}")
    print(f"Median             = {median_value}")
    print(f"Variance           = {variance_value:.2f}")
    print(f"Standard Deviation = {std_value:.2f}")
    print("Meaning: the mean is the typical grade (~86); the median (88) is the middle grade;")
    print("a standard deviation of ~6.6 means the grades are fairly close to each other,")
    print("not widely spread out.")


def test_part4():
    print("\n===== PART 4: CORRELATION =====")
    study_hours = [1, 2, 3, 4, 5, 6]
    final_grade = [50, 55, 65, 70, 80, 85]
    r = calculate_correlation(study_hours, final_grade)
    print(f"study_hours = {study_hours}")
    print(f"final_grade = {final_grade}")
    print(f"correlation = {r:.4f}")
    print("Meaning: the value is very close to +1, so the relationship is very strong")
    print("and positive: the more hours a student studies, the higher the final grade.")


def test_part5():
    print("\n===== PART 5: PROBABILITY =====")
    # 1) A bag with 5 red and 3 blue balls -> probability of drawing red.
    red = 5
    blue = 3
    p_red = simple_probability(red, red + blue)
    print(f"P(red ball) = {red}/{red + blue} = {p_red:.3f}   (by hand: 0.625)")
    # 2) Tossing a coin twice, getting heads both times (two independent events).
    p_two_heads = independent_events([0.5, 0.5])
    print(f"P(two heads) = 0.5 * 0.5 = {p_two_heads:.3f}   (by hand: 0.25)")
    # 3) Of 100 students, 60 attended all lectures; of those 60, 54 passed.
    p_pass_given_attend = conditional_probability(54, 60)
    print(f"P(pass | attended) = 54/60 = {p_pass_given_attend:.3f}   (by hand: 0.9)")


if __name__ == "__main__":
    test_part1()
    test_part2()
    test_part3()
    test_part4()
    test_part5()
