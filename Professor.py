import sqlite3

class Professor:

    def __init__(self):
        self.nome = ""
        self.cpf = ""
        self.departamento = ""
    
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
        try:
            cursor.execute("""
                    INSERT INTO professores (nome, cpf, departamento) VALUES (?,?,?)
            """, (self.nome, self.cpf, self.departamento))
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
        try:
            cursor.execute("""
                    DELETE FROM professores WHERE cpf = (?)
            """, (self.cpf,))
        except Exception as erro:
            print(erro)
            cursor.close
            conexao.close
            return erro
            
        cursor.close()
        conexao.commit()
        conexao.close()
    
    def atualizar(self,novo_nome, novo_cpf, novo_departamento):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        try:
            cursor.execute("""
                    UPDATE professores SET nome = "{}", cpf = "{}", departamento = "{}" WHERE cpf = "{}"
            """.format(novo_nome, novo_cpf, novo_departamento, self.cpf))
        except Exception as erro:
            print(erro)
            cursor.close
            conexao.close
            return erro
            
        cursor.close()
        conexao.commit()
        conexao.close()

    def lsitar(self):
        conexao = sqlite3.connect("database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM professores")
        lista_professores = cursor.fetchall()
        print("\n--- Lista de todos os professores registrados ---")
        print("=" * 50)
        for prof_info in lista_professores:
            print("Nome {}    CPf: {}\nDepartamento: {}".format(prof_info[1], prof_info[2], prof_info[3]))
        cursor.close()
        conexao.commit()
        conexao.close()
    