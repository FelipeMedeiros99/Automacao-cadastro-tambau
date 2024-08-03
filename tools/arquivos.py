# desativado

'''
def dados_do_cadastro():

    from libs.correcao_de_dados import modelo_de_contato
    import os

    documento = os.path.join('C:\\','Users','USER','Desktop', 'dados para cadastro.txt')

    if not os.path.isfile(documento):

        with open(documento, 'w+') as arquivo:

            arquivo.write('nome:\n')
            arquivo.write('cpf:\n')
            arquivo.write('nascimento:\n')
            arquivo.write('\n')
            arquivo.write('reserva:\n')
            arquivo.write('\n')

            arquivo.write('cep:\n')
            arquivo.write('endereço:\n')
            arquivo.write('bairro:\n')
            arquivo.write('telefone:\n')
            arquivo.write('email:\n')
            print('documento "dados para cadastro" adicionado a área de trabalho')
            input()

    else:
        cpfs = []
        nomes = []
        nascimentos = []
        with open(documento, 'r+') as arquivo:
            for i in arquivo.readlines():
                # separando os cpfs
                if 'cpf' in i:
                    cpf = []
                    for dados in i:
                        cpf.append(dados) if dados.isnumeric() else None
                    cpf = ''.join(cpf)
                    if len(cpf) == 11:
                        cpfs.append(cpf)
                    else:
                        print(f'cpf {cpf} inválido, verifique e tente novamente')
                        input()
                        break

                # separando os nomes
                if 'nome' in i:
                    nome = []
                    for dados in i:
                        nome.append(dados)
                    nome = ''.join(nome)
                    nomes.append(nome[5:].strip())

                # separando os nascimentos
                if 'nascimento' in i:
                    nascimento = []
                    for dados in i:
                        nascimento.append(dados) if dados.isnumeric() else None
                    nascimento = ''.join(nascimento)
                    nascimentos.append(str(nascimento))

                # guardando o cep
                if 'cep' in i:
                    cep = []
                    for numeros in i:
                        if numeros.isnumeric():
                            cep.append(numeros)

                    cep = ''.join(cep)
                    if len(cep) != 8:
                        print('cep incorreto, verifique')
                        break

                # pegando o endereço
                if 'endereço' in i:
                    endereco = i[11:].strip()

                # pegando o bairro
                if 'bairro' in i:
                    bairro = i[7:].strip()



                # pegando o telefone
                if 'telefone' in i:
                    num = []
                    for numeros in i:
                        if numeros.isnumeric():
                            num.append(numeros)
                    numero = modelo_de_contato(''.join(num))
                    if not numero:
                        print('Número inválido, verifique')
                        input()
                        break
                if 'reserva' in i:
                    reserva = []
                    for numeros in i:
                        if numeros.isnumeric():
                            reserva.append(numeros)
                    reserva = ''.join(reserva)

                if 'email' in i:
                    email = i[6:].strip()

        dados = {'cpfs': cpfs, 'nomes': nomes, 'nascimentos': nascimentos,
                 'cep': cep, 'endereço': endereco, 'bairro': bairro,
                 'telefone': numero, 'email': email, 'reserva': reserva}
        return dados

'''

