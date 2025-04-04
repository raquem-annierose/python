def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

answer = multiply(2, 3, 4) 
print(answer)# Output: 24

multiply()