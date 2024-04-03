# Open the source file in read mode
with open('./archive (2)/human_chat.txt', 'r', encoding="UTF-8") as source_file:
    # Read all lines from the source file
    lines = source_file.readlines()

lines = [i[8:] for i in lines]
# Open the destination file in write mode
with open('e1.txt', 'w', encoding="UTF-8") as destination_file:
    # Write all lines to the destination file
    destination_file.writelines(lines)

print("Lines have been successfully copied from source_file.txt to destination_file.txt")
