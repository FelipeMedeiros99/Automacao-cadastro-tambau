def filtra_numeros(string):
    string = list(string)
    numeros = [caractere for caractere in string if caractere.isnumeric()]
    return "".join(numeros)

