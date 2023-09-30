def avaregeLength(words:list) -> float:
    count = 0
    for n in words:
        for x in n:
            count += 1
            if x == " ":
                count -= 1
    return count/len(words)


z = avaregeLength(words=["Computer Science", "Art"])
print(z)