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
    
    def adicionar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
                INSERT INTO alunos(nome, cpf) VALUES (?, ?)   
        """, (self.nome, self.cpf))
        cursor.close()
        conexao.commit()
        conexao.close()
    
    def apagar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
                DELETE FROM alunos were cpf = (?)
        """, (self.cpf))
        cursor.close()
        conexao.commit()
        conexao.close()
    
    def atualizar(self, novo_nome, novo_cpf):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
                UPDATE alunos were nome = (?) SET cpf = (?) AND SET nome = (?) 
        """, (self.nome,novo_cpf, novo_nome))
        cursor.close()
        conexao.commit()
        conexao.close
    
    def listar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")
        lista_alunos = cursor.fetchall()
        for nome_cpf in lista_alunos:
            print("Nome: {}    CPF: {}".format(nome_cpf[0], nome_cpf[1]))
        cursor.close()
        conexao.commit()
        conexao.close()
    



        

