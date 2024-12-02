import numpy as np

# Read the file
data = np.loadtxt('input_day1')

# Split into two arrays
array1 = data[:, 0]
array2 = data[:, 1]

# Sort both arrays
array1 = np.sort(array1)
array2 = np.sort(array2)

# Initialize the variable to store the grand total
grand_total = 0

# Iterate through both sorted arrays
for val1, val2 in zip(array1, array2):
    # Calculate the difference and add to the grand total
    grand_total += abs(val1 - val2)

print("Grand Total Difference:", grand_total)