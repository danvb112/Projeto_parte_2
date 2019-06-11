import sqlite3

class Disciplina:

    def __init__(self):
        self.nome = ""
        self.codigo = ""
    
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
        try:
            cursor.execute("""
                INSERT INTO disciplinas(nome, codigo) VALUES (?,?)
            """, (self.nome, self.codigo))
            pass
        except Exception as erro:
            print(erro)
            cursor.close()
            conexao.close()
            return erro
        cursor.close()
        conexao.commit()
        conexao.close()
    
    def apagar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
                DELETE FROM disciplinas WHERE codigo = (?)
        """, (self.codigo,))
        cursor.close()
        conexao.commit()
        conexao.close()
    
    def atualizar(self, novo_nome ,novo_codigo):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
                UPDATE disciplinas WHERE codigo = (?) SET nome = (?) AND SET codigo = (?) 
        """, (self.codigo, novo_nome, novo_codigo))
        cursor.close()
        conexao.commit()
        conexao.close()

    def listar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM disciplinas")
        Lista_disciplinas = cursor.fetchall()
        print("\n--- Lista com todas as disciplinas registradas ---")
        print("=" *50)
        for info_disciplinas in Lista_disciplinas:
            print("Nome: {}   Codigo: {}".format(info_disciplinas[1], info_disciplinas[2]))
        cursor.close()
        conexao.commit()
        conexao.close()
    
        
