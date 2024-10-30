from cidade import Cidade
from controle_cidade import ControleCidade

def main():
    controle = ControleCidade()

    while True:
        print("\nMenu:")
        print("1. Cadastrar cidade")
        print("2. Pesquisar cidade")
        print("3. Excluir cidade")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            # Cadastrar cidade
            nome = input("Digite o nome da cidade: ")
            pais = input("Digite o país da cidade: ")
            nova_cidade = Cidade(id=None, nome=nome, pais=pais)  # ID é gerado pelo banco
            controle.cadastrar_cidade(nova_cidade)

        elif escolha == "2":
            # Pesquisar cidade
            id_cidade = int(input("Digite o ID da cidade a ser pesquisada: "))
            cidade_encontrada = controle.pesquisar_cidade(id_cidade)
            if cidade_encontrada:
                print(f"Cidade encontrada: {cidade_encontrada}")
            else:
                print("Cidade não encontrada.")

        elif escolha == "3":
            # Excluir cidade
            id_cidade = int(input("Digite o ID da cidade a ser excluída: "))
            cidade_para_excluir = controle.pesquisar_cidade(id_cidade)
            if cidade_para_excluir:
                controle.excluir_cidade(cidade_para_excluir)
            else:
                print("Cidade não encontrada para exclusão.")

        elif escolha == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
