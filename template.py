# Importing necessary libraries
import numpy as np

# Define the list of numbers
numbers = [1,2,1,1,1,1,1,2,1,21,1]

# Count total number of elements in the list
total_numbers = len(numbers)

# Initialize variables
count = 0
max_count = 0
streaks_count = 0
long_streaks_count = 0
high_numbers_count = 0

# Find the highest number in the list
highest_number = max(numbers)

# Iterate through the list of numbers
for num in numbers:
    if num < 2.0:
        count += 1
        if count > max_count:
            max_count = count
            streaks_count = 1
        elif count == max_count:
            streaks_count += 1
        if count > 10:
            long_streaks_count += 1
    else:
        count = 0
    
    if num > 100000:
        high_numbers_count += 1

# Print the maximum number of consecutive occurrences where a number is less than 2.0
print("The maximum number of consecutive occurrences where a number is less than 2.0 is:", max_count)
print("This streak occurred", streaks_count, "times.")
print("The number of times a streak of more than 10 consecutive occurrences happened is:", long_streaks_count)
print("The total number of elements in the list is:", total_numbers)
print("The highest number in the list is:", highest_number)
print("The number of times a number higher than 100000 occurred is:", high_numbers_count)
