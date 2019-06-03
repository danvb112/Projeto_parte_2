class Disciplina():

    def __init__(self, codigo, nome):
        self.nome = nome
        self.codigo = codigo
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def get_codigo(self):
        return self.codigo
    
    def set_codigo(self, novo_codigo):
        self.codigo = novo_codigo
        