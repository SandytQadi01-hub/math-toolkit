# ============================================================
# students_analysis.py  -  PART 6: Integrated Project
# ------------------------------------------------------------
# Uses the math_toolkit library on real-looking data for 10
# students (name, weekly study hours, final grade) and prints
# the results as a table plus a short analysis.
# Run with:  python students_analysis.py
# ============================================================

import math_toolkit as mt

# Sample data for 10 students: (name, weekly study hours, final grade).
students = [
    ("Sara",   1, 52),
    ("Omar",   2, 58),
    ("Lina",   3, 61),
    ("Khalid", 4, 65),
    ("Huda",   5, 70),
    ("Yousef", 6, 75),
    ("Nour",   7, 80),
    ("Tariq",  8, 84),
    ("Rana",   9, 88),
    ("Faisal", 10, 93),
]

PASS_MARK = 60

# Separate the data into simple lists so the toolkit can use them.
study_hours = [student[1] for student in students]
final_grades = [student[2] for student in students]


# Print the students data as a clean table.
def print_students_table():
    print("=" * 45)
    print(f"{'Name':<10}{'Study Hours':<15}{'Final Grade':<12}")
    print("=" * 45)
    for name, hours, grade in students:
        status = "Pass" if grade > PASS_MARK else "Fail"
        print(f"{name:<10}{hours:<15}{grade:<12}{status}")
    print("=" * 45)


# Run the full Part 6 analysis using the math toolkit.
def main():
    print("PART 6 - INTEGRATED PROJECT: Student Performance Analysis\n")
    print_students_table()

    # 1) Mean and standard deviation of the grades.
    mean_grade = mt.calculate_mean(final_grades)
    std_grade = mt.calculate_std(final_grades)
    median_grade = mt.calculate_median(final_grades)

    # 2) Correlation between study hours and grades.
    correlation = mt.calculate_correlation(study_hours, final_grades)

    # 3) Probability that a random student from the list passed (grade > 60).
    passed_count = 0
    for grade in final_grades:
        if grade > PASS_MARK:
            passed_count += 1
    probability_pass = mt.simple_probability(passed_count, len(final_grades))

    print("\n----- RESULTS -----")
    print(f"Average grade (mean)         : {mean_grade:.2f}")
    print(f"Median grade                 : {median_grade}")
    print(f"Standard deviation of grades : {std_grade:.2f}")
    print(f"Correlation (hours vs grade) : {correlation:.4f}")
    print(f"Students who passed          : {passed_count} out of {len(final_grades)}")
    print(f"P(random student passed)     : {probability_pass:.2f}")

    print("\n----- SHORT REPORT -----")
    print(f"On average, students scored about {mean_grade:.0f}, and the grades are spread")
    print(f"by roughly {std_grade:.0f} points around that average, so performance is fairly varied.")
    print(f"The correlation between weekly study hours and the final grade is {correlation:.2f},")
    print("which is very strong and positive: students who studied more clearly scored higher.")
    print(f"Finally, {probability_pass * 100:.0f}% of the students passed, so a randomly chosen")
    print(f"student has a {probability_pass:.2f} probability of being a passing student.")


if __name__ == "__main__":
    main()
