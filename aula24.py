# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  G a b r i e l
# -7-6-5-4-3-2-1

nome = 'Gabriel'

#print(nome[2])
#print(nome[-5])
#print('b' in nome)
#print('bri' in nome)

#print(10 * '-')

#print('b' not in nome)
#print('bri' not  in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')    