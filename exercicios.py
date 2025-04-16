print('Python na Escola de Programação da Alura')

nome = 'Wesley Fabiano Laurindo'
idade = 36

print(f'Meu nome é {nome} e tenho {idade} anos')
# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

palavra = 'ALURA'
cont = 0

while cont <= len(palavra)- 1:
    letra = palavra[cont]
    print(f'{letra}')
    cont += 1

pi = 3.14159
pi_arredondado = round(pi,2)

print(f'O valor de pi arredondado é : {pi_arredondado}')


def configurar_tempo_foco():
    import os
    os.system('clear')
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if 25 <= tempo <= 45:
        print("Tempo configurado para", tempo, "minutos.")
    else:
        print("Valor inválido. Configure um tempo entre 25 e 45 minutos.")

configurar_tempo_foco()        