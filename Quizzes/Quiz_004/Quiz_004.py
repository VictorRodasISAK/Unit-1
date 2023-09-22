def searching_perfect(num: int) -> list and bool:
    m = []
    y = False
    for n in range(1, num):
        if num % n == 0:
            m.append(n)
            x = sum(m)
            if x == num:
                y = True
    return m, y

result = searching_perfect(num=3)
print(result)
