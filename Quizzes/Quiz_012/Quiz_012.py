def mystery(num1: int, num2: int) -> int:
    x = num2 * (num1-1)
    y = x + num1
    return y

out = mystery(num1= 70, num2= 50)
print(out)