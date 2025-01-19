class DynamicProperties:
    """
    A class that allows dynamic addition of properties during runtime.
    """

    def add_property(self, name: str, default_value: str) -> None:
        """
        Adds a dynamic property to the object with the specified name and default value.

        Args:
            name (str): The name of the property.
            default_value (str): The default value for the property.
        """

        def getter(self_obj) -> any:
            """
            Gets the value of the dynamic property.

            Args:
                self_obj: The instance of the class.

            Returns:
                any: The value of the property, or the default value if the property has not been set.
            """
            return self_obj.__dict__.get(name, default_value)

        def setter(self_obj, value: str) -> None:
            """
            Sets the value of the dynamic property.

            Args:
                self_obj: The instance of the class.
                value (str): The new value for the property.
            """
            self_obj.__dict__[name] = value

        setattr(self.__class__, name, property(getter, setter))


obj = DynamicProperties()
obj.add_property('name', 'default_name')

print(obj.name)  # default_name
assert obj.name == 'default_name', "Should be 'default_name'"

obj.name = "Python"

print(obj.name)  # Python
assert obj.name == 'Python', "Should be 'Python'"
