while True:
    print ('-------------------------------------------')
    print ('Para dividir, digite /')
    print ('Para subtrair, digite -')
    print ('Para somar, digite +')
    print ('Para multiplicar digite *')
    print ('Para dividir e ter o resultado arredondado, digite //')
    print ('Para dividir e ter resultados com resto na divisão, digite R')
    print ('Para realizar uma exponenciação, digite ** (O segundo número digitado será elevado ao primeiro)')
    print ('Para sair digite 0')
    print ('-------------------------------------------')
    operacao= input()
    if operacao == '0':
        break;

    n1= int(input ('Escreva o primeiro número inteiro: '))
    n2= int(input ('Escreva o segundo número inteiro: '))
    if operacao == '+':
        print ('soma', n1+n2)

    elif operacao == '-':
        print('subtração', n1-n2)

    elif operacao == '/':
        if n2!=0:
            print ('Divisão', n1/n2)
        else:
             print ('NÃO DIVIDE POR ZERO !!!')
            
    elif operacao == '*':
        print ('multiplicação', n1*n2)
               
    elif operacao== '//':
        if n2!=0:
            print('Divisão arredondada', n1//n2)
        else:
            print('NÃO DIVIDE POR ZERO !!!')

    elif operacao == 'R':
        if n2!=0:
            print('Resto', n1%n2)
        else:
            print('NÃO DIVIDE POR ZERO !!!')

    elif operacao == '**':
            print('exponenciação', n1**n2)
        
        
    

