import csv
from typing import List

FILENAME = "students.csv"


def calculate_average_mark() -> None:
    """
    Calculates and prints the average mark of students from the CSV file.

    Reads the 'students.csv' file, extracts the 'Mark' column,
    calculates the average mark, and prints the result.

    Prints a warning message if there is no data in the file.
    """

    marks: List[int] = []

    with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            marks.append(int(row["Mark"]))

    if marks:
        avg_mark = sum(marks) / len(marks)
        print(f"The average grade of students: {avg_mark:.2f}")
    else:
        print("There is no data in the file.")


def add_student(name: str, age: int, mark: int) -> None:
    """
    Adds a new student record to the CSV file.

    Args:
        name (str): The name of the student.
        age (int): The age of the student.
        mark (int): The student's mark.
    """

    with open(FILENAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, mark])

    print(f"Student {name} has been added!")


if __name__ == "__main__":
    calculate_average_mark()

    new_name = input("Enter the student name: ")
    new_age = int(input("Age: "))
    new_mark = int(input("Mark: "))

    add_student(new_name, new_age, new_mark)

    calculate_average_mark()
