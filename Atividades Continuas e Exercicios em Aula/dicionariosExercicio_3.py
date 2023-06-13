def conta_vogais(texto):
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    texto = texto.lower()
    for caractere in texto:
        if caractere in 'aeiou':
            vogais[caractere] += 1
    return vogais


def exibe(vogais):
    print('-' * 20)
    print('VOGAIS')
    print('-' * 20)
    for vogal in 'aeiou':
        print(f'\'{vogal}\' = {vogais[vogal]}')
    print()


def main():
    texto = input('Texto: ')
    vogais = conta_vogais(texto)
    exibe(vogais)


main()
