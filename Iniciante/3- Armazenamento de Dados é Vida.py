#Desafio: Com as máquinas pesadas agrupadas estrategicamente, graças ao seu algoritmo de cálculo energético, agora a mineração está muito mais eficiente! Com isso, os CodeMiners logo terão que aumentar a capacidade de armazenamento de dados em seus discos de Mithril. Atualmente, cada máquina tem uma capacidade em teraflops e todas terão um upgrade! Escreva um programa que calcule a nova capacidade total de todas as máquinas após um aumento percentual específico.

capacidade_atual, aumento_percentual = map(int, input().split())

# TODO: Calcule a nova capacidade do disco de Mithril
capacidade_nova = int(capacidade_atual * (aumento_percentual/100+1))
# TODO: Imprima a nova capacidade
print(capacidade_nova)