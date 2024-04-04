# Desafio
# Em um jogo de RPG, os personagens geralmente possuem uma lista de itens que podem ser utilizados durante o jogo. Esses itens podem ser armas, armaduras, poções de cura, entre outros. É importante que o jogador tenha um controle desses itens para poder utilizá-los no momento adequado.
# Crie um programa que permita cadastrar uma lista de itens que o personagem possui. A lista deve conter o valor fixo de 3 itens e deve ser exibida na tela.

# Lista para armazenar os itens
itens = []

#//ToDo: Solicite os itens ao usuário
for iten in range(3):
    itens.append(input())
print("Lista de itens:")
for item in itens:
    print(f'- {item}')