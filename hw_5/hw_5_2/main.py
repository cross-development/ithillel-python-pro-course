from hw_5.hw_5_2.processors.average_calculator import AverageCalculator

if __name__ == '__main__':
    filename = "data/numbers.txt"
    calculator = AverageCalculator(filename)
    result = calculator.process()

    if result is not None:
        print(f"Average: {result}")
