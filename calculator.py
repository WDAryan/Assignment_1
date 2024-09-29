def main():
    try:

        expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")

        for operator in ['+', '-', '*', '/']:
            expression = expression.replace(operator, f' {operator} ')

        x, y, z = expression.split()

        x = int(x)
        z = int(z)

        if y == '+':
            result = x + z
        elif y == '-':
            result = x - z
        elif y == '*':
            result = x * z
        elif y == '/':
            result = x / z
        else:
            print("Invalid operator")
            return

        print(f"{result:.1f}")

    except ValueError:
        print("Invalid input format. Please enter the expression as 'x y z' where x and z are integers and y is an operator (+, -, *, /).")


main()
