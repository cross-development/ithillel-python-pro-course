class Person:
    """
    Represents a person with a name and age.

    Attributes:
        name (str): The person's name.
        age (int): The person's age.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Initializes a Person object.

        Args:
            name (str): The person's name.
            age (int): The person's age.
        """
        self.name = name
        self.age = age

    def __lt__(self, other: 'Person') -> bool:
        """
        Compares the ages of two people.

        Args:
            other (Person): The other person to compare with.

        Returns:
            bool: True if this person is younger than the other person, False otherwise.
        """
        return self.age < other.age

    def __eq__(self, other: 'Person') -> bool:
        """
        Checks if two people have the same age.

        Args:
            other (Person): The other person to compare with.

        Returns:
            bool: True if the ages are equal, False otherwise.
        """
        return self.age == other.age

    def __gt__(self, other: 'Person') -> bool:
        """
        Compares the ages of two people.

        Args:
           other (Person): The other person to compare with.

        Returns:
           bool: True if this person is older than the other person, False otherwise.
        """
        return self.age > other.age

    def __repr__(self) -> str:
        """
        Returns a string representation of the person.

        Returns:
           str: The string representation of the person object.
        """
        return f"Person(name='{self.name}', age={self.age})"


people: list[Person] = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35),
    Person("Diana", 20),
]

sorted_people = sorted(people)

print(sorted_people)

assert all(p1.age <= p2.age for p1, p2 in
           zip(sorted_people, sorted_people[1:])), "Each person should be younger than or equal to the next person"

print("All tests passed!")
