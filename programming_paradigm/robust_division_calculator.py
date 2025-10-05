def safe_divide(numerator, denominator):
    """
    Safely divides numerator by denominator, handling errors.
    Returns result or error messages.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"

