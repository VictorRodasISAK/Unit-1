units = ["Tera", "Giga", "Mega", "Kilo", "Unit", "Milli", "Micro", "Nano", "Pico"]
def powersTen(num:int) -> str:
    y = ""
    count = 0
    for x in range(-12,1,3):
        count += 1
        r = abs(x//3)
        y += f"{num}{' 000' * r}".ljust(20)
        y += f"{units[count - 1]} gram of salt\n"
    for n in range(0,12,3):
        count += 1
        t = n//3
        y += f"0.{'000 ' * t}00{num}".center(3).ljust(20)
        y += f"{units[count - 1]} gram of salt\n"
    return y
x = powersTen(num=7)
print(x)

