import datetime, requests, time, os, pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from Project_01_Functions import valid_number, frame_maker, valid_value, date_comparison, reason_transaction, project_leave

with open("../Project_01_Files/Project_01_Words1.csv", mode="r") as words_file:
    words = words_file.readlines()


def return_menu():
    while True:
        for n_menu in range(21, 30):
            print(words[n_menu].strip())
            time.sleep(0.5)
        validate2 = valid_number(msg=words[30], valid="1234567")

        if validate2 == "1":
            print(words[31])
            url = "https://api.coingecko.com/api/v3/coins/markets"
            params = {
                "vs_currency": "usd",
                "ids": "cardano",
                "order": "market_cap_desc",
                "per_page": 1,
                "page": 1,
                "sparkline": False
            }

            response = requests.get(url, params=params)

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
            reason = reason_transaction(msg1=words[54], msg2=words[55], msg3=words[56],
                                        list=["Work Payment", "Sales", "Luck", "Owed Money", "Others"])
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
            reason = reason_transaction(msg1=words[54], msg2=words[55], msg3=words[56],
                                        list=["Payments", "Stuff", "Kombini", "Travels", "Others"])
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
            csv_file_path = "/Users/m19-056/PycharmProjects/pythonProject1/Unit1/Projects/Project_01_Crypto_Wallet/Project_01_Files/Project_01_Account_Management.csv"
            df = pd.read_csv(csv_file_path)
            data = [df.columns.tolist()] + df.values.tolist()
            download_folder = os.path.expanduser("~/Downloads")
            pdf_file = os.path.join(download_folder, "Account_Management.pdf")
            doc = SimpleDocTemplate(pdf_file, pagesize=letter)
            table = Table(data)

            style = TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])

            table.setStyle(style)
            story = []
            story.append(table)
            doc.build(story)
            print(f"{words[57]}{words[58]}")

            print(project_leave())

        elif validate2 == "7":
            print(frame_maker(msg=words[52].strip(), sym="^", space=50, num=5))
            exit(1)


if __name__ == "__main__":
    return_menu()