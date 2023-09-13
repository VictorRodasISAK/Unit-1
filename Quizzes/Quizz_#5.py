"""text = str(input())
abc = "abcdefghijklmnopqrstuvwxyz"
total = 0
for let in text.lower():
    position = abc.find(let) + 1
    total += position

print(total)"""

def sum(text:str) -> int:
    ttl = 0
    for let in text:
        ttl += int(ord(let))
    return ttl

x = sum(text="MAth")
print(x)
