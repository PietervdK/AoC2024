import re
# Define the regex pattern
pattern_1 = "mul\(\d{1,3},\d{1,3}\)"

# Initialize lists to store the found
results_1 = []
# Open and read the text file
with open('input_day3', 'r') as file:
 for line in file:
 # Search for A and B configurations in the cur
    matches_1 = re.findall(pattern_1, line)

 # Extend the lists with the found values
 results_1.extend(matches_1)
 
# Print the results
#print("values:", results)

# Initialize list to store matches_2
results_2 = []

# Define regex pattern
pattern_2 = "\d{1,3},\d{1,3}"

# Initialize the total product accumulator
total_product = 0

#loop over list, extract integers and multiple , safe in result in total
for i in results_1:
    matches_2 = re.findall(pattern_2, line)
    results_2.extend(matches_2)
    for i in results_2:
       # Split the string by the comma
        parts = i.split(",")
    
    # Convert the parts into integers and calculate the product
        num1 = int(parts[0])
        num2 = int(parts[1])
        product = num1 * num2
    
    # Accumulate the product
    total_product += product

print(total_product)