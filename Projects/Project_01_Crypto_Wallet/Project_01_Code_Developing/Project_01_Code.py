from Project_01_Functions import uname_repeated, validate_pass, try_login, recover_password, frame_maker, valid_number
from Project_01_Functions import valid_value, date_comparison, reason_transaction, project_leave
import datetime, requests, time, os, pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

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
                def return_menu():
                    while True:
                        for n_menu in range(21, 30):
                            print(words[n_menu].strip())
                            time.sleep(0.5)
                        validate2 = valid_number(msg=words[30], valid="1234567")

                        if validate2 == "1":
                            print(words[31])
                            website = "https://api.coingecko.com/api/v3/coins/markets"
                            info_wanted = {
                                "vs_currency": "usd",
                                "ids": "cardano",
                                "order": "market_cap_desc",
                                "per_page": 1,
                                "page": 1,
                                "sparkline": False
                            }

                            response = requests.get(website, params=info_wanted)

                            if response.status_code == 200:
                                data = response.json()[0]

                                print("Basic info about ADA:")
                                print(f"NAME: {data['name']}")
                                print(f"SYMBOL: {data['symbol']}")
                                print(f"ACTUAL PRICE (USD): ${data['current_price']}")
                                print(f"MARKET CAPITALIZATION (USD): ${data['market_cap']}")
                                print(f"TOTAL VOLUME IN THE LAST 24 HOURS (USD): ${data['total_volume']}")
                                print(f"PRICE VARIATION IN THE LAST 24 HOURS: {data['price_change_percentage_24h']}%")

                            else:
                                print(words[53])
                            print()
                            with open("../Project_01_Files/Project_01_Cardano_Info.txt", mode="r") as file:
                                cardano_file2 = file.read()
                                print(cardano_file2)

                            print(project_leave())

                        elif validate2 == "2":
                            with open("../Project_01_Files/Project_01_Account_Management.csv", mode='r') as file:
                                balance_file = file.readlines()
                            balance = 0
                            for line in balance_file:
                                date, amount, reason = line.strip().split(",")
                                balance += float(amount)
                            today = datetime.date.today()
                            message = f"Your current Cardano Coins {today} is {balance:.2f} ADA"
                            print(frame_maker(msg=message, sym="$", space=50, num=3))

                            print(project_leave())

                        elif validate2 == "3":
                            amount = valid_value(msg=words[32])
                            date = datetime.date.today()
                            reason = reason_transaction(list=["Work Payment", "Sales", "Luck", "Owed Money", "Others"])
                            line = f"{date},{amount},{reason}\n"
                            with open("../Project_01_Files/Project_01_Account_Management.csv", mode="a") as manage_file:
                                manage_transactions = manage_file.writelines(line)
                            print(words[42])
                            print(project_leave())

                        elif validate2 == "4":
                            with open("../Project_01_Files/Project_01_Account_Management.csv", mode='r') as file:
                                balance_file = file.readlines()

                            balance = 0
                            for line in balance_file:
                                date, amount, reason = line.strip().split(",")
                                balance += float(amount)
                            print(words[38].strip())
                            print(words[33])
                            withdraw_amount = valid_value(msg=words[39])

                            while float(withdraw_amount) > balance:
                                print(words[44].strip())
                                withdraw_amount = float(input(words[45]))
                            date = datetime.date.today()
                            reason = reason_transaction(list=["Payments", "Stuff", "Kombini", "Travels", "Others"])
                            line = f"{date},{-withdraw_amount},{reason}\n"
                            with open("../Project_01_Files/Project_01_Account_Management.csv", mode="a") as manage_file:
                                manage_transactions = manage_file.writelines(line)
                            print(words[43])
                            print(project_leave())


                        elif validate2 == "5":
                            print(words[46])
                            date_correct = date_comparison(msg=words[47])

                            with open("../Project_01_Files/Project_01_Account_Management.csv", mode='r') as file:
                                view_transactions = file.readlines()
                            for line in view_transactions:
                                date = line.split(",")[0]
                                amount = line.split(",")[1]
                                reason = line.split(",")[2].strip()
                                if date == date_correct:
                                    print(f"{date} {amount} ADA {reason}")
                                    print()

                            print(project_leave())

                        elif validate2 == "6":
                            csv_file = "/Users/m19-056/PycharmProjects/pythonProject1/Unit1/Projects/Project_01_Crypto_Wallet/Project_01_Files/Project_01_Account_Management.csv"
                            read_csv = pd.read_csv(csv_file)
                            info = [read_csv.columns.tolist()] + read_csv.values.tolist()
                            download_path = os.path.expanduser("~/Downloads")
                            pdf = os.path.join(download_path, "Account_Management.pdf")

                            doc = SimpleDocTemplate(pdf, pagesize=letter)
                            table = Table(info)
                            print_format = TableStyle([
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)
                            ])

                            table.setStyle(print_format)
                            info_stored = []
                            info_stored.append(table)
                            doc.build(info_stored)
                            print(f"{words[57]}{words[58]}")

                            print(project_leave())

                        elif validate2 == "7":
                            print(frame_maker(msg=words[52].strip(), sym="^", space=50, num=5))
                            exit(1)

                if __name__ == "__main__":
                    return_menu()

            if not result:
                print(words[16].strip())
                print(words[17])
                want_recover = valid_number(msg=words[3], valid="12")

                if want_recover == "1":
                    print(words[18])
                    questions_good = recover_password(msg1=words[13], msg2=words[9], msg3=words[10], msg4=words[11],
                                                      msg5=words[12])
                    print(questions_good)
                    print(project_leave())
                else:
                    print(words[37])
                    continue


if __name__ == "__main__":
    return_menu_login()
