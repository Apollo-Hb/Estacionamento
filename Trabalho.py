# Aluno: Apollo.
# Data: 17/06/2024.

"""
Desenvolva uma aplicação Python que utilize ao menos 2 coleções e funções, para que seja possível realizar o cadastro de veículos em um estacionamento com o seguinte menu:

1 - Estacionar veículo

2 - Retirar veículo

3 - Veículos estacionados

4 - Está estacionado?

0 - Sair


Deve gravar a placa do veículo que será a chave, marca, modelo, cor e proprietário.


Para entrega:

- Deve ser comentado o código explicando o que faz cada coisa.

- Ter os comentários de docstring identificando o autor e data de criação

- Por padrão deve estacionar um carro que você é o proprietário

- Entregar aqui o link do repositório do github.

- Deve respeitar as normas da PEP-8

- O erros devem ser tratados.
"""

# Dicionário para armazenar os veículos estacionados.
estacionamento = {}

# Função que exibe o menu de opções e retorna a opção escolhida pelo usuário.
def menu():
    print("\nMenu:")  # Imprime o menu de opções.
    print("1 - Estacionar veículo")  # Opção para estacionar veículo.
    print("2 - Retirar veículo")  # Opção para retirar veículo.
    print("3 - Veículos estacionados")  # Opção para listar veículos estacionados.
    print("4 - Está estacionado?")  # Opção para verificar se um veículo está estacionado.
    print("0 - Sair")  # Opção para sair do programa.
    
    try:
        opcao = int(input("Escolha uma opção: "))  # Tenta converter a entrada do usuário em um inteiro.
        return opcao  # Retorna a opção escolhida
    except ValueError as e:  # Captura o erro se a conversão falhar.
        print(f"Opção inválida: {e}")  # Informa ao usuário que a opção é inválida.
        return None  # Retorna None se houver um erro.

# Função para estacionar um veículo no estacionamento.
def estacionar_veiculo():
    try:
        placa = input("Placa do veículo: ")  # Solicita a placa do veículo.
        if placa in estacionamento:  # Verifica se o veículo já está estacionado.
            print("Veículo já está estacionado.")  # Informa que o veículo já está estacionado.
            return

        marca = input("Marca do veículo: ")  # Solicita a marca do veículo.
        modelo = input("Modelo do veículo: ")  # Solicita o modelo do veículo.
        cor = input("Cor do veículo: ")  # Solicita a cor do veículo.
        proprietario = input("Proprietário do veículo: ")  # Solicita o nome do proprietário.

        estacionamento[placa] = {  # Adiciona o veículo ao dicionário de estacionamento com as informações que o usuario inserir.
            'marca': marca,
            'modelo': modelo,
            'cor': cor,
            'proprietario': proprietario
        }
        print(f"Veículo {placa} estacionado com sucesso.")  # Informa que o veículo foi estacionado com sucesso.
    except Exception as e:  # Captura qualquer exceção que ocorra durante o processo de estacionamento.
        print(f"Erro ao estacionar o veículo: {e}")  # Informa ao usuário sobre o erro.

# Função para retirar um veículo do estacionamento.
def retirar_veiculo():
    try:
        placa = input("Placa do veículo para retirar: ")  # Solicita a placa do veículo a ser retirado.
        
        if placa in estacionamento:  # Verifica se o veículo está no dicionário de estacionamento.
            del estacionamento[placa]  # Remove o veículo do dicionário de estacionamento.
            print(f"Veículo {placa} retirado com sucesso.")  # Informa que o veículo foi retirado com sucesso.
        else:
            print("Veículo não encontrado.")  # Informa que o veículo não foi encontrado no dicionário de estacionamento.
    except Exception as e:  # Qualquer exceção que ocorra durante o processo de retirada do veículo.
        print(f"Erro ao retirar o veículo: {e}")  # Informa ao usuário sobre o erro.
    # Função para listar os veículos estacionados.

def veiculos_estacionados():
    if estacionamento:  # Verifica se há veículos estacionados.
        print("Veículos estacionados:")
        for placa, detalhes in estacionamento.items():  # Itera sobre os itens do dicionário de estacionamento.
            print(f"Placa: {placa}")  # Imprime a placa do veículo.
            for chave, valor in detalhes.items():  # Itera sobre os detalhes do veículo.
                print(f"  {chave.capitalize()}: {valor}")  # Imprime os detalhes do veículo (marca, modelo, cor, proprietário).
            print()  # Imprime uma linha em branco para separar os veículos.
    else:
        print("Não há veículos estacionados.")  # Informa que não há veículos estacionados.

# Função para verificar se um veículo está estacionado.
def esta_estacionado():
    placa = input("Placa do veículo: ")  # Solicita a placa do veículo para verificação.
    if placa in estacionamento:  # Verifica se o veículo está no dicionário de estacionamento.
        print("Veículo está estacionado.")  # Informa que o veículo está estacionado.
    else:
        print("Veículo não está estacionado.")  # Informa que o veículo não está estacionado.

# Função para encerrar o programa.
def sair():
    print("Encerrando o programa.")  # Informa que o programa será encerrado.
    exit()  # Encerra o programa.

# Cria ou atualiza a chave 'abc' no dicionário 'estacionamento' com um novo dicionário contendo informações do veículo.
estacionamento["AL123"] = {
    "marca": "Audi",  # Define a marca do veículo.
    "modelo": "AudiR8",  # Define o modelo do veículo.
    "cor": "Prata",  # Define a cor do veículo.
    "proprietario": "Apollo Hoinatz Bardini"  # Define o proprietário do veículo.
}

# Imprime o dicionário para à chave AL123 dentro do dicionário estacionamento.
print(estacionamento["AL123"])

# Ponto de entrada do programa.
if __name__ == "__main__":
    while True:  # Loop infinito para manter o programa rodando.
        opcao = menu()  # Chama a função menu e armazena a opção escolhida.
        if opcao is None:  # Verifica se a opção é None, indicando uma entrada inválida.
            continue  # Continua o loop, solicitando uma nova opção.

        match opcao:  # Estrutura de decisão para executar a função correspondente à opção escolhida.
            case 1:  # Se a opção for 1, chama a função para estacionar um veículo.
                estacionar_veiculo()
            case 2:  # Se a opção for 2, chama a função para retirar um veículo.
                retirar_veiculo()
            case 3:  # Se a opção for 3, chama a função para listar os veículos estacionados.
                veiculos_estacionados()
            case 4:  # Se a opção for 4, chama a função para verificar se um veículo está estacionado.
                esta_estacionado()
            case 0:  # Se a opção for 0, chama a função para sair do programa.
                sair()