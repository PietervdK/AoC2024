import numpy as np

def count_matching_sequences(file_path):
    count = 0  # Counter for matching sequences
    
    with open(file_path, 'r') as file:
        for line in file:
            # Read and process each line
            numbers = np.array(list(map(float, line.strip().split())))
            
            # Calculate differences between consecutive elements
            differences = np.diff(numbers)
            
            # Check if the sequence is increasing or decreasing within bounds
            is_increasing = np.all((differences >= 1) & (differences <= 3))
            is_decreasing = np.all((-3 <= differences) & (differences <= -1))
            
            if is_increasing or is_decreasing:
                count += 1
    
    # Output only the total count
    print(count)

# Example usage
file_path = "input_day2"  # Replace with your file path
count_matching_sequences(file_path)
