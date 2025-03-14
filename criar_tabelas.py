import psycopg2

def criar_tabelas():
    try:
        conexao = psycopg2.connect(
            dbname="ficha_rpg",
            user="postgres",
            password="postgresql",
            host="localhost",
            port="5432"
        )
        cursor = conexao.cursor()

        # Criando a tabela "personagem"
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS personagem (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                classe VARCHAR(50) NOT NULL,
                nivel INT DEFAULT 1,
                raca VARCHAR(50) NOT NULL,
                experiencia INT DEFAULT 0
            );
        """)

        # Criando a tabela "atributos"
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS atributos (
                id SERIAL PRIMARY KEY,
                personagem_id INT REFERENCES personagem(id) ON DELETE CASCADE,
                forca INT DEFAULT 10,
                destreza INT DEFAULT 10,
                constituicao INT DEFAULT 10,
                inteligencia INT DEFAULT 10,
                sabedoria INT DEFAULT 10,
                carisma INT DEFAULT 10
            );
        """)

        conexao.commit()
        print("Tabelas criadas com sucesso!")

    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")

    finally:
        cursor.close()
        conexao.close()

if __name__ == "__main__":
    criar_tabelas()
