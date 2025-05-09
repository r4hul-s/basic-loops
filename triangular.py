# Get number of rows from the user
rows = int(input("Enter number of rows: "))

# Print triangular star pattern
for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)