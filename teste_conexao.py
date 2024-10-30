from connection_factory import ConnectionFactory

class TesteConexao:
    @staticmethod
    def main():

        conexao = ConnectionFactory.get_connection()
        
        if conexao:
            print("Conexão aberta!")
            try:
            
                nome_cidade = input("Digite o nome da cidade: ")
                pais_cidade = input("Digite o nome do país: ")
                
                sql = "INSERT INTO cidade (nome, pais) VALUES (%s, %s)"
                
                cursor = conexao.cursor()
                
                cursor.execute(sql, (nome_cidade, pais_cidade))
                
                conexao.commit()
                print("Cidade inserida com sucesso!")
            except Exception as e:
                print(f"Ocorreu um erro ao inserir a cidade: {e}")
            finally:
                cursor.close()
                conexao.close()
        else:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")

if __name__ == "__main__":
    TesteConexao.main()
