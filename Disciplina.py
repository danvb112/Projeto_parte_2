import sqlite3

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

    def adicionar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO disciplinas(nome, codigo) VALUES (?,?)
        """, (self.nome, self.codigo))
        cursor.close()
        conexao.commit()
        conexao.close()
    
    def apagar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
                DELETE FROM disciplinas were codigo = (?)
        """, (self.codigo))
        cursor.close()
        conexao.commit()
        conexao.close()
    
    def atualizar(self, novo_nome ,novo_codigo):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
                UPDATE disciplinas were codigo = (?) SET nome = (?) AND SET codigo = (?) 
        """, (self.codigo, novo_nome, novo_codigo))
        cursor.close()
        conexao.commit()
        conexao.close()

    def listar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM disciplinas")
        Lista_disciplinas = cursor.fetchall()
        for info_disciplinas in Lista_disciplinas:
            print("Nome: {}   Codigo: {}".format(info_disciplinas[0], info_disciplinas[1]))
        cursor.close()
        conexao.commit()
        conexao.close()
    
        
