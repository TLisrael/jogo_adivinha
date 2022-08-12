import random


def pc_adivinha(x):
    global adivinhe
    menor = 1
    maior = x
    feedback = ''
    while feedback != 'c':
        if menor != maior: # Se o número menor for diferente do maior
            adivinhe = random.randint(menor, maior) # Gere um número aleatório
        else:
            adivinhe = menor
        feedback = input(
            f'{adivinhe} é muito alto (A), muito baixo (B) ou correto (C)? ').lower()  # lower para que mesmo que o usuário digite em maiúsculo, o PC entenda em minusculo
        if feedback == 'a':
            maior = adivinhe - 1
        elif feedback == 'b':
            menor = adivinhe + 1
    print(f'O CPU acertou o seu número! {adivinhe} era o correto!')


pc_adivinha(10)
