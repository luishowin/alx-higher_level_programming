#!/usr/bin/bash
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        :return: A dictionary containing the attributes of the Student instance.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

# Example usage:
if __name__ == "__main__":
    # Instantiate a Student
    student = Student(first_name="John", last_name="Doe", age=20)

    # Convert the Student instance to a dictionary
    student_dict = student.to_json()

    print("Dictionary representation of the Student instance:")
    print(student_dict)
