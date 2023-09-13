""" first = input("Please enter your first name: ")
last = input("Please enter your last name: ")

while True:
    yr = input("Enter your graduation year: ")
    if yr.isdigit()== True:
        year = int(yr)
        break

print(f"Your email is: {yr}.{first}.{last}@uwcisak.jp")


first = input("Put a word: ")
second = input("Put another word: ")

fc=first.capitalize()
sc=second.capitalize()
print(fc,sc)

email = input("Enter your email: ")

if "@" in email:
    if "@uwcisak.jp" in email:
        print("You are an isak member")
    else :
        print("you are not an isak member")
else:
    print("not an email")


x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))
if x < y and x < z:
    if y > z:
        print(f"The highest number is: " + str(y))
        print("The second number is: " + str(z))
        print("The last number is: " + str(x))
    else:
        print("The highest number is: " + str(z))
        print("The second number is: " + str(y))
        print("The last number is: " + str(x))
else:
    if y > z:
        print("The highest number is: " + str(x))
        print("The second number is: " + str(y))
        print("The last number is: " + str(z))
    else:
        print("The highest number is: " + str(x))
        print("The second number is: " + str(z))
        print("The last number is: " + str(y)) """

limite = 10
valor_inicial = 1
valor_actual = valor_inicial
incremento = 1

while True:
    print(valor_actual)
    valor_actual += incremento

    if valor_actual > limite:
        valor_actual = valor_inicial
