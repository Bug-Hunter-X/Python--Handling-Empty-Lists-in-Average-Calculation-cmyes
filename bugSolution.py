def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")  # Raise exception for empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

# Handling the exception
try:
    my_empty_list = []
    average_empty = calculate_average(my_empty_list)
    print(f"The average of an empty list is: {average_empty}")
except ValueError as e:
    print(f"Error: {e}") 