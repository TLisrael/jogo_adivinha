import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def adivinhe(x):  # Definindo função. x = parametro
    numero_aleatorio = random.randint(1, x)
    adivinhe = 0
    while adivinhe != numero_aleatorio:  # Enquanto o palpite for diferente do número aleatório gerado, faça
        adivinhe = int(input(f'Adivinhe o número que está entre 1 e {x}: '))
        if adivinhe < numero_aleatorio:
            print('Tente novamente. Você chutou baixo demais!')
        elif adivinhe > numero_aleatorio:
            print('Tente novamente. Você chutou alto demais.')

    print(f'Mandou bem, meu chapa. O número correto era {numero_aleatorio}')
    img = mpimg.imread('unnamed.jpg')
    imgplot = plt.imshow(img)
    plt.show()


adivinhe(10)


import random


def pc_adivinha(x):
    menor = 1
    maior = x
    feedback = ''
    while feedback != 'c':
        if menor != maior:
            adivinhe = random.randint(menor, maior)
        else:
            adivinhe = menor
        feedback = input(
            f'{adivinhe} é muito alto (A), muito baixo (B) ou correto (C)? ').lower()  # lower para que mesmo que o usuário digite em maiúsculo, o PC entenda em minusculo
        if feedback == 'a':
            maior = adivinhe - 1
        elif feedback == 'l':
            menor = adivinhe + 1
        print(f'O CPU acertou o seu número! {adivinhe} era o correto!')
    pc_adivinha(10)
