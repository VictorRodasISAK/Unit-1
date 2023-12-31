# Crypto Wallet
![Project_01_Gif.gif](Project_01_Images/Project_01_Gif.gif)


**Fig.1:** *Crypto GIF* [^1]


[^1]: Ryanhoggan. “Bitcoin Crypto GIF - Bitcoin Crypto - Discover &amp; Share Gifs.” Tenor, Tenor, 20 July 2021, tenor.com/view/bitcoin-crypto-gif-22404527.


# Criteria A: Planning
## Problem Definition


Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell
electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which
is starting to become burdensome and too disorganized. It is also difficult for Ms. Sato to find past transactions or
important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the
cryptocurrency, the transactions, along with useful statistics.


## Proposed Solution


### Design Statement


I will design and make a Python Code for a client who is really interested in Cryptocurrencies. The Cryptocurrency that
I am going to use Cardano (ADA), For this Software I will be using Python 3.9. on PyCharm 23.2.1. running this on a MacBook Air model 2017.
It will take approximately two weeks, and it is going to be evaluated with the criteria that is set below. Also, the customer
needs to know every transaction, and keep everything organized, so the code will have organization, in consequence, the customer can
access to this information without problem. I will be using Python because the customer wants a software that can be run on an
effective way by the effective coding and with a clear idea of what the customer wants. PyCharm gives the client a
better experience, making our life easier to understand the different things that the project has. This software can be
run without problems on Windows, Linux and different operative systems. The costumer just need to have PyCharm to run the
software, it not requires higher requirements, because the tools that are going to be used are simple, therefore, the
program can be run on a computer with low-high statistics. Moreover, the program is always telling the customer what to do,
with the different options, so it is easy to understand every procedure and the customer will not have complications.




### Description of the Currency


Cardano sees itself as a third-generation blockchain platform designed to overcome the limitations of earlier blockchains
like Bitcoin and Ethereum. Launched in 2017, Cardano seeks to offer a more scalable, sustainable, and interoperable solution
for blockchain. Unlike some projects focusing solely on code development, Cardano emphasizes fact-finding and analysis,
aiming to create a robust foundation through scientific scrutiny and peer-reviewed academic research[^2]. Besides being an
innovative blockchain project, Cardano has some catalysts on the horizon, namely increased developer activity, that could
catapult its price higher. Investors who purchase its tokens now have the advantage of buying in at a much lower entry point,
which increases their potential upside[^3].


[^2]: Crypto.com. “What Is Cardano (Ada)?” Crypto.Com, crypto.com/university/what-is-cardano-ada. Accessed 18 Sept. 2023.


[^3]: Patel, Neil. “Why It Makes Sense to Buy Cardano Now.” The Motley Fool, The Motley Fool, 9 Jan. 2023, www.fool.com/investing/2023/01/09/why-it-makes-sense-to-buy-cardano-now/#:~:text=Besides%20being%20an%20innovative%20blockchain,which%20increases%20their%20potential%20upside.




### Description of my Software
My software is named Cardinity, where the function of this software is to have a record of transactions that the customer
with the Crypto Coin of Cardano. This has different options that the customer can do. The first thing that you can
do is have your procedures in a Safe Place, because you need to log-in by a username and a password that only the customer
know. In the case that the customer forget the password, after three attempts, the user can recover the password by following
the steps that are shown on the software. Besides, the program is giving different options to keep track of every process,
that the customer makes, like deposits, withdrawals, etc., even if the user wants to know the transaction made on a certain day.
In addition, it also shows information about the coin, and can print every transaction made into a pdf, so the customer
can have everything recorded.


### Justification
PyCharm is considered to be one of the most integrated Python IDEs, offering a range of modules and tools which make coding
a lot faster and easier for programmers. It offers support for both Python 2 (2.7) and Python 3 (3.5 and above) versions
and can be used on a multitude of platforms including Windows, Linux, and macOS[^4]. PyCharm has many advantages. Its an intelligent
code editor helps to write high quality code. Its different color codes for keywords, classes and functions increase the
readability and understandability of the code. This also simplifies error detection. An autocomplete feature is also included.
Code navigation features help developers to edit and improve code effortlessly, and to easily navigate to a function,
class or file. Locating an element, symbol or variable in the source code is very simple, and the lens mode allows to inspect
and debug the entire source code. Refactoring allows quick and efficient changes to local or global variables. Developers
can improve the internal structure without changing the external performance of the code[^5].


[^4]: Ramakrishnan, Manasa. “What Is PyCharm? How Is It Useful for Python Development?” Emeritus Online Courses, 24 Jan. 2023, emeritus.org/blog/coding-what-is-pycharm/.


[^5]: Alexandre. “Pycharm: All about the Most Popular Python Ide.” DataScientest, 20 Feb. 2023, datascientest.com/en/pycharm-all-about-the-most-popular-python-ide#:~:text=PyCharm%20has%20many%20advantages.,This%20also%20simplifies%20error%20detection.


## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger displays the description, the history and the future of the Cardano Crypto currency.
3. The electronic ledger allows users to enter, withdraw and record transactions.
4. The electronic ledger gives the opportunity to save every transaction made with the currency and print it as a pdf.
5. The electronic ledger allows an option to enter a date and watch the transactions that the customer made on that day.
6. The electronic ledger has a login system that gives the opportunity to restore the password by some questions.


# Criteria B: Design


## System Diagram
![Project_01_System_Diagram.png](Project_01_Images%2FProject_01_System_Diagram.png)


**Fig.2:** *System Diagram Image*


## Flow Diagrams
![Project_01_Flow_Diagram1.png](Project_01_Images%2FProject_01_Flow_Diagram1.png)


**Fig.3:** *Flow Diagram 1, validate_pass function*


![Project_01_Flow_Diagram1_Explained.png](Project_01_Images%2FProject_01_Flow_Diagram1_Explained.png)


**Fig.4:** *Flow Diagram 1 Explained, validate_pass function*


![Project_01_Flow_Diagram2.png](Project_01_Images%2FProject_01_Flow_Diagram2.png)


**Fig.5:** *Flow Diagram 2, try_login function*


![Project_01_Flow_Diagram2_Explained.png](Project_01_Images%2FProject_01_Flow_Diagram2_Explained.png)


**Fig.6:** *Flow Diagram 2 Explained, try_login function*


![Project_01_Flow_Diagram3.png](Project_01_Images%2FProject_01_Flow_Diagram3.png)


**Fig.7:** *Flow Diagram 3, recover_password function*


![Project_01_Flow_Diagram3_Explained.png](Project_01_Images%2FProject_01_Flow_Diagram3_Explained.png)


**Fig.8:** *Flow Diagram 3 Explained, recover_password function*


![Project_01_Flow_Diagram4.png](Project_01_Images%2FProject_01_Flow_Diagram4.png)


**Fig.9:** *Flow Diagram 4, date_comparison function*


![Project_01_Flow_Diagram4_Explained.png](Project_01_Images%2FProject_01_Flow_Diagram4_Explained.png)


**Fig.10** *Flow Diagram 4 Explained, date_comparison function*


## Record of tasks
| Task No | Planned Action                                    | Planned Outcome                                                                                                                                                                                           | Time estimate     | Target completion date | Criteria |
|---------|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------------|----------|
| 1       | Create a system diagram                           | To have a clear idea of the hardware and software requirements for the process                                                                                                                            | 10 min            | Sep 13                 | B        |
| 2       | Create a login system                             | To have a flow diagram and the code for the login system                                                                                                                                                  | 30 min            | Sep 14                 | B, C     |
| 3       | Describing the general idea of my software        | What the customer wants? What can I do to solve the problem? With this I had a better view of what I was expecting to reach with my code. Therefore, help my client in the best way possible.             | 45 min            | Sep 15                 | A        |
| 4       | Create a sign in system                           | To have a program that keeps the information safe and no one can access it, except the customer. In the case that the customer forgets the password, the customer will have the opportunity to recover it | 1 hour and 30 min | Sep 16                 | B, C     |
| 5       | Test the Log-In and Check-In                      | To have a clear idea if the project is working as expected                                                                                                                                                | 25 min            | Sep 17                 | C        |
| 6       | Flow diagrams of Log-In / Check-In                | To have an idea how the code is working and see if I can make it easier.                                                                                                                                  | 1 hour            | Sep 18                 | B        |
| 7       | Coding the first options for the costumer         | To have and show the different options that the customer can access, trying to make it easier and understandable for the customer.                                                                        | 2 hours           | Sep 19                 | C        |
| 8       | Getting feedback from my seniors                  | To see if I can make the code in an easier way.                                                                                                                                                           | 1 hour            | Sep 20                 | B        |
| 9       | Learning how to add information from web sites    | To know how I can make some connections with web pages. And have the best data possible in my code                                                                                                        | 1 hour and 15 min | Sep 22                 | B, C     |
| 10      | Including information from web pages into my code | To have the most updated values, and make life easier for my customer. So the client will know the recent values about the Crypto Coin.                                                                   | 2 hours           | Sep 23                 | C        |
| 11      | Learning how to convert a csv into a pdf          | To give my customer the option to print the transactions that the person made into a pdf                                                                                                                  | 1 hour and 30 min | Sep 24                 | C        |
| 12      | Getting feedback from my seniors (Part 2)         | To have a better code and make it comfortable for everyone who is using it.                                                                                                                               | 45 min            | Sep 24                 | B, C     |
| 13      | Adding the last options of menu                   | To have options well tested, therefore the code can run without problems                                                                                                                                  | 1 Hour            | Sep 25                 | C        |
| 14      | Reviewing my code                                 | To see if I can add more options or make it simpler with some functions                                                                                                                                   | 2 Hours           | Sep 26                 | C        |
| 15      | Start making more flow diagrams                   | To know how it is running, therefore, see if there is a  gap that I need to fulfill.                                                                                                                      | 3 Hours           | Sep 27                 | B, C     |
| 16      | Adding details to my code                         | To have a colorful and well defined code, so for the customer is going to be easier to follow instructions                                                                                                | 30 min            | Sep 28                 | C        |
| 17      | Receiving feedback from classmates                | To see if I can make other things that can be useful for my project                                                                                                                                       | 1 hour            | Sep 29                 | C        |
| 18      | Adding feedback given by classmates               | To have some details that can be helpful for the customer                                                                                                                                                 | 45 min            | Sep 30                 | C        |
| 19      | Finishing my flow diagrams                        | To have the complete scheme of how my program is working, therefore, see if I can make some changes.                                                                                                      | 1 hour and 30 min | Oct 01                 | B, C     |
| 20      | Reviewing the complete project                    | To see if I'm missing something or I can add more things to the project.                                                                                                                                  | 1 hour            | Oct 02                 | B        |
| 21      | Making my video of the proof                      | To show the entire process that my code can make.                                                                                                                                                         | 30 min            | Oct 04                 | B, C     |
| 22      | Uploading my project to Github                    | To show the project finished.                                                                                                                                                                             | 15 min            | Oct 04                 | B        |

# Criteria C: Development
## Existing tools
| Libraries |
|-----------|
| Datetime  |
| Requests  |
| Time      |
| Os        |
| Pandas    |


## List of techniques used
1. For Loops (To make a process several times, like look into the lines of the files)
2. If statements (To access to the different options. Moreover, to show or return some values if a statement is T or F)
3. Input validation (To see if the value entered is correct using 'While' loop)
4. Dictionaries (To give the parameters of the information that I want to get)
5. Web scraping (To get information from a website)
6. Reporting (To create a CSV into a PDF)
7. Encryption (To Log-In with a username and password)


## Development
### Words file
In this part of the code I have every phrase that I am using on the python code. I took this from a csv file named `Project_01_Words1.csv"`
I open this file as a 'read' mode. In addition, I use `words = words_file.readlines()` to read each line of the code.
So everytime that you see a 'words[x]' where 'x' is the number of the 'phrase' that I want to show.
```.py
with open("../Project_01_Files/Project_01_Words1.csv", mode="r") as words_file:
   words = words_file.readlines()
```
### Cardano Information 'Option 1' (Success Criteria #2)
Here is where I use the library of 'requests' that helps to extract information from a website, therefore this information
is taken from the website 'Coingecko' I take the information with `response = requests.get(website, params=info_wanted)`
Then with the dictionary 'info_wanted' I give the parameters or the info that I want to get from the website. `"vs_currency": "usd",`
is establishing a relation between the Crypto Coin and USD. `"ids": "cardano",` 'ids' refers that I want the information
from Cardano. `"order": "market_cap_desc",` 'order' as the name says, it is to order the information per capitalization.
`"per_page": 1, "page": 1,` means that I want to get information 1 per one, but in the second line I tell the program to
look just in the first page.`"sparkline": False` is in False, because I do not want to print a Graph. Finally,
`if response.status_code == 200:` this wants to measure that we get the information successfully.


```.py
website = "https://api.coingecko.com/api/v3/coins/markets"
info_wanted = {
   "vs_currency": "usd",
   "ids": "cardano",
   "order": "market_cap_desc",
   "per_page": 1,
   "page": 1,
   "sparkline": False
}
# Requesting the information from the website and the information that I want
response = requests.get(website, params=info_wanted)
# Success asking the request
if response.status_code == 200:
   data = response.json()[0]
```
### Transactions 'Option 3' and 'Option 4' (Success Criteria #3)
This is the code for Deposits. It starts with the function named `valid_value` which is validating the value entered by the
customer. If the user enters a letter or a negative value, it will display an error and have the opportunity to enter another
value. When the value is validated, the program will record the day with the library datetime `date = datetime.date.today()`.
Then, with the function `reason_transaction` the user needs to enter the reason for the deposit, this with numbers. Inside
I have another function named `valid_number` which measures if the value entered is valid.


```.py
amount = valid_value(msg=words[32])
date = datetime.date.today()
reason = reason_transaction(list=["Work Payment", "Sales", "Luck", "Owed Money", "Others"])
```


For the withdrawals I start by opening the file 'Project_01_Account_Management.csv' in read mode, and I split the values
that I have divided by a ',' and I take the 2nd value, because it is the place where the transactions are recorded. Then
I add these values and put them in 'balance'.
```.py
with open("../Project_01_Files/Project_01_Account_Management.csv", mode='r') as file:
   balance_file = file.readlines()
balance = 0
for line in balance_file:
   # The values that I get from the split
   date, amount, reason = line.strip().split(",")
   balance += float(amount)
```
In addition, I use the function `valid_value` to see if the value is valid. Then with a 'while' loop I measure
if the value is higher than the value in balance. If this is 'True' It will ask another time, until the statement is 'False'
Finally I record the day of the transaction and I use the function `reason_transaction` to keep the data well organized.
```.py
withdraw_amount = valid_value(msg=words[39])
while float(withdraw_amount) > balance:
   print(words[44].strip())
   withdraw_amount = float(input(words[45]))
date = datetime.date.today()
reason = reason_transaction(list=["Payments", "Stuff", "Kombini", "Travels", "Others"])
```
The file that I use is named 'Project_01_Account_Management.csv' and with this part of the code `manage_file.writelines(line)`
I can save and record the data with 'writelines'. The part of '(line)' means the format that I introduce.
```.py
with open("../Project_01_Files/Project_01_Account_Management.csv", mode="a") as manage_file:
   manage_transactions = manage_file.writelines(line)
```
### CSV into PDF Option '6' (Success criteria #4)
I start with putting the file route in 'csv_file', then with the library 'pandas as pd' `pd.read_csv(csv_file)` I read the file.
With `[read_csv.columns.tolist()]` the program take how many columns should have the table and with `read_csv.values.tolist()`
I put the information that the program finds. Next with the library 'os' I can direct where I want to download the PDF, in this case
in 'Downloads' `os.path.expanduser("~/Downloads")`. Also `os.path.join(download_path, "Account_Management.pdf")` this give
the opportunity to make the 'download_path' and name the pdf.
```.py
csv_file = "/Users/m19-056/PycharmProjects/pythonProject1/Unit1/Projects/Project_01_Crypto_Wallet/Project_01_Files/Project_01_Account_Management.csv"
read_csv = pd.read_csv(csv_file)
info = [read_csv.columns.tolist()] + read_csv.values.tolist()
download_path = os.path.expanduser("~/Downloads")
pdf = os.path.join(download_path, "Account_Management.pdf")
```
Now talking about the design of the information that I want to print, with the library `from reportlab.lib.pagesizes
import letter` and `from reportlab.platypus import SimpleDocTemplate` I can put the size of the PDF. With `from
reportlab.platypus import Table` and `table = Table(info)` I can make a table with the information that is on
the CSV. Talking about the style of the table I use the library `from reportlab.platypus import TableStyle` Each line is
well identified of what I want to reach and talking about the numbers, everytime you see a number (in the first part) or
'-1' in the (second part) refers that I want to put that option in my table, for example: `('BACKGROUND', (0, 1), (-1, -1), colors.white),`
In the first part, I put '(0,1)' the '0' is where the index starts, then '1' means the start of the range that I want for
the background, starting from 2, because the index starts from '0'. In the second part I put '(-1,-1)', this means that I
i want to apply the color white as my background from the beginning to the end. I can choose the color with the library
`from reportlab.lib import colors`. Finally, with `table.setStyle(print_format)` I set all the changes in my table.
```.py
doc = SimpleDocTemplate(pdf, pagesize=letter)
table = Table(info)
# Complete style of the table
print_format = TableStyle([
   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
   ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
   ('BACKGROUND', (0, 1), (-1, -1), colors.white),
   ('GRID', (0, 0), (-1, -1), 1, colors.black)
])
# Save the format and changes
table.setStyle(print_format)
```
### Search by date 'Option 5' (Success Criteria #5)
The program gives the opportunity to see the transactions that the user made on a certain day. Starting with a function
`date_comparison` that is to measure that the date entered is correct, if it is not correct, it will keep asking until it
is a valid value. Then, it will enter into the file 'Project_01_Account_Management' and split the values divided by ',' and
take the first value, this to compare with the returned information of the function 'date_comparison'. If there are transactions
on that day, it will print all the transactions on that day, otherwise, it will print nothing.
```.py
date_correct = date_comparison(msg=words[47])
with open("../Project_01_Files/Project_01_Account_Management.csv", mode='r') as file:
   view_transactions = file.readlines()
for line in view_transactions:
   date, amount, reason = line.strip().split(",")
   if date == date_correct:
       print(f"{green}{date} {amount} ADA {reason}{end_code}")
```
Here is the function `date_comparison`. At the beginning I tell the customer to enter a date with the format YYYY-MM-DD,
then I split the division with '-' if the splits are 3, it will continue with the program, if not, it will ask another time
until the splits are 3 . Then I split the values into 'year', 'month' and 'day', and I verify if these values are digits. If
they are digits, the function will continue, otherwise it will ask another time. If the format is not followed, I print
'Please follow the format'. Finally, I compare if the day is less or equal to 31 and greater or equal to 1, and month less
or equal tan 12 and greater or equal to 12. If everything is correct, it will return the date entered.
```.py
def date_comparison(msg: str) -> str:
   while True:
       date_search = input(msg)
       splits_date = date_search.split("-")
       if len(splits_date) == 3:
           year, month, day = splits_date
           if day.isdigit() and month.isdigit() and year.isdigit():
               year, month, day = int(year), int(month), int(day)
               if 1 <= month <= 12 and 1 <= day <= 31:
                   date = f"{year}-{month:02}-{day:02}"
                   return date


       print(words[48].strip())
```


### Password Recover (Success Criteria #6)
One of my success criteria was the option to recover the password by answering some questions that were asked at the registration,
This begins due to a mistake made in the Log-In, so after 3 attempts, the user will have the option to recover the password.
I define the function `recover_password` where the user needs to input the username and need to answer the questions. Then
I open a file with the line code `with open('../Project_01_Files/Project_01_Users_Logged.csv', mode='r') as f:` where I
have all the data of the users. Then I use a 'for' loop to split each line of the '.csv' file and I take the first value
of this, so I can compare the username and take the line that is the same as the username. Therefore, I can compare each
answer the questions, with the data that I have on the file. If everything is correct, it will show the password. However,
if something is bad, it will print that the person should make an account.


```.py
def recover_password(msg1: str) -> str:
   user_val = input(f"{yellow}{msg1}{end_code}")
   answers = []
   for n in range(9, 13):
       ques_ans = input(f"{yellow}{words[n]}{end_code}")
       answers.append(ques_ans.lower()) # I save all the answers in 'answers[]'
   with open('../Project_01_Files/Project_01_Users_Logged.csv', mode='r') as f:
       data = f.readlines()
   for line in data:
       line_user = line.strip().split(",")
       # I compare if the user entered is in the database
       if line_user[0].strip() == user_val:
           # If yes it will take just the data from this line, trying to compare every response
           if line_user[2] == answers[0] and line_user[3] == answers[1] and line_user[4] == answers[2] and line_user[5] == answers[3]:
               return f"{yellow}{words[19].strip()}{line_user[1]}\n{words[20]}{end_code}"
   return f"{red}{words[59]}{end_code}"
```
## Sign-In system
I start this process by asking if the customer wants to create an account or wants to Log-In. If the user wants to create
an account, the person needs to put a username and a password. With a function named `uname_repeated` I look into the database
and compare the usernames, if there is a username with the same name, the program will print that the username is already
being used.
```.py
user_repeat = input(words[5])
valid_uname = uname_repeated(uname=user_repeat)
while valid_uname == True:
   print(words[41].strip())
   user_repeat = input(words[5])
   valid_uname = uname_repeated(uname=user_repeat)
```
Then for the password, the client needs to fulfill some requirements, such us the password needs to contain at least 7
characters, one lower letter and one upper letter. With the function `validate_pass` I see if the password entered has the
correct format. If not, it will keep asking.
```.py
pass_test = input(words[7])
passw = validate_pass(upass=pass_test)
# It will keep asking if 'validate_pass' is False
while not passw:
   print(f"ERROR! {words[6].strip()}")
   pass_test = input(words[7])
   passw = validate_pass(upass=pass_test)
```
This is the function of `validate_pass`. If the password follows the format, the program will continue. Nevertheless,
if something is missing it will keep asking.
```.py
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
   # If all values are True, it will return true, otherwise, False.
   return upper and lower and num
```
Finally, if everything is good, the program will ask the personal questions, and keep all the data recorded on a CSV file,
named 'Project_01_Users_Logged'. All the information is separated by ','.
```.py
for n in range(9, 13):
   answers_recover = input(words[n])
   answers += answers_recover + ","


with open("../Project_01_Files/Project_01_Users_Logged.csv", mode="a") as user_file:
   user_file.writelines(f"{user_repeat},{pass_test},{answers.lower()}\n")
```
## Leave program function
I define the function `project_leave` and I print the options that the user has. Then I use another function named `valid_number`
that watch if the value entered is correct or not, it will continue asking until the vale is correct. Furthermore, If the
customer enters '1' it will return to the main menu, otherwise, the program will break completely with a message made by
another function named `frame_maker`.
```.py
def project_leave():
   print(f"{purple}{words[35].strip()}\n{words[36]}{end_code}")
   number = valid_number(msg=words[3], valid="12")
   if number == '1':
       return f"{blue}{words[37]}{end_code}" # Break the if (option) and returns to the main menu
   elif number == "2":
       print(frame_maker(msg=words[52].strip(), sym="*", space=50))
   return exit(1) # Break the hole program
```

# Video of the code

[Click here for the video](https://youtu.be/3r1-wyJCNsI)