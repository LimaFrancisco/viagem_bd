from cidade import Cidade
from connection_factory import ConnectionFactory
import psycopg2
from psycopg2 import sql

class ControleCidade:
    def __init__(self):
        self.conexao = ConnectionFactory.get_connection()

    def cadastrar_cidade(self, cidade):

        if self.conexao:
            try:
                sql_insert = "INSERT INTO cidade (nome, pais) VALUES (%s, %s)"
                cursor = self.conexao.cursor()
                cursor.execute(sql_insert, (cidade.nome, cidade.pais))
                self.conexao.commit()
                print("Cidade cadastrada com sucesso!")
            except Exception as e:
                print(f"Ocorreu um erro ao cadastrar a cidade: {e}")
            finally:
                cursor.close()
                self.conexao.close()
        else:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")

    def pesquisar_cidade(self, id):
        cidade = None
        if self.conexao:
            try:
                sql_select = "SELECT id, nome, pais FROM cidade WHERE id = %s"
                cursor = self.conexao.cursor()
                cursor.execute(sql_select, (id,))
                resultado = cursor.fetchone()
                
                if resultado:
                    cidade = Cidade(id=resultado[0], nome=resultado[1], pais=resultado[2])
                else:
                    print("Cidade não encontrada.")
            except Exception as e:
                print(f"Ocorreu um erro ao pesquisar a cidade: {e}")
            finally:
                cursor.close()
                self.conexao.close()
        
        return cidade

    def excluir_cidade(self, cidade):
        if self.conexao:
            try:
                sql_delete = "DELETE FROM cidade WHERE id = %s"
                cursor = self.conexao.cursor()
                cursor.execute(sql_delete, (cidade.id,))
                self.conexao.commit()
                
                if cursor.rowcount > 0:
                    print("Cidade excluída com sucesso!")
                else:
                    print("Cidade não encontrada para exclusão.")
            except Exception as e:
                print(f"Ocorreu um erro ao excluir a cidade: {e}")
            finally:
                cursor.close()
                self.conexao.close()
        else:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")
