"""def dna_translator(in_protein: str):
    out_protein = ""
    if in_protein == "A":
        out_protein = "T"
    if in_protein == "G":
        out_protein = "C"
    if in_protein == "T":
        out_protein = "A"
    if in_protein == "C":
        out_protein = "G"
    if in_protein == "AGTC":
        out_protein = "TCAG"
    return out_protein

x = dna_translator("G")
print(x)"""

"""def mystery_box1(word:str, flip_case:bool)->str:
    output = ""
    for letter in word:
        output = letter + output
    if flip_case == True:
        output = output.lower()
    else:
        output = output.replace(output[-1], "") + output[-1].upper()
    return output

test = mystery_box1(word = "Hello", flip_case = False)
print(test)

def mystery_box(email:str)-> str:
    output = ""
    output1 = email.split("@")
    output2 = output1[0]
    output3 = output1[1]
    output4 = output2.split(".")
    output5 = output4[0].capitalize(), output4[1].capitalize()
    output6 = output5[0] + " " + output5[1]
    output = (output6 + "\n" + output3)
    return str(output)
name = mystery_box(email = "victor.rodas@gmail.com")
print(name) """

"""def MCD(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
def MCM(num1, num2):
    return (num1 * num2) // MCD(num1, num2)
def Numbers_MCM(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = MCM(result, num)
    return result

numbers = [8, 6, 2]
mcm_result = Numbers_MCM(numbers)
print(mcm_result)

def mystery_box4(numbers_7: list):
    out = []
    result = 0
    for number in numbers_7:
        if number <= 7:
            out.append(number)
            suma = sum(out)
            result = suma / len(out)
    return result, out
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(mystery_box4(numbers_7=numbers))"""