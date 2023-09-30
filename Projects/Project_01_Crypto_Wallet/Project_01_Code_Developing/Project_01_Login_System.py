from Project_01_Functions import uname_repeated, validate_pass, try_login, recover_password, frame_maker, valid_number, project_leave
import time
with open("../Project_01_Files/Project_01_Words1.csv", mode="r") as words_file:
    words = words_file.readlines()

def return_menu_login():
    while True:

        for n in range(0, 3):
            print(words[n].strip())
            time.sleep(0.5)

        validate = valid_number(msg=words[3], valid="12")

        if validate == "1":
            print(words[4])
            user_repeat = input(words[5])
            valid_uname = uname_repeated(uname=user_repeat)
            while valid_uname == True:
                print(words[41].strip())
                user_repeat = input(words[5])
                valid_uname = uname_repeated(uname=user_repeat)

            print(words[6].strip())
            pass_test = input(words[7])
            passw = validate_pass(upass=pass_test)

            while not passw:
                print(f"ERROR! {words[6].strip()}")
                pass_test = input(words[7])
                passw = validate_pass(upass=pass_test)

            print(words[8])
            answers = ""
            for n in range(9, 13):
                answers_recover = input(words[n])
                answers += answers_recover + ","

            with open("../Project_01_Files/Project_01_Users_Logged.csv", mode="a") as user_file:
                user_file.writelines(f"{user_repeat},{pass_test},{answers.lower()}\n")

            print(words[34])
            print(project_leave())

        elif validate == "2":

            attempts = 3
            result = try_login(msg1=words[13], msg2=words[14])
            while result == False and attempts > 1:
                print(f"ERROR! {words[15]}")
                result = try_login(msg1=words[13], msg2=words[14])
                attempts -= 1
            if result:
                print("Welcome")
                break
            if not result:
                print(words[16].strip())
                print(words[17])
                want_recover = valid_number(msg=words[3], valid="12")

                if want_recover == "1":
                    print(words[18])
                    questions_good = recover_password(msg1=words[13], msg2=words[9], msg3=words[10], msg4=words[11],
                                                      msg5=words[12])
                    print(questions_good)
                    print()
                    print(project_leave())
                else:
                    print(words[37])
                    continue


if __name__ == "__main__":
    return_menu_login()