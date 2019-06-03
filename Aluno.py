import sqlite3

class Aluno():

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
