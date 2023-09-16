"""room_number= 0
for floor in range(1,11):
    for room in range(1, 11):
        room_number += 1
        print(f"{room_number}-Room {floor}F{room:02d}")"""


def room_find(number: int) -> str:
    room_number = 0
    y = ""
    for floor in range(1, 11):
        for room in range(1, 11):
            room_number += 1
            if room_number == number:
                y += f"{room_number}-Room {floor}F{room:02d}"
    return y

find_room = room_find(number = 50)
print(find_room)
