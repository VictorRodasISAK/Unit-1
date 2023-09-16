def best_month(month: str) -> str:
    y = ""
    print(month.center(32))
    print(f"Su   Mo   Tu   We   Th   Fr   Sa")
    for x in range(1,32):
        y += f"{str(x).center(2)}   "
        if x % 7 == 0:
            y += f"\n"
    return y

out = best_month(month="January")
print(out)