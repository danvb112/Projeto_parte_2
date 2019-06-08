import sqlite3

class Aluno:

    def __init__(self):
        self.nome = ""
        self.cpf = ""
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    
    def adicionar_ao_banco(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        try:
            cursor.execute("""
                INSERT INTO alunos(nome, cpf) VALUES (?, ?)   
                """, (self.nome, self.cpf))
            pass
        except Exception as erro:
            print(erro)
            cursor.close()
            conexao.close()
            return erro
        cursor.close()
        conexao.commit()
        conexao.close()
        return True

    def apagar_do_banco(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
                DELETE FROM alunos were cpf = (?)
        """, (self.cpf))
        cursor.close()
        conexao.commit()
        conexao.close()
    
    def atualizar_banco(self, novo_nome, novo_cpf):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("""
                UPDATE alunos were nome = (?) SET cpf = (?) AND SET nome = (?) 
        """, (self.nome, novo_cpf, novo_nome))
        cursor.close()
        conexao.commit()
        conexao.close
    
    def listar_todos(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")
        lista_alunos = cursor.fetchall()
        for nome_cpf in lista_alunos:
            print("Nome: {}    CPF: {}".format(nome_cpf[1], nome_cpf[2]))
        cursor.close()
        conexao.commit()
        conexao.close()
    



        

