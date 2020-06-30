def func_executor(*args):
    result = []
    for arg in args:
        func = arg[0]
        params = arg[1]
        result.append(func(*params))
    return result
        

def sum_numbers(num1, num2, num3):
    return num1 + num2 + num3

def multiply_numbers(num1, num2, num3):
    return num1 * num2 * num3

print(func_executor((sum_numbers, (1, 2, 5)), (multiply_numbers, (2, 4, 2))))
