def try_login(name:str, password:str) -> bool:
    with open('09.14_Users.csv', mode='r') as f:
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
    result = try_login(name=in_name,password=in_pass)
    attempts -= 1

if result == False:
    print("Sayonara")
    exit(1) #1 is the code for exit without error

print("Welcome") #Rest of the program