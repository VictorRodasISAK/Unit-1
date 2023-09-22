with open("../Project_01_Files/Project_01_Words1.csv", "r") as words_file:
    words = words_file.readlines()

for n in range(0, 3):
    print(words[n].strip())

validate = input(words[3])

while not validate in "12":
    print("ERROR")
    validate = input(words[3])

if int(validate) == 1:
    print(words[4])

    uname = input(words[5])


    def validate_pass(password: str) -> bool:
        upper, lower, num = False, False, False
        count = 0
        for letter in password:
            count += 1
            if letter.isupper():
                upper = True
            elif letter.islower():
                lower = True
            elif letter.isnumeric():
                num = True
        if count < 7:
            return False

        return upper and lower and num


    print(words[6])
    password = input(words[7])
    passw = validate_pass(password=password)

    while not passw:
        print(f"ERROR! {words[6]}")
        password = input(words[7])
        passw = validate_pass(password=password)


    print(words[8])
    answers = ""
    for n in range(9, 13):
        answers_recover = input(words[n])
        answers += answers_recover + ", "

    print(answers)

    with open("../Project_01_Files/Project_01_Users_Loged.csv", "w") as user_file:
        user_file.writelines(f"{uname},{password},{answers}\n")


"""def try_login(name:str, password:str) -> bool:
    with open('09.14_Users.csv',mode='r') as f:
        data = f.readlines()

    success = False
    for line in data:
        uname = line.split(',')[0]
        upass = line.split(',')[1].strip()
        if uname == name and upass == password:
            success = True
            break
    return success

attempts = 3
in_name = input("Enter your username")
in_pass = input("Enter your password")
result = try_login(name=in_name, password=in_pass)
while result == False and attempts > 1:
    in_name = input("Enter your username")
    in_pass = input("Enter your password")
    result = try_login(name=in_name, password=in_pass)
    attempts -= 1

if result == False:
    print("You are not in the database")
    exit(1)"""
