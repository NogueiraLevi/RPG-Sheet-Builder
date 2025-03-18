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

# Select tabela
def listar_personagem():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM personagem;")
    personagens = cursor.fetchall()

    cursor.close()
    conexao.close()
    return personagens

# Atualizar Personagem
def atualizar_personagem(personagem_id, novo_nome, nova_classe, nova_raca, novo_nivel, nova_experiencia):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE personagem
        SET nome = %s, classe = %s, raca = %s, nivel = %s, experiencia = %s
        WHERE id = %s
        RETURNING id;
    """, (novo_nome, nova_classe, nova_raca, novo_nivel, nova_experiencia, personagem_id))

    atualizado = cursor.fetchone()  # Verifica se o ID foi atualizado
    conexao.commit()

    cursor.close()
    conexao.close()

    if atualizado:
        print(f"Personagem ID {personagem_id} atualizado com sucesso!")
    else:
        print(f"Erro: Nenhum personagem com ID {personagem_id} encontrado.")


# Deletar Personagem
def deletar_personagem(personagem_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM personagem WHERE id = %s", (personagem_id,))
    conexao.commit()

    cursor.close()
    conexao.close()
    
    print(f"Personagem ID {personagem_id} deletado com sucesso!")
