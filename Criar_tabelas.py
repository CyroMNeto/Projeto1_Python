import sqlite3

arquivo_db = "Base_Dados_teste.db"

def Abrir_conexao():
    conexao = None
    try:
        conexao = sqlite3.connect(arquivo_db)
    except sqlite3.Error as Erro_Conexao:
        print("OPS... Deu um erro: ", Erro_Conexao)

    return conexao

def Fechar_conexao(conexao):
    if conexao:
        conexao.close()

def Criar_tabelas(conexao, criar_tabela_sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(criar_tabela_sql)
    except sqlite3.Error as Erro_Criar_Tabela:
        print("OPS... Erro ao criar a Tabela: ", Erro_Criar_Tabela)

def Inserir_alunos(conexao, inserir_alunos_sql):
    try:
        cursor = conexao.cursor()
        cursor.execute(inserir_alunos_sql)
    except sqlite3.Error as Erro_Inserir_Alunos:
        print("OPS... Erro ao inserir alunos: ", Erro_Inserir_Alunos)

def Buscar_alunos(conexao, buscar_alunos_sql):
    alunos = None
    try:
        cursor = conexao.cursor()
        cursor.execute(buscar_alunos_sql)
        alunos = cursor.fetchall()
    except sqlite3.Error as Erro_Buscar_Alunos:
        print("OPS... Erro ao inserir alunos: ", Erro_Buscar_Alunos)
    finally:
        return alunos

#Iniciando a conexão
conexao = Abrir_conexao()

#Criando uma Tabela SQL
criar_tabela_sql = """ CREATE TABLE IF NOT EXISTS 
                        alunos ( id integer PRIMARY KEY AUTOINCREMENT,
                                 nome text NOT NULL,
                                 idade integer NOT NULL,
                                 nivel integer NOT NULL,
                                 faixa text NOT NULL
                      ); """
Criar_tabelas(conexao, criar_tabela_sql)

#Inserir alunos
sql_inserir_aluno_Arthur = "INSERT INTO alunos (nome, idade, nivel, faixa) VALUES ('Arthur',12, 3, 'Azul')"
sql_inserir_aluno_Thiago = "INSERT INTO alunos (nome, idade, nivel, faixa) VALUES ('Thiago',10, 2, 'Verde')"

Inserir_alunos(conexao, sql_inserir_aluno_Arthur)
Inserir_alunos(conexao, sql_inserir_aluno_Thiago)

#Buscando os alunos
buscar_alunos_sql = "SELECT * FROM alunos"
alunos = Buscar_alunos(conexao, buscar_alunos_sql)

#Fechando a conexão
Fechar_conexao(conexao)

for alunos in alunos:
    print(f'O aluno {alunos[1]}, faixa {alunos[4]}, nível {alunos[3]}, tem {alunos[2]} anos')