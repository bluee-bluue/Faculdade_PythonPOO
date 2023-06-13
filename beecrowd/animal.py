palavra_1 = str(input())
palavra_2 = str(input())
palavra_3 = str(input())

if palavra_1 == 'vertebrado':
    if palavra_2 == 'ave':
        if palavra_3 == 'carnivoro':
            print('aguia')
        elif palavra_3 == 'onivoro':
            print('pomba')
    elif palavra_2 == 'mamifero':
        if palavra_3 == 'onivoro':
            print('homem')
        elif palavra_3 == 'herbivoro':
            print('vaca')
elif palavra_1 == 'invertebrado':
    if palavra_2 == 'inseto':
        if palavra_3 == 'hematofago':
            print('pulga')
        elif palavra_3 == 'herbivoro':
            print('lagarta')
    elif palavra_2 == 'anelideo':
        if palavra_3 == 'hematofago':
            print('sanguessuga')
        elif palavra_3 == 'onivoro':
            print('minhoca')
