nome = input('Digite seu nome: ')

idade = 36

print(f'Meu nome é {nome} e tenho {idade} anos')
# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))


palavra = 'ALURANDO'
cont = 0

while cont <= len(palavra)- 1:
    letra = palavra[cont]
    print(f'{letra}')
    cont += 1