import json

def save_to_json_file(my_obj, filename):
    """
    Write the given object to a text file using a JSON representation.

    :param my_obj: The object to be saved to the file.
    :param filename: The name of the file to which the object will be saved.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(my_obj, file)
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
my_object = {"name": "John", "age": 30, "city": "New York"}
save_to_json_file(my_object, "output.json")
