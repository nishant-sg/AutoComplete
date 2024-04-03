import csv

# Open the CSV file in read mode
with open('./archive (3)/medium.csv', 'r', encoding="UTF-8") as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Open the text file in write mode
    with open('e2.txt', 'w', encoding="UTF-8") as txt_file:
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Check if the row has at least two columns
            if len(row) >= 2:
                # Write the second column to the text file
                txt_file.write(row[1] + '\n')

print("Second column has been successfully written to output.txt")
