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
