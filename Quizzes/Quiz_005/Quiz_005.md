# Quiz 005
## Given a string, create a program that produces the sum of the characters in the string.
### Python Code
```.py
def sum(text:str) -> int:
    ttl = 0
    for let in text:
        ttl += int(ord(let))
    return ttl

x = sum(text="MAth")
print(x)
```

### Proof
![Quiz_005_Proof_Image.png](Quiz_005_Proof_Image.png)
**Fig.1:** Proof of the Quiz 005

### Flow Chart
![Quiz_005_Flow_Chart.png](Quiz_005_Flow_Chart.png)
**Fig.2:** Flow Chart of the Quiz 005

### Work on paper
![Quiz_005_Work_Paper.jpeg](Quiz_005_Work_Paper.jpeg)
**Fig.3:** Work on paper of the Quiz 005