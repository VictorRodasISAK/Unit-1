def new_ascii(text: str, shift: int):
    for let in text:
        new = ord(let) + shift
        if let == " ":
            print(" ", end="")
            continue
        elif new > 122:
            new -= 26
        print(chr(new), end="")


x = new_ascii(text="abcdefghijklmnopqrstuvwxyz", shift=13)