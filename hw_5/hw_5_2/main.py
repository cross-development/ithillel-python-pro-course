from calculators.average_calculator import AverageCalculator

if __name__ == '__main__':
    filename = "numbers.txt"
    calculator = AverageCalculator(filename)
    result = calculator.process()

    if result is not None:
        print(f"Average: {result}")
