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
        try:
            cursor.execute("""
                    DELETE FROM alunos WHERE cpf = ?
            """, (self.cpf,))
        except Exception as erro:
            print(erro)
            cursor.close()
            conexao.close()
            return erro
        cursor.close()
        conexao.commit()
        conexao.close()
    
    def atualizar_banco(self, novo_nome, novo_cpf):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        try:
            cursor.execute("""
                    UPDATE alunos 
                    SET cpf = "{}", 
                    SET nome = "{}"  WHERE cpf = "{}" 
            """.format(novo_cpf, novo_nome, self.cpf))
        except Exception as erro:
            print(erro)
            cursor.close()
            conexao.close()
            return erro
        cursor.close()
        conexao.commit()
        conexao.close
    
    def listar_todos(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")
        lista_alunos = cursor.fetchall()
        print("\n--- Lista de todos os Alunos registrados ---")
        print("=" * 50)
        for nome_cpf in lista_alunos:
            print("Nome: {}    CPF: {}".format(nome_cpf[1], nome_cpf[2]))
        cursor.close()
        conexao.commit()
        conexao.close()
    



        

