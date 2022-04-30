from pessoa import Pessoa

lista = list()


try:
    cpf = input("Insira seu CPF:\n").replace(' ','')
    keys = cpf 

    if cpf == '' or  len(cpf) != 11 :
        raise TypeError("O CPF é obrigatório. O Cliente não foi adicionado à lista.")
    
    name = input("Insira seu nome:\n").replace(' ','')
    if name == '':
        raise TypeError("o nome é obrigatório. O Cliente não foi adicionado à lista.")
    
    sobrenome = input("Insira seu sobrenome:\n").lstrip()
    if sobrenome == '':
        raise TypeError("O sobrenome é obrigatório. O Cliente não foi adicionado à lista.")
    
    data_de_nascimento = input("Data de nascimento:\n")
    if data_de_nascimento == '':
        raise TypeError("A data de nascimento é obrigatória. O Cliente não foi adicionado à lista.")

    if cpf in lista:
        raise TypeError("CPF já cadastrado")
    keys = Pessoa(cpf, name, sobrenome, data_de_nascimento) 
    lista.append(keys)    
except TypeError as mensagem:
    print("Erro: ",mensagem)

    
for pessoa in lista:
    print(pessoa.get_nome())

