from pathlib import Path

caminho_do_arquivo = Path("clientes_biblioteca.txt")

nome = input("Digite seu nome: ")
telefone = int(input("Digite seu telefone: "))
numero_do_cartao = int(input("Digite o numero do seu cartão: "))

with caminho_do_arquivo.open(mode='a') as arquivo:
    arquivo.write(f"{nome}, {telefone}, {numero_do_cartao}\n")
    
print("Cliente cadastrado com sucesso!")