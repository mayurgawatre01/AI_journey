import pandas as pd

marks = {
    'Maths': [15, 17, 6, 14, 19],
    'English': [20, 20, 12, 13, 18],
    'Science': [15, 7, 16, 20, 9]
}
marks_df = pd.DataFrame(marks)
print(marks_df)

print(marks_df["Maths"])