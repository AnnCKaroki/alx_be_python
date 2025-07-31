def safe_divide(numerator, denominator):

    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den

        return result

    except ValueError:
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
