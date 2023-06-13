import random
import time
nome = str(input('diga seu nome: '))
print('bem vindo,', nome)
confirma = 0
vida = 10
pistola = 2
espingarda = 8
revolver = 5
arma_sel = int
zumbi_vida = 10

while vida > 0:
    while confirma == 0:
        time.sleep(0.7)
        arma = str(input(f'{nome}, escolha uma arma: \n pistola \n  dano: {pistola} \n  total de munição: {espingarda} \n espingarda \n  dano: {revolver} \n  total de munição: 5 \n revolver \n  dano: 3 \n  total de munição: 6 \n'))
        confirm = str(input(f'você selecionou {arma} \nconfimar? \n'))
        if confirm == 'sim':
            print(f'voce coletou {arma}')
            confirma += 1
            if arma == 'pistola':
                arma_sel = pistola
            elif arma == 'espingarda':
                arma_sel = espingarda
            elif arma == 'revolver':
                arma_sel = revolver
            time.sleep(0.7)
            print(f'\n...')
            time.sleep(1.5)
            print(f'\n \nbeleza {nome}, estamos em um apocalipse zumbi, doido não!? \nenfim, há um zumbi vindo!!! ')
            break
        else:
            confirma = 0
    while zumbi_vida > 0:
        time.sleep(1.5)
        fazer = str(input(f'o que faremos? \n atacar \n fugir \n'))

        if fazer == 'atacar':
            print('\nvocê atacou o zumbi')
            zumbi_vida -= arma_sel
            if zumbi_vida < 0:
                zumbi_vida = 0
            if vida < 0:
                vida = 0
            print(f'zumbi: {zumbi_vida}/10 \nvocê: {vida}/10')
            print(f'\nzumbi te atacou \nvoce: {vida-1}/10 \nzumbi: {zumbi_vida}/10')
        elif fazer == 'fugir':
            possibilidade = random.randint(1, 10)

            if (possibilidade%2) == 0:
                vida = 0
                print('um zumbi te atacou e você morreu!')
            else:
                zumbi_vida = 0
                print('você conseguiu fugir!')
    print('ótimo, você se livrou dele!')
    break