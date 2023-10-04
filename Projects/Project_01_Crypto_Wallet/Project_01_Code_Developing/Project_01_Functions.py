with open("../Project_01_Files/Project_01_Words1.csv", mode="r") as words_file:
    words = words_file.readlines()
black = "\33[0;30m"
red = "\33[0;31m"
green = "\33[0;32m"
yellow = "\33[0;33m"
blue = "\33[0;34m"
purple = "\33[0;35m"
cyan = "\33[0;36m"
white = "\33[0;37m"
end_code = "\033[00m"
def uname_repeated(uname: str) -> bool:
    with open('../Project_01_Files/Project_01_Users_Logged.csv', mode='r') as f:
        data = f.readlines()
    same = False
    for line in data:
        user = line.split(',')[0].strip()
        if user == uname:
            same = True
            break
    return same


def validate_pass(upass:str) -> bool:
    upper, lower, num = False, False, False
    count = 0
    for letter in upass:
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


def try_login(msg1: str, msg2: str) -> bool:
    name = input(f"{yellow}{msg1}{end_code}")
    pass_login = input(f"{yellow}{msg2}{end_code}")
    with open('../Project_01_Files/Project_01_Users_Logged.csv', mode='r') as f:
        data = f.readlines()
    success = False
    for line in data:
        user = line.split(',')[0]
        upass = line.split(',')[1].strip()
        if user == name and upass == pass_login:
            success = True
            break
    return success


def recover_password(msg1: str) -> str:
    user_val = input(f"{yellow}{msg1}{end_code}")
    answers = []
    for n in range(9, 13):
        ques_ans = input(f"{yellow}{words[n]}{end_code}")
        answers.append(ques_ans.lower())
    with open('../Project_01_Files/Project_01_Users_Logged.csv', mode='r') as f:
        data = f.readlines()
    for line in data:
        line_user = line.strip().split(",")
        if line_user[0].strip() == user_val:
            if line_user[2] == answers[0] and line_user[3] == answers[1] and line_user[4] == answers[2] and line_user[5] == answers[3]:
                return f"{yellow}{words[19].strip()}{line_user[1]}\n{words[20]}{end_code}"
    return f"{red}{words[59]}{end_code}"



def frame_maker(msg: str, sym: str, space: int) -> str:
    width = 2 + 2 * space + len(msg)

    top_line = sym * width
    middle_line = sym + " "*(width-2) + sym
    msg_line = sym + " "*space + msg.upper() + " "*space + sym

    banner = f"{blue}{top_line}\n{middle_line}\n{msg_line}\n{middle_line}\n{top_line}{end_code}"
    return banner

def valid_number(msg: str, valid: str) -> str:
    valid_num = input(f"{yellow}{msg}{end_code}")
    while not valid_num in valid:
        valid_num = input(f"{red}ERROR!\n{msg}{end_code}")
    return valid_num

def valid_value(msg: str) -> float:
    amount = input(f"{yellow}{msg}{end_code}")
    temp1 = amount.replace(".", "")
    while not temp1.isnumeric():
        amount = input(f"{red}{words[40]}{end_code}")
        temp1 = amount.replace(".", "")
    withdraw_amount = float(amount)
    return withdraw_amount

def date_comparison(msg: str) -> str:
    while True:
        date_search = input(f"{yellow}{msg}{end_code}")
        splits_date = date_search.split("-")
        if len(splits_date) == 3:
            year, month, day = splits_date
            if day.isdigit() and month.isdigit() and year.isdigit():
                year, month, day = int(year), int(month), int(day)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    return f"{year}-{month:02}-{day:02}"
        print(f"{red}{words[48].strip()}{end_code}")



def reason_transaction(list:list) -> str:
    print(f"{purple}{(words[54].strip())}\n{(words[56])}{end_code}")
    for word in range(len(list)):
        print(f"{purple}{word+1}. {list[word]}\n{end_code}".strip())
    print()
    reason = valid_number(msg=words[55], valid="12345")
    return list[int(reason) - 1]


def project_leave():
    print(f"{purple}{words[35].strip()}\n{words[36]}{end_code}")
    number = valid_number(msg=words[3], valid="12")
    if number == '1':
        return f"{blue}{words[37]}{end_code}"
    elif number == "2":
        print(frame_maker(msg=words[52].strip(), sym="*", space=50))
    return exit(1)
