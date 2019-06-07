import sqlite3

class Professor():

    def __init__(self, nome, cpf, departamento):
        self.nome = nome
        self.cpf = cpf
        self.departamento
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    
    def get_departamento(self):
        return self.departamento
    
    def set_departamento(self, novo_departamento):
        self.departamento = novo_departamento
    
    def adicionar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
                INSERT INTO professores (nome, cpf, departamento) VALUES (?,?,?)
        """, (self.nome, self.cpf, self.departamento))
        cursor.close()
        conexao.commit()
        conexao.close()

    def apagar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
                DELETE FROM professores were cpf = (?)
        """, (self.cpf))
        cursor.close()
        conexao.commit()
        conexao.close()
    
    def atualizar(self,novo_nome, novo_cpf, novo_departamento):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
                UPDATE professores were cpf = (?) SET nome = (?) AND SET cpf = (?) AND SET departamento = (?) 
        """, (self.cpf, novo_nome, novo_cpf, novo_departamento))
        cursor.close()
        conexao.commit()
        conexao.close()

    def lsitar(self):
        conexao = sqlite3.connect()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM professores")
        lista_professores = cursor.fetchall()
        for prof_info in lista_professores:
            print("Nome {}    CPf: {}\nDepartamento: {}".format(prof_info[0], prof_info[1], prof_info[2]))
        cursor.close()
        conexao.commit()
        conexao.close()
    