"""
Data processing script to read and parse poorly formatted CSV numbers.

This module reads a file containing comma-separated numbers with inconsistent
formatting, cleans the data, and calculates their sum.
"""


def parse_numbers_from_file(filename):
    """
    Read a file and parse integers from a poorly formatted comma-separated line.
    
    Args:
        filename (str): Path to the file containing comma-separated numbers.
    
    Returns:
        list: A list of parsed integers.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If non-numeric values are encountered after stripping.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    
    # Split by comma and process each element
    numbers = []
    for item in content.split(','):
        # Strip whitespace from each item
        cleaned = item.strip()
        # Ignore empty strings
        if cleaned:
            try:
                numbers.append(int(cleaned))
            except ValueError:
                print(f"Warning: Could not convert '{cleaned}' to integer. Skipping.")
    
    return numbers


def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.
    
    Args:
        numbers (list): List of integers to sum.
    
    Returns:
        int: The sum of all numbers in the list.
    """
    return sum(numbers)


def main():
    """Main function to orchestrate file reading and sum calculation."""
    filename = "data.txt"
    
    # Parse numbers from file
    numbers = parse_numbers_from_file(filename)
    
    if numbers:
        total = calculate_sum(numbers)
        print(f"Parsed numbers: {numbers}")
        print(f"Sum: {total}")
    else:
        print("No valid numbers found in file.")


# Test cases
if __name__ == "__main__":
    # Uncomment to run tests
    # Test 1: Create a sample file
    with open("data.txt", "w") as f:
        f.write("1, 2,3 ,4,,5")
    
    main()
    
    # Test 2: Verify with another format
    print("\n--- Test 2 ---")
    with open("data.txt", "w") as f:
        f.write("10,  20, , 30,40")
    
    main()