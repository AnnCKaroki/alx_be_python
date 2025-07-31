def safe_divide(numerator, denominator):

    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den

        print(f"The result of the division is {result}")

        return result

    except ValueError:
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
