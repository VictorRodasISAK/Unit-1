from Project_01_Functions import uname_repeated, validate_pass, try_login, recover_password, frame_maker, valid_number, project_leave
import time
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

def return_menu_login():
    while True:

        for n in range(0, 3):
            print(f"{purple}{words[n].strip()}{end_code}")
            time.sleep(0.5)

        validate = valid_number(msg=words[3], valid="12")

        if validate == "1":
            user_repeat = input(f"{yellow}{words[4].strip()}\n{words[5]}{end_code}")
            valid_uname = uname_repeated(uname=user_repeat)
            while valid_uname == True:
                user_repeat = input(f"{red}{words[41].strip()}\n{words[5]}{end_code}")
                valid_uname = uname_repeated(uname=user_repeat)

            pass_test = input(f"{yellow}{words[6].strip()}\n{words[7]}{end_code}")
            passw = validate_pass(upass=pass_test)

            while not passw:
                pass_test = input(f"{red}ERROR!\n{words[6].strip()}\n{words[7]}{end_code}")
                passw = validate_pass(upass=pass_test)

            print(f"{purple}{words[8].strip()}{end_code}")
            answers = ""
            for n in range(9, 13):
                answers_recover = input(f"{yellow}{words[n]}{end_code}")
                answers += answers_recover + ","

            with open("../Project_01_Files/Project_01_Users_Logged.csv", mode="a") as user_file:
                user_file.writelines(f"{user_repeat},{pass_test},{answers.lower()}\n")

            print(f"{purple}{words[34]}{end_code}")
            print(project_leave())

        elif validate == "2":

            attempts = 4
            result = try_login(msg1=words[13], msg2=words[14])
            while result == False and attempts > 1:
                print(f"{red}ERROR! You have: {attempts - 1} attempts remaining, {words[15]}{end_code}")
                result = try_login(msg1=words[13], msg2=words[14])
                attempts -= 1
            if result:
                print(frame_maker(msg=words[21].strip(), sym="#", space=50))
                break

            if not result:
                print(f"{purple}{words[16].strip()}\n{words[17]}{end_code}")
                want_recover = valid_number(msg=words[3], valid="12")

                if want_recover == "1":
                    print(f"{purple}{words[18]}{end_code}")
                    print(recover_password(msg1=words[13]))
                    print(project_leave())
                else:
                    print(f"{blue}{words[37]}{end_code}")
                    continue

if __name__ == "__main__":
    return_menu_login()