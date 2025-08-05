def calculate(expression):
    parts = expression.split('+')
    result = 0
    for part in parts:
        if '*' in part:
            mult_parts = part.split('*')
            mult_result = 1
            for num in mult_parts:
                mult_result *= float(num)
            result += mult_result
        else:
            result += float(part)
    return result