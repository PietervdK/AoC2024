import numpy as np

def count_safe_sequences(file_path):
    safe_count = 0  # Counter for safe sequences

    def is_safe(sequence):
        """Check if a sequence is safe without removing any level."""
        differences = np.diff(sequence)
        increasing_safe = np.all((1 <= differences) & (differences <= 3))
        decreasing_safe = np.all((-3 <= differences) & (differences <= -1))
        return increasing_safe or decreasing_safe

    with open(file_path, 'r') as file:
        for line in file:
            # Convert the line to a NumPy array
            numbers = np.array(list(map(float, line.strip().split())))

            # Check if the sequence is safe directly
            if is_safe(numbers):
                safe_count += 1
                continue

            # Check if removing one element makes it safe
            for i in range(len(numbers)):
                temp_numbers = np.delete(numbers, i)
                if is_safe(temp_numbers):
                    safe_count += 1
                    break

    # Print only the total count of safe sequences
    print(safe_count)

# Example usage
file_path = "input_day2"  # Replace with your file path
count_safe_sequences(file_path)
