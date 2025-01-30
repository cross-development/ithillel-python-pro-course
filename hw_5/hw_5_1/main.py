from hw_5.hw_5_1.calculator import Calculator

if __name__ == '__main__':
    calculator = Calculator()

    while True:
        try:
            expression = input(
                "Enter calculation (e.g., 12.5 + 3.2; allowed operators: +, -, /, *) or 'exit' to quit: ").strip()

            if expression.lower() == 'exit':
                break

            parts_of_expression = expression.split()

            if len(parts_of_expression) != 3:
                raise ValueError("Invalid input format. Use: number operator number")

            num1, operator, num2 = parts_of_expression
            result = calculator.calculate(num1, operator, num2)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

        print("=" * 40)
