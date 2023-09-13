def dna_translator(in_protein: str) -> str:
    out_protein = ""
    for n in in_protein:
        if n == "A":
            out_protein += "T"
        elif n == "G":
            out_protein += "C"
        elif n == "T":
            out_protein += "A"
        elif n == "C":
            out_protein += "G"
    return out_protein


x = dna_translator(in_protein="agtc".upper())
print(x)
