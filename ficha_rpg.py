import psycopg2

def conectar():
    try:
        conexao = psycopg2.connect(
            dbname="ficha_rpg",  
            user="postgres",  
            password="postgresql",  
            host="localhost",  
            port="5432"  
        )
        print("Conexão bem-sucedida ao banco de dados!")
        return conexao
    except Exception as e:
        print(f"Erro na conexão: {e}")

# Testando a conexão
if __name__ == "__main__":
    conectar()
