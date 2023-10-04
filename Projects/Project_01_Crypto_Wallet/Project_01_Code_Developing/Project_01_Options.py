import datetime, requests, time, os, pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from Project_01_Functions import valid_number, frame_maker, valid_value, date_comparison, reason_transaction, project_leave

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

def return_menu():
    while True:
        for n_menu in range(22, 30):
            print(f"{purple}{words[n_menu].strip()}{end_code}")
            time.sleep(0.5)
        validate2 = valid_number(msg=words[30], valid="1234567")

        if validate2 == "1":
            print(f"{purple}{words[31]}{end_code}")
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
                print(f"{red}{words[53]}{end_code}\n")
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
            print(frame_maker(msg=message, sym="$", space=50))
            print(project_leave())

        elif validate2 == "3":
            amount = valid_value(msg=words[32])
            date = datetime.date.today()
            reason = reason_transaction(list=["Work Payment", "Sales", "Luck", "Owed Money", "Others"])
            line = f"{date},{amount},{reason}\n"
            with open("../Project_01_Files/Project_01_Account_Management.csv", mode="a") as manage_file:
                manage_transactions = manage_file.writelines(line)
            print(f"{green}{words[42]}{end_code}")
            print(project_leave())

        elif validate2 == "4":
            with open("../Project_01_Files/Project_01_Account_Management.csv", mode='r') as file:
                balance_file = file.readlines()

            balance = 0
            for line in balance_file:
                date, amount, reason = line.strip().split(",")
                balance += float(amount)
            print(f"{purple}{words[38].strip()}\n{words[33]}{end_code}")
            withdraw_amount = valid_value(msg=words[39])

            while float(withdraw_amount) > balance:
                withdraw_amount = input(
                    f"{purple}{print(words[44].strip())}{end_code}\n{yellow}{float(input(words[45]))}{end_code}")
            date = datetime.date.today()
            reason = reason_transaction(list=["Payments", "Stuff", "Kombini", "Travels", "Others"])
            line = f"{date},{-withdraw_amount},{reason}\n"
            with open("../Project_01_Files/Project_01_Account_Management.csv", mode="a") as manage_file:
                manage_transactions = manage_file.writelines(line)
            print(f"{green}{words[43]}{end_code}")
            print(project_leave())


        elif validate2 == "5":
            print(f"{purple}{words[46]}{end_code}")
            date_correct = date_comparison(msg=words[47])

            with open("../Project_01_Files/Project_01_Account_Management.csv", mode='r') as file:
                view_transactions = file.readlines()
            for line in view_transactions:
                date, amount, reason = line.strip().split(",")
                if date == date_correct:
                    print(f"{green}{date} {amount} ADA {reason}{end_code}")
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
            print(f"{purple}{words[57]}{words[58]}{end_code}")
            print(project_leave())

        elif validate2 == "7":
            print(frame_maker(msg=words[52].strip(), sym="^", space=50))
            exit(1)


if __name__ == "__main__":
    return_menu()