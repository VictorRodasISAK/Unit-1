def new_ascii(text: str, shift: int) -> str:
    x = ""
    for let in text:
        new = ord(let) + shift
        if new > 122:
            new -= 26
        x += f"{chr(new)}"
    return x



shift1 = new_ascii(text="abcdefghijklmnopqrstuvwxyz", shift=13)
print(shift1)