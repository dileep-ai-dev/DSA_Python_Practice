arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Row sums
for idx, row in enumerate(arr, start=1):
    print("Row", idx, "sum =", sum(row))

print()

# Column sums
for idx, col in enumerate(zip(*arr), start=1):
    print("Column", idx, "sum =", sum(col))

print()

# Transpose
transpose = list(map(list, zip(*arr)))
print("Transpose:", transpose)