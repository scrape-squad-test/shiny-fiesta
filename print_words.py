file_path = 'text_file.txt'  # Replace with file name 

try:
    # read mode ('r')
    with open(file_path, 'r') as file:
        file_content = file.read()
        print("--- File Content ---")
        print(file_content)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# The University of Alabama at Birmingham (University of Alabama at Birmingham) UAB
