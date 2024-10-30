import psycopg2
from psycopg2 import OperationalError

class ConnectionFactory:
    USERNAME = "postgres"
    PASSWORD = "1234"
    DB_URL = "localhost"
    DB_PORT = "5433"
    DB_NAME = "viagem"
    
    @staticmethod
    def get_connection():
 
        try:
            conexao = psycopg2.connect(
                host=ConnectionFactory.DB_URL,
                port=ConnectionFactory.DB_PORT,
                database=ConnectionFactory.DB_NAME,
                user=ConnectionFactory.USERNAME,
                password=ConnectionFactory.PASSWORD
            )
            return conexao
        except OperationalError as e:
            print(f"Ocorreu um erro ao conectar ao banco de dados: {e}")
            return None
