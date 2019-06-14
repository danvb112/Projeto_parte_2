import sqlite3

conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()

cursor.execute("""

    CREATE TABLE alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL, 
        cpf TEXT NOT NULL UNIQUE )
""") 

cursor.execute("""
  
   CREATE TABLE professores(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE ,
        departamento TEXT NOT NULL)
""")

cursor.execute("""
    CREATE TABLE disciplinas(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL,
        codigo TEXT NOT NULL UNIQUE )
""")

conexao.commit()
cursor.close()
conexao.close()

