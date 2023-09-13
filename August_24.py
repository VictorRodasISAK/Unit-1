"""while True:
    salary = input("Please enter your salary: ")
    if salary.isdigit()== True:
        if int(salary) < 10001 and int(salary) > 0:
            tax1 = int(salary) * 0.05
            print("Your tax is: " + str(tax1) + " US")
            break
        else:
            if int(salary) < 50001:
                tax2 = int(salary) * 0.1
                print("Your tax is: " + str(tax2) + " US")
                break
            else:
                if int(salary) < 100001:
                    tax3 = int(salary) * 0.15
                    print("Your tax is: " + str(tax3) + " US")
                    break
                else:
                    tax4 = int(salary) * 0.25
                    print("Your tax is: " + str(tax4) + " US")
                    break
    else:
        print("The value that you enter is incorrect, try again!")
#Exercise 3
while True:
    N1 = input("Please enter the 1st name: ")
    N2 = input("Enter the 2nd name: ")
    N3 = input("Enter the 3rd name: ")
    if N1.isalpha():
        if N2.isalpha():
            if N3.isalpha():
                Names = N1, N2, N3
                NamesO = sorted(Names)
                print(NamesO)
                break
    else:
        print("The entered data is not correct, try again")"""

while True:
    a = input("Enter your 1st number: ")
    b = input("Enter your 2nd number: ")
    c = input("Enter your 3rd number: ")
    d = input("Enter your 4th number: ")
    e = input("Enter your 5th number: ")
    if a.isdecimal():
        if b.isdecimal():
            if c.isdecimal():
                if d.isdecimal():
                    if e.isdecimal():
                        Numbers = a, b, c, d, e
                        NumbersO = sorted(Numbers)
                        Middle_number = NumbersO[2]
                        print("The median of your scores is: " + Middle_number)
                        break
    else:
        print("The entered data is incorrect")