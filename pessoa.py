'''
Utilizando orientação a objetos criar uma aplicação que insira uma pessoa em uma lista e valide os dados da pessoa.
A estrutura que representará a pessoa deve possuir os seguintes atributos:

Nome
Sobrenome
CPF 
Data de Nascimento 
As seguintes regras devem ser observadas:

Todas as informações são obrigatórias.
Caso alguma informação não seja preenchida deve-se apresentar uma mensagem informando que a 
informação específica é obrigatória e que a pessoa não foi adicionada à lista.
Ex: de mensagem: "A data de nascimento é obrigatória. O Cliente não foi adicionado à lista".
------------------------------------------------------------------------------------------------------|
Não deve ser possível adicionar pessoas com o mesmo CPF.
Validar quantidade total de candidatos por vaga.
Associar candidato por vaga.
A listagem de pessoas deve conter as informações:
'''
class Pessoa:
    def __init__(self, cpf, nome, sobrenome, data_de_nascimento ):
        self.__cpf = cpf 
        self.__nome = nome 
        self.__sobrenome = sobrenome 
        self.__data_de_nascimento = data_de_nascimento       
    
         
    # Métodos Get
    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_data_de_nascimento(self):
        return self.__data_de_nascimento    

    # Métodos Set
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_nome(self, nome):
        self.__nome = nome
    
    def set_sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome
    
    def set_rg(self, data_de_nascimento):
        self.__data_de_nascimento = data_de_nascimento

