#RU 4491252

#mensagem de erro para as dimensoes
def mensagemErro():
    print('Você digitou alguma dimensão do objeto com valor não numérico')
    print('Por favor entre com as dimensões desejadas novamente')

#mensagem de erro para o Peso
def mensagemErro2():
    print('Você digitou o peso do objeto com valor não numérico')
    print('Por favor entre com o peso desejado novamente')


#função para coletar as dimensões do objeto
def dimensoesObjeto():
    
    #armazenando o cálculo das dimensoes versus valor
    precoDimensoes4491252 = 0
    while True: #criando o loop
        try: #tentativa de inserir comprimento
            comprimento = float(input('Digite o comprimento do objeto (em cm): ')) #inserindo o comprimento
            if comprimento <= 0: #tratamento de erro para valores negativos e 0
                mensagemErro() #chamando a função mensagem de erro
                continue #fazendo o looping voltar ao início

        #tratamento de erro valor não numérico
        except: #caso o valor seja uma letra
            mensagemErro() #aparecerá a mensagem de erro
            continue #o programa retornará ao começo

        #o código abaixo segue a mesma ideia do comprimento, apenas mudando a variável para largura
        try:
            largura = float(input('Digite a largura do objeto (em cm): '))
            if largura <= 0:
                mensagemErro()
                continue

        except:
            mensagemErro()
            continue
        
        #o código abaixo segue a mesma ideia do comprimento e da largura, apenas mudando a variável para altura
        try:
            altura = float(input('Digite a altura do objeto (em cm): '))
            if largura <= 0:
                mensagemErro()
                continue
        
        except:
            mensagemErro()
            continue

        #calculando a dimensão do objeto
        dimensoes = altura * comprimento * largura
        print(f'O volume do objeto é (em cm³): {dimensoes:.1f}') #mostrando o volume para o usuário

        #condições para cálculo do valor pelas dimensões
        if dimensoes < 1000: #para dimensões abaixo de 1000
            precoDimensoes4491252 += 10 #adiciona 10 reais ao preço

        elif dimensoes >= 1000 and dimensoes < 10000: #para dimensões entre 1000 e abaixo de 10000
            precoDimensoes4491252 += 20 #adiciona 20 reais ao preço

        elif dimensoes >= 10000 and dimensoes < 30000: #para dimensões entre 10000 e abaixo de 30000
            precoDimensoes4491252 += 30 #adiciona 30 reais ao preço

        elif dimensoes >= 30000 and dimensoes < 100000: #para dimensões entre 30000 e abaixo de 100000
                precoDimensoes4491252 += 50 #adiciona 50 reais ao preço

        else: #caso as dimensões sejam maiores que 100000
            #as seguintes mensagens aparecerão na tela
            print('Não aceitamos objetos com dimensões tão grandes')
            print('Entre com as dimensões novamente')
            continue #volta o looping para o início

        #ao chamar a função, retorna o valor para cálculo final
        return precoDimensoes4491252

#função para coletar o peso do objeto
def pesoObjeto():

    #armazenando peso versus multiplicador
    pesoMultiplicador4491525 = 0
    while True: #criando o looping para adicionar o peso
        try: #tentativa de inserir comprimento
            peso = float((input('Digite o peso do objeto (em kg): '))) #variável que receberá o valor
            if peso <= 0: #tratamento de erro para peso com valor negativo e 0
                mensagemErro2() #mensagem de erro para valores não numéricos no peso
                continue #volta ao início do looping
        
        except: #tratamento de erro valor não numérico
            mensagemErro2() #mensagem de erro para valores não numéricos no peso
            continue #fazendo o looping retornar ao início

        #condições do cálculo do valor por peso
        if peso <= 0.1: #para pesos abaixo de 0.1kg
            pesoMultiplicador4491525 += 1 #adiciona 1 ao multiplicador do peso

        elif peso >= 0.1 and peso < 1: #para pesos entre 0.1 e menores que 1
            pesoMultiplicador4491525 += 1.5 #adiciona 1.5 ao multiplicador do peso

        elif peso >= 1 and peso < 10: #para pesos entre 1 e menores que 10
            pesoMultiplicador4491525 += 2 #adiciona 2 ao multiplicador do peso

        elif peso >= 10 and peso < 30: #para pesos entre 10 e menores que 30
            pesoMultiplicador4491525 += 3 #adiciona 3 ao multiplicador do peso

        else: #caso o peso esteja acima de 30 kg
            #o usuário recebe esta mensagem de erro
            print('Não aceitamos objetos tão pesados')
            print('Por favor entre com o peso desejado novamente')
            pesoObjeto() #chama a função de volta ao início

        #ao chamar a função, retorna o valor para usar no cálculo final
        return pesoMultiplicador4491525

#Função para Selecionar a Rota
def rotaObjeto():

    #armazenando rota versus multiplicador
    rotaMultiplicador4491525 = 0

    #criando o looping para selecionar a rota
    while True:
        #mensagem que aparecerá para o usuário saber quais os valores para cada rota
        print('Selecione a rota:')
        print(' RS - De Rio de Janeiro até São Paulo')
        print(' SR - De São Paulo até Rio de Janeiro')
        print(' BS - De Brasília até')
        print(' SB - De São Paulo até Brasília')
        print(' BR - De Brasília até Rio de Janeiro')
        print(' RB - De Rio de Janeiro até Brasília')
        rota = (input('>> ')) #variável para o usuário digitar a rota que deseja

        #condições para cálculo de valores por rota
        if rota == 'RS' : #se a rota digitada for
            rotaMultiplicador4491525 += 1 #adiciona 1 ao valor do multiplicador da rota
            
        elif rota == 'SR' : #se a rota digitada for
            rotaMultiplicador4491525 += 1 #adiciona 1 ao valor do multiplicador da rota

        elif rota == 'BS' : #se a rota digitada for
            rotaMultiplicador4491525 += 1.2 #adiciona 1.2 ao valor do multiplicador da rota

        elif rota == 'SB' : #se a rota digitada for
            rotaMultiplicador4491525 += 1.2 #adiciona 1.2 ao valor do multiplicador da rota

        elif rota == 'BR' : #se a rota digitada for
            rotaMultiplicador4491525 += 1.5 #adiciona 1.5 ao valor do multiplicador da rota

        elif rota == 'RB' : #se a rota digitada for
            rotaMultiplicador4491525 += 1.5 #adiciona 1.5 ao valor do multiplicador da rota

        else: #caso digite ao diferente dos valores do if e dos elif
            print('Você digitou uma rota que não existe') #mensagem de erro que aparece para o usuário
            continue #volta o looping ao início

        #ao chamar a função, retorna o valor para cálculo final
        return rotaMultiplicador4491525

#realizando o processo
print('Bem vindo a Companhia de Logística Lucas Viganó da Silva S.A.')
dimensoes = dimensoesObjeto() #armazena o valor retornado da função dimensoesObjeto para uma variável que pode ser usada fora da função
peso = pesoObjeto() #armazena o valor retornado da função pesoObjeto para uma variável que pode ser usada fora da função
rota = rotaObjeto() #armazena o valor retornado da função rotaObjeto para uma variável que pode ser usada fora da função

#cálculo do valor total a pagar
valorTotal = (dimensoes) * (peso) * (rota)

#imprimindo o valor a ser pago para o cliente final
print(f'Total a pagar (R$): {valorTotal:.2f} (dimensões: {dimensoes} * peso: {peso} * rota {rota})')