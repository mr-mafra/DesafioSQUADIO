# Desafio: A Aventura do Explorador

# //ToDO: Adicione uma condição para verificar se a quantidade de passos é positiva.
# // Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
# // Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

# Entrada
quantidade_passos = int(input())

if quantidade_passos == 0:
    print("Nenhum passo dado na floresta.")

else:
    for passo in range(1,quantidade_passos+1):
        if passo == 1:
            print(f"Explorador: {passo} passo")
        else:
            print(f"Explorador: {passo} passos")
