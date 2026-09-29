# Math Toolkit for Machine Learning

A small math library built **from scratch in pure Python** (no NumPy),
covering the math foundations for Machine Learning: vectors, matrices,
statistics, correlation, and probability. It ends with an integrated project
that applies the library to analyze 10 students' performance.

All code was **executed and verified** in a local Python 3.12 environment, and
every function was checked against a by-hand calculation.

## Topics Covered

- **Vectors:** add, subtract, dot product, magnitude
- **Matrices:** add, multiply (row × column), transpose
- **Statistics:** mean, median, variance, standard deviation
- **Correlation:** Pearson correlation coefficient
- **Probability:** simple event, independent events, conditional probability

## Project Structure

```
math-toolkit/
├── README.md              # this file
├── parts_1_to_5.py        # Parts 1–5 solutions, each tested vs. a hand calculation
├── math_toolkit.py        # the organized library (all functions gathered)
├── students_analysis.py   # Part 6: integrated project on 10 students
├── REPORT.md              # short report interpreting the results (Arabic)
└── .gitignore
```

## How to Run

```bash
python parts_1_to_5.py
python students_analysis.py
```

## Verified Results

### Parts 1–5 (matches by-hand math)

| Function | Example | Result |
|----------|---------|--------|
| `vector_add([3,4],[1,2])` | | `[4, 6]` |
| `dot_product([3,4],[1,2])` | | `11` |
| `magnitude([3,4])` | | `5.0` |
| `matrix_multiply([[1,2],[3,4]],[[5,6],[7,8]])` | | `[[19,22],[43,50]]` |
| `calculate_mean([85,90,78,92,88,76,95])` | | `86.29` |
| `calculate_std(...)` | | `6.56` |
| `calculate_correlation([1..6],[50,55,65,70,80,85])` | | `0.9954` |
| `simple_probability(5, 8)` | red ball | `0.625` |
| `independent_events([0.5,0.5])` | two heads | `0.25` |
| `conditional_probability(54, 60)` | P(pass \| attend) | `0.9` |

### Part 6 — Student analysis (10 students)

| Metric | Value |
|--------|-------|
| Mean grade | 72.60 |
| Median grade | 72.5 |
| Std deviation | 12.96 |
| Correlation (hours vs grade) | 0.9991 |
| Passed (grade > 60) | 8 / 10 |
| P(random student passed) | 0.80 |

**Conclusion:** studying more hours is very strongly linked to a higher final
grade (correlation ≈ 1.0). See `REPORT.md` for the full interpretation.
