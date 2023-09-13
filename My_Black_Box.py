def my_black_box1(num: float, month: int, year: float):
    month_letters = ""
    months1 = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
    if month <= 12:
        month_letters2 = months1[month - 1]
        month_letters = month_letters2
    else:
        print("The value entered is not correct")
    age = 2023 - year
    print(f"Your age is {age}")
    return num, month_letters, year


date = my_black_box1(num=19, month=12, year=2006)
print(f"And your date of birth is: {date}")