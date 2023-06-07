#RU 4491252

#função para mostrar cardápio
def mostrarCardapio() :
    print("""
            **********Cardápio**********

    | Código |	     Descrição	       | Valor(R$) |
    |   100  |	   Cachorro-Quente     |    9,00   |
    |   101  |	Cachorro-Quente Duplo  |   11,00   |
    |   102  |	       X-Egg	       |   12,00   |
    |   103  |	      X-Salada	       |   13,00   |
    |   104  |	       X-Bacon	       |   14,00   |
    |   105  |	       X-Tudo	       |   17,00   |
    |   200  |	 Refrigerante Lata     |    5,00   |
    |   201  |	    Chá Gelado	       |    4,00   |
    """)

#criando o menu
print('Bem Vindo a Lanchonete do Lucas Viganó da Silva')
mostrarCardapio() #chamando a função para mostrar cardápio

#inserindo código para pedido e calculando o valor total
codigo = int(input('Entre com o código desejado: '))
precoTotal4491252 = 0 #criando a variável para cálculo do preço total
        
#looping dos pedidos
while codigo >= 0 : #o looping acontece quando o código for maior digitado for maior que 0, auxiliando no tratamento de dados
    if codigo == 100 : #caso digite o código 100
        preco = 9.00 #é armazenado o preço de 9 reais
        precoTotal4491252 += preco #o preço é adicionado ao preço total
        #imprimindo as informações que aparecerá para o consumidor
        print('Você pediu um Cachorro-Quente no valor de 9,00')
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        opcao = int(input('>> ')) #criando a variável para escolher se deseja fazer mais pedidos

    #o código abaixo segue a mesma ideia do código 100
    elif codigo == 101 :
        preco = 11.00
        precoTotal4491252 += preco
        print('Você pediu um Cachorro-Quente Duplo no valor de 11,00')
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        opcao = int(input('>> '))
    
    #o código abaixo segue a mesma ideia do código 100
    elif codigo == 102 :
        preco = 12.00
        precoTotal4491252 += preco
        print('Você pediu um X-Egg no valor de 12,00')
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        opcao = int(input('>> '))

    #o código abaixo segue a mesma ideia do código 100
    elif codigo == 103 :
        preco = 13.00
        precoTotal4491252 += preco
        print('Você pediu um X-Salada no valor de 13,00')
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        opcao = int(input('>> '))
    
    #o código abaixo segue a mesma ideia do código 100
    elif codigo == 104 :
        preco = 14.00
        precoTotal4491252 += preco
        print('Você pediu um X-Bacon no valor de 14,00')
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        opcao = int(input('>> '))
    
    #o código abaixo segue a mesma ideia do código 100
    elif codigo == 105 :
        preco = 17.00
        precoTotal4491252 += preco
        print('Você pediu um X-Tudo no valor de 17,00')
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        opcao = int(input('>> '))
    
    #o código abaixo segue a mesma ideia do código 100
    elif codigo == 200 :
        preco = 5.00
        precoTotal4491252 += preco
        print('Você pediu um Refrigerante Lata no valor de 5,00')
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        opcao = int(input('>> '))
    
    #o código abaixo segue a mesma ideia do código 100
    elif codigo == 201 :
        preco = 4.00
        precoTotal4491252 += preco
        print('Você pediu um Chá Gelado no valor de 4,00')
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        opcao = int(input('>> '))
    
    else : #caso o código digitado seja diferente dos valores anteriores
        print('Opção Inválida') #será impresso uma opção inválida
        codigo = int(input('Entre com o código desejado: ')) #o usuário poderá digitar o código novamente
        continue #o continue da seguimento ao looping

    #criando as opções de pedir mais e encerrar pedido
    if opcao == 1 : #caso a opção ao fazer um pedido seja 1
        #o usuário poderá digitar o código novamente
        codigo = int(input('Entre com o código desejado: '))
    
    elif opcao == 0 : #caso a opção ao fazer um pedido seja 0
        print(f'Valor total a ser pago é: {precoTotal4491252:.2f}') #será impresso o valor a ser pago
        break #o break encerra o programa

    else : #caso o usuário digite algo diferente de 0 ou 1
        #a mensagem do pedido é repetida
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        int(input('>> ')) #o usuário irá digitar a opção aqui, dando continuidade ao looping