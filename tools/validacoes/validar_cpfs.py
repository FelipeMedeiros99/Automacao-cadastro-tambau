from re import compile, findall
from pycnpj_cpf.core import cnpj_or_cpf_is_valid as checar

def exibe_cpf(cpf):
    cpf_ = []
    for numero in cpf:
        cpf_.append(numero)
    cpf_.insert(3, '.')
    cpf_.insert(7, '.')
    cpf_.insert(11, '-')
    return ''.join(cpf_)


def validar_cpfs(txt):
    # ------- regex ------ 
    padrao = compile(r'(\d{3}.?.?.?\d{3}.?.?.?\d{3}.?.?.?\d{2})')

    # ------ vars --------
    cpfs_corretos = []
    cpfs_errados = []
    cpfs = findall(padrao, txt)
    
    # trabalhando os cpfs
    for cpf in cpfs:
        cpf = ''.join(list(filter(lambda x: x.isnumeric(), cpf)))
        cpf_valido = checar(cpf)
        if cpf_valido:
            cpfs_corretos.append(cpf)
        else:
            cpfs_errados.append(cpf)

    cpfs_errados = [exibe_cpf(cpfs_errados[c]) for c in range(len(cpfs_errados))]
    
    return cpfs_corretos, cpfs_errados
