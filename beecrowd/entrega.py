semana = str(input())
dia = int(input())
dias = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

if semana == 'domingo' or semana == 'segunda' or semana == 'terca' or semana == 'quarta' or  semana == 'quinta' or semana == 'sexta' or semana == 'sabado':
    if dia >= 0 and dia <= 6:
        if semana == 'domingo':
            if dia == 0:
                print('chega hoje!')
            elif dia == 1:
                print('sera entregue segunda')
            elif dia == 2:
                print('sera entregue terca')
            elif dia == 3:
                print('sera entregue quarta')
            elif dia == 4:
                print('sera entregue quinta')
            elif dia == 5:
                print('sera entregue sexta')
            elif dia == 6:
                print('sera entregue sabado')
        if semana == 'segunda':
            if dia == 0:
                print('chega hoje!')
            elif dia == 1:
                print('sera entregue terca')
            elif dia == 2:
                print('sera entregue quarta')
            elif dia == 3:
                print('sera entregue quinta')
            elif dia == 4:
                print('sera entregue sexta')
            elif dia == 5:
                print('sera entregue sabado')
            elif dia == 6:
                print('sera entregue domingo')
        if semana == 'terca':
            if dia == 0:
                print('chega hoje!')
            elif dia == 1:
                print('sera entregue quarta')
            elif dia == 2:
                print('sera entregue quinta')
            elif dia == 3:
                print('sera entregue sexta')
            elif dia == 4:
                print('sera entregue sabado')
            elif dia == 5:
                print('sera entregue domingo')
            elif dia == 6:
                print('sera entregue segunda')
        if semana == 'quarta':
            if dia == 0:
                print('chega hoje!')
            elif dia == 1:
                print('sera entregue quinta')
            elif dia == 2:
                print('sera entregue sexta')
            elif dia == 3:
                print('sera entregue sabado')
            elif dia == 4:
                print('sera entregue domingo')
            elif dia == 5:
                print('sera entregue segunda')
            elif dia == 6:
                print('sera entregue terca')
        if semana == 'quinta':
            if dia == 0:
                print('chega hoje!')
            elif dia == 1:
                print('sera entregue sexta')
            elif dia == 2:
                print('sera entregue sabado')
            elif dia == 3:
                print('sera entregue domingo')
            elif dia == 4:
                print('sera entregue segunda')
            elif dia == 5:
                print('sera entregue terca')
            elif dia == 6:
                print('sera entregue quarta')
        if semana == 'sexta':
            if dia == 0:
                print('chega hoje!')
            elif dia == 1:
                print('sera entregue sabado')
            elif dia == 2:
                print('sera entregue domingo')
            elif dia == 3:
                print('sera entregue segunda')
            elif dia == 4:
                print('sera entregue terca')
            elif dia == 5:
                print('sera entregue quarta')
            elif dia == 6:
                print('sera entregue quinta')
        if semana == 'sabado':
            if dia == 0:
                print('chega hoje!')
            elif dia == 1:
                print('sera entregue domingo')
            elif dia == 2:
                print('sera entregue segunda')
            elif dia == 3:
                print('sera entregue terca')
            elif dia == 4:
                print('sera entregue quarta')
            elif dia == 5:
                print('sera entregue quinta')
            elif dia == 6:
                print('sera entregue sexta')
