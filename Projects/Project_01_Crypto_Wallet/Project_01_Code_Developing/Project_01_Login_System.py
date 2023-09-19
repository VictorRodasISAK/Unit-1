with open("../Project_01_Files/Project_01_Words.tsv", "r") as words_file:
    words = words_file.readlines()

def validate_uname(uname: str) -> bool:
    upper, lower, num = False, False, False
    for letter in uname:
        if letter.isupper():
            upper = True
        elif letter.islower():
            lower = True
        elif letter.isnumeric():
            num = True
    return upper and lower and num

answers = []
for msg in words:
    user_ques = input(msg)
    while not validate_uname(uname=user_ques):
        user_ques = input("ERROR " + msg)
    answers.append(user_ques)

print(answers)


#with open("Project_01_Users_Loged.csv", "w") as user_file:
    #user_file.writelines(f"{str(answers)}\n")



"""for msg in words:
    if 'username'in msg:
        user_a = input(msg)
        while validate_uname(user_a) == False:
            user_a = input("ERROR"+msg)
    else:
        user_a = input("ERROR " + msg)
    answers.append([msg, user_a])"""







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