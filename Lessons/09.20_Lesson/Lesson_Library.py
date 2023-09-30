def frame_maker(msg: str, sym: str, space: int) -> str:
    width = 2 + 2 * space + len(msg)
    red = "\33[0;31m"
    end_code = "\033[00m"

    top_line = sym * width
    middle_line = sym + " "*(width-2) + sym
    msg_line = sym + " "*space + msg.upper() + " "*space + sym

    banner = f"{top_line}\n{middle_line}\n{red}{msg_line}{end_code}\n{middle_line}\n{top_line}"
    return banner

def print_menu(menu):
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]}")


def validate_integer(msg:str, menu):
    option = input(msg)
    while not option.isdigit():
        print("[ERROR]")
        print_menu(menu)
        option = input("Please enter an option: ")

    return int(option)