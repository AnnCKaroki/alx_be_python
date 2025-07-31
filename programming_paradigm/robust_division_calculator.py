def safe_divide(numerator, denominator):

    try:
        num = float(numerator)
        den = float(denominator)

        result = num / den

        return result

    except ValueError:
        return "Error: Non-numeric input provided"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
