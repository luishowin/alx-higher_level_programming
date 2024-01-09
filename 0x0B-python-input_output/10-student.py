#!/usr/bin/python3
"""Def class."""


class Student:
    """
    Class representing a student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        :param age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        :param attrs: A list of strings specifying the attributes to include in the dictionary.
                      If None, all attributes are included.
        :return: A dictionary containing the specified attributes of the Student instance.
        """
        if attrs is None:
            # If attrs is None, include all attributes
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            # Include only the specified attributes
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

# Example usage:
if __name__ == "__main__":
    # Instantiate a Student
    student = Student(first_name="John", last_name="Doe", age=20)

    # Convert the Student instance to a dictionary with specified attributes
    selected_attrs = ['first_name', 'age']
    student_dict = student.to_json(attrs=selected_attrs)

    print("Dictionary representation of the Student instance with selected attributes:")
    print(student_dict)
