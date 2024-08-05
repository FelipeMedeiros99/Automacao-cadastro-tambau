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