def mult(num: int) -> str:
    y = ""
    count = 0
    if 2 <= num <= 10:
        for n in range(1, 11):
            count += 1
            y += f"{num} * {count} = {num * count}\n"
        return y


result = mult(num=6)
print(result)
