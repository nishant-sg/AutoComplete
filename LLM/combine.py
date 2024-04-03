# List of text files to be combined
file_list = ['e1.txt', 'e2.txt']  # Add more files as needed

# Name of the combined file
combined_file = 'combined.txt'

# Open the combined file in write mode
with open(combined_file, 'w', encoding="UTF-8") as combined:
    # Iterate over each file in the list
    for file_name in file_list:
        # Open each file in read mode
        with open(file_name, 'r', encoding="UTF-8") as file:
            # Read the content of the file and write it to the combined file
            combined.write(file.read())
            # Add a newline to separate the content of each file
            combined.write('\n')

print("Text files have been successfully combined into combined.txt")
