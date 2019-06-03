import sqlite3

conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()

cursor.execute("""

    CREATE TABLE alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL, 
        cpf TEXT NOT NULL)
""") 

cursor.execute("""
  
   CREATE TABLE professores(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        departamento TEXT NOT NULL)
""")

cursor.execute("""
    CREATE TABLE disciplinas(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL,
        codigo TEXT NOT NULL)
""")

cursor.execute("""
    CREATE TABLE turmas(
        id INTEGER PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL,
        codigo TEXT NOT NULL,
        periodo TEXT NOT NULL,
        disciplina_id INTEGER NOT NULL FOREING KEY(turmas_disciplina) REFERENCES disciplinas(id)
        professor_id INTEGER NOT NULL FOREING KEY(turmas_professor) REFERENCES professores(id)

    )
""")

cursor.execute("""
    CREATE TABLE alunos_turma(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER NOT NULL FOREING KEY(turma_aluno) REFERENCES alunos(id)
        turma_id INTEGER NOT NULL FOREING KEY(aluno_turma) REFERENCES turmas(id)
    )

""")

conexao.close()
