nome = 'Gabriel Halmenschlager'
altura = 1.70
peso = 65
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Gabriel Halmenschlager tem 1.80 de altura,
# pesa 65 quilos e seu IMC é
# 22.49