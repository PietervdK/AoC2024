import numpy as np

# Read the file
data = np.loadtxt('input_day1')

# Split into two arrays
array1 = data[:, 0]
array2 = data[:, 1]

# Initialize the variable to store the grand total
grand_total = 0

# Loop through each number in array1
for num in array1:
    # Count how many times this number exists in array2
    count_in_array2 = np.sum(array2 == num)
    
    # Multiply the value by the count and add to the grand total
    grand_total += num * count_in_array2

print("Grand Total:", grand_total)
