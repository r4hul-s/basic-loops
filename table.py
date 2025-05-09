# Get input from the user
num = int(input("Enter a number to print its table: "))

# Print the multiplication table using a for loop
print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
