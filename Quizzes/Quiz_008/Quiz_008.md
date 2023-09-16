# Quiz 008
## Create a function that receives as input a string and returns the string ciphered with shift 13
### Python Code
```.pyc
def new_ascii(text: str, shift: int):
    for let in text:
        new = ord(let) + shift
        if let == " ":
            print(" ", end="")
            continue
        elif new > 122:
            new -= 26
        print(chr(new), end="")


x = new_ascii(text="abcdefghijklmnopqrstuvwxyz", shift=13)
```

### Proof
![Quiz_008_Proof_Image.png](Quiz_008_Proof_Image.png)
**Fig.1:** Proof of the Quiz 008

### Flow Chart
![Quiz_008_Flow_Chart.png](Quiz_008_Flow_Chart.png)
**Fig.2:** Flow Chart of the Quiz 008

### Work on paper
![Quiz_008_Work_Paper.jpeg](Quiz_008_Work_Paper.jpeg)
**Fig.3:** Work on paper of the Quiz 008