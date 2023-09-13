"""def sum_letters(text: str) -> int:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sum_total = 0

    for let in text.lower():
        index = -1
        for i in range(len(alphabet)):
            if let == alphabet[i]:
                index = i+1
                sum_total += index
    return sum_total

case1 = sum_letters(text="Math")
print(case1)

N = int(input("Pleas enter your number: "))
for let in range(1, N + 1):
    print(let)
x = int(input())
sum = 0
for n in range(x):
    y = int(input())
    sum = y^3 + sum
    print(sum)

n = int(input())
answer = 'PRIME'
for i in range(2, n - 1):
    if n % i == 0:
        answer = 'COMPOSITE'
print(answer) """