# Quiz 004
## Given a number, create a program that produces the output factors.
### Python Code
```.py
def number(num: int):
    m = []
    for n in range(num - 1):
        n += 1
        if num % n == 0:
            print(n)
            m.append(n)
            x = sum(m)
            if x == num:
                print()
                print(f"{num} is a perfect number")
    return num, m


result = number(num=28)
```
### Proof
![Quiz_004_Proof_Image.png](Quiz_004_Proof_Image.png)

### Flow Chart
![Quiz_004_Flow_Chart.png](Quiz_004_Flow_Chart.png)

### Work on paper
![Quiz_004_Work_Paper.jpeg](Quiz_004_Work_Paper.jpeg)