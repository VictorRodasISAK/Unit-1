"""my_info = [17, "Victor", "2025.victor.daniel.rodas.barrios@uwcisak.jp", "Guatemala"]
print(f"Hi my name is {my_info[1]}, and I am from {my_info[3]}, I am {my_info[0]} years old and my email is: {my_info[2]}")

index = 0

for nums in my_info[2]:
    index += 1
print(f"There are: {index} letters in my email")

count_vowel = 0
for letters in my_info[2]:
    if letters in "aiueo":
        count_vowel += 1
print(f"There are: {count_vowel} vowels in my email")

percentage = (count_vowel / index) * 100
print(f"The amount of vowels in my email = {percentage}%")

for numbers in range(0, 2024):
    print(f"Year {numbers}")
    numbers += 1

for numbers in range(1, 1000, 2):
    print(f"Odd numbers are: {numbers}")

for numbers in range(100):
    print(numbers % 3)

memes = ["LoL", "OMG", "Atp"]
for mem in range(100):
    print(memes[mem % 3], end= "-") """


# QUIZ 004
def number(num:int)->int:
    for n in range(num - 1):
        n += 1
        if num % n == 0:
            print(n)
    return num
result = number(num=40)