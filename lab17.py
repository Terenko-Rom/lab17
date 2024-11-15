import pandas as pd
import csv
matrix = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [9, 2, 2, 8],
    [1, 3, 3, 7]
]
with open('massiv.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(matrix)
df = pd.read_csv('massiv.csv', header=None)
row_sums = df.sum(axis=1)
with open('res.txt', 'w') as f:
    for sum_value in row_sums:
        f.write(str(sum_value) + '\n')