def blackbox3(word: str) -> str:
    vars = []
    result = ""
    for i in range(26):
        vars.append(0)
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for k in range(len(word)):
        letter = word.lower()[k]
        for i in range(len(alpha)):
            if letter == alpha[i]:
                vars[i] += 1
                result += str(vars[i])
        if letter == " ":
            result += " "
    return result


x = blackbox3(word="aaaaAABB")
print(x)