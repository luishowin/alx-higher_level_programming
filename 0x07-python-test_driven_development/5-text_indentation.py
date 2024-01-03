#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.

    Example:
    >>> text_indentation("Hello. How are you? This is a test: Goodbye.")
    Hello
    How are you
    This is a test
    Goodbye
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty line
    current_line = ""

    # Iterate through each character in the text
    for char in text:
        # Check if the character is one of '.', '?', or ':'
        if char in ('.', '?', ':'):
            # Print the current line without leading or trailing spaces
            print(current_line.strip())
            # Reset the current line for the next segment
            current_line = ""
        else:
            # Append the character to the current line
            current_line += char

    # Print the last line without leading or trailing spaces
    print(current_line.strip())

# Example usage:
text_indentation("Hello. How are you? This is a test: Goodbye.")