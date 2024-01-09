#!/usr/bin/python3
"""Def func append."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in a file.

    :param filename: The name of the file.
    :param search_string: The specific string to search for in each line.
    :param new_string: The line of text to insert after lines containing the search string.
    """
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')

# Example usage:
if __name__ == "__main__":
    # Example file content before running the function
    with open("example.txt", "w", encoding="utf-8") as example_file:
        example_file.write("This is a sample file.\n")
        example_file.write("Line with the specific string.\n")
        example_file.write("Another line without the string.\n")

    # Running the function to insert a line after each line containing the specific string
    append_after(filename="example.txt", search_string="specific", new_string="Inserted line")

    # Display the updated content of the file
    with open("example.txt", "r", encoding="utf-8") as updated_file:
        print(updated_file.read())
