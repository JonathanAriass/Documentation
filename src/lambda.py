class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    """

    class MyClass:
        def __init__(self):
            """
            Initializes an instance of MyClass.
            """
            self.add = lambda x, y: x + y
            self.subtract = lambda x, y: x - y
            self.multiply = lambda x, y: x * y
            self.divide = lambda x, y: x / y

# Example usage
calc = Calculator()
print(calc.add(5, 3))  # Output: 8
print(calc.subtract(10, 4))  # Output: 6
print(calc.multiply(2, 6))  # Output: 12
print(calc.divide(15, 3))  # Output: 5