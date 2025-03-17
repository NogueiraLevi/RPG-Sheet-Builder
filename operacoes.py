import psycopg2

# Função para conectar ao banco de dados
def conectar():
    return psycopg2.connect(
        dbname="ficha_rpg",
        user="postgres",
        password="postgresql",
        host="localhost",
        port="5432"
    )

def criar_personagem(nome, classe, raca, nivel=1):
    conexao = conectar() # Função para se conectar ao BD
    cursor = conexao.cursor() # Executar comandos SQL

    cursor.execute("""
        INSERT INTO personagem(nome, classe, raca, nivel)
        VALUES (%s, %s, %s, %s) 
        RETURNING id;
""", (nome, classe, raca, nivel)) # %s são placeholders 
    
    personagem_id = cursor.fetchone()[0] # Pega o primeiro resultado retornado(apenas o ID)
    conexao.commit() # Confirma inserção no banco
    cursor.close()
    conexao.close()

    print(f'personagem {nome} criado com sucesso! ID: {personagem_id}')
    return personagem_id # permitir saber qual foi o ID gerado

def listar_personagem():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM personagem;")
    personagens = cursor.fetchall()

    cursor.close()
    conexao.close()
    return personagens