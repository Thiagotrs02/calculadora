import math
while True:
    try:
        operador = input('Digite o operador que deseja realizar: ')
        if not operador:
            print('erro! digite um operador')
            continue



        if operador == '+':
            n1 = input('Digite um valor: ')
            n2 = input('Digite outro valor: ')
            if not n1.isdigit() or not n2.isdigit():
                print('erro! digite um valor')
                continue
            n1 = float(n1)
            n2 = float(n2)
            s = n1 + n2
            print(f'A soma de {n1} + {n2} = {s}')


        if operador == '-':
            n1 = input('Digite um valor: ')
            n2 = input('Digite outro valor: ')
            if not n1.isdigit() or not n2.isdigit():
                print('erro! digite um valor')
                continue
            n1 = float(n1)
            n2 = float(n2)
            s = n1 - n2
            print(f'A subtração de {n1} - {n2} = {s}')


        if operador == '*':
            n1 = input('Digite um valor: ')
            n2 = input('Digite outro valor: ')
            if not n1.isdigit() or not n2.isdigit():
                print('erro! digite um valor')
                continue
            n1 = float(n1)
            n2 = float(n2)
            s = n1 * n2
            print(f'A multiplicação de {n1} * {n2} = {s}')


        if operador == '/':
            n1 = input('Digite um valor: ')
            n2 = input('Digite outro valor: ')
            if not n1.isdigit() or not n2.isdigit():
                print('erro! digite um valor')
                continue
            n1 = float(n1)
            n2 = float(n2)
            s = n1 / n2
            print(f'A divisão de {n1} / {n2} = {s}')


        if operador == '**':
            n1 = input('Digite o valor da base: ')
            n2 = input('Digite o valor do expoente: ')
            if not n1.isdigit() or not n2.isdigit():
                print('erro! digite um valor')
                continue
            n1 = float(n1)
            n2 = float(n2)
            s = math.pow(n1, n2)
            print(f'A potencia de {n1} ** {n2} = {s}')


        if operador == '//':
            n1 = input('Digite um valor: ')
            n2 = input('Digite outro valor: ')
            if not n1.isdigit() or not n2.isdigit():
                print('erro! digite um valor')
                continue
            n1 = float(n1)
            n2 = float(n2)
            s = n1 // n2
            print(f'A divisão inteira de {n1} // {n2} = {s}')


        if operador == '%':
            n1 = input('Digite um valor: ')
            n2 = input('Digite a porcentagem: ')
            if not n1.isdigit() or not n2.isdigit():
                print('erro! digite um valor')
                continue
            n1 = float(n1)
            n2 = float(n2)
            p = n2 / 100
            s = n1 * p
            print(f'{n2}% de {n1} = {s}')


        sair = input('Deseja sair? [s/n] ').lower()
        if sair.startswith('s'):
            break
        else:
            continue

    except Exception as error:
        print(error)
