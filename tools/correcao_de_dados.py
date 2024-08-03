import re

def modelo_de_contato(numero):
    try:
        contato = [num for num in numero if num.isnumeric()]

        if len(contato) == 10:
            contato.insert(2, '9')
            return ''.join(contato)

        else:
            return ''.join(contato)
    except IndexError:
        return ""


def exibe_cpf(cpf):
    """
    serve exclusivamente para deixar o cpf bonito de se ver
    :param cpf:
    :return:
    """
    cpf_ = []
    for pos, numero in enumerate(cpf):
        cpf_.append(numero)
    cpf_.insert(3, '.')
    cpf_.insert(7, '.')
    cpf_.insert(11, '-')
    return ''.join(cpf_)

def modelo_cpf(txt):
    lista_cpfs = []
    padrao = re.compile(r'(\d{3}.?.?.?\d{3}.?.?.?\d{3}.?.?.?\d{2})')
    cpfs = re.findall(padrao, txt)
    cpf_errado = []
    # trabalhando os cpfs
    for cpf in cpfs:
        cpf = ''.join(list(filter(lambda x: x.isnumeric(), cpf)))
        # calculando o primeiro dígito verificador
        cpf_errado.append(cpf)
        digito1 = []
        for pos, cont in enumerate(range(10, 1, -1)):
            digito1.append(int(cpf[pos])*cont)
        digito1 = 11 - (sum(digito1) % 11)
        if digito1 >= 10:
            digito1 = 0
        # se o primeiro estiver correto, calcula-se o segundo
        if digito1 == int(cpf[9]):
            digito2 = []
            for pos, cont in enumerate(range(11, 1, -1)):
                digito2.append(int(cpf[pos]) * cont)
            digito2 = 11 - (sum(digito2)%11)
            if digito2 >= 10:
                digito2 = 0

            if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
                cpf_errado.remove(cpf)
                lista_cpfs.append(exibe_cpf(cpf))
    cpf_errado = [exibe_cpf(cpf_errado[c]) for c in range(len(cpf_errado))]
    return lista_cpfs, cpf_errado


if __name__ == "__main__":
    print(modelo_cpf('123..456. 789- 78'))
