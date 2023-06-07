#RU 4491252

#criando a lista dos produtos
listaProdutos = []

#imprimindo a saudação com o identificador pessoal
print(' ')
print('Bem Vindo ao Controle de Estoque da Bicicletaria do Lucas Viganó da Silva')

#declarando função para cadastrar peças
def cadastrarPeca(contador):
    produto = {} #criando um dicionário vazio para adicionar os produtos
    produto['codigo'] = contador #o código do produto receberá a variável contador e será adicionado ao dicionário na chave 'código'
    produto['nome'] = input('Por favor entre com o NOME da peça: ') #entrada para adicionar o nome do produto ao dicionário na chave 'nome'
    produto['fabricante'] = input('Por favor entre com o FABRICANTE da peça: ') #entrada para adicionar o fabricante do produto ao dicionário na chave 'fabricante'
    produto['valor'] = float(input('Por favor entre com o VALOR da peça: ')) #entrada para adicionar o valor do produto ao dicionário na chave 'valor'
    listaProdutos.append(produto.copy()) #colocando os itens adicionados como último elemento dentro da lista

#declarando a função para consultar peças
def consultarPeca():
    print('Você selecionou a Opção de Consultar Peças') #mensagem que aparecerá para o usuário

    #cria um looping para realizar as consultas até que o usuário digite 4 para retornar ao menu principal
    while True:
        #menu das opções de escolhas de consulta
        print('Escolha a opção desejada')
        print('1 - Consultar Todas as Peças')
        print('2 - Consultar Peças por Código')
        print('3 - Consultar Peças por Fabricante')
        print('4 - Retornar')

        #local onde o usuário digitará a opção desejada
        opcaoConsulta = (input('>> '))

        #condições para cada opção escolhida
        if opcaoConsulta == '1': #caso escolha a opção 1
            print('-'*20) #impressão para melhorar o visual
            for produto in listaProdutos: #for usado para fazer a varredura entre os produtos, mostrando todos que estão dentro da lista
                #o print apresenta a lista com os dicionários, cada dicionário é um produto, os \n tornam mais fácil visualizar cada chave
                print('Código: ', produto['codigo'],
                '\nNome : ', produto['nome'],
                '\nFabricante: ', produto['fabricante'],
                '\nValor: ', produto['valor'])
                print('-'*20) #impressão para melhorar o visual
        
        elif opcaoConsulta == '2': #caso escolha a opção 2
            codigoConsulta = int(input('Digite o CÓDIGO da Peça: ')) #será necessário o usuário digitar o código do produto, o qual será armazenado numa variável
            encontrado = False #setando a variável como False
            for produto in listaProdutos: #o for realiza a varredura entre os produtos, identificando todos que estão na lista
                if produto['codigo'] == codigoConsulta: #caso o código digitado seja igual o valor dentro da chave 'codigo'
                    #será apresentado um print mostrando todos os produtos com aquele código, apresentando todas as informações sobre ele
                    print('-'*20)
                    print('Código: ', produto['codigo'],
                        '\nNome : ', produto['nome'],
                        '\nFabricante: ', produto['fabricante'],
                        '\nValor: ', produto['valor'])
                    print('-'*20)
                    encontrado = True #quando encontrado o código, a variável é setada para True, o programa só mostra os produtos que forem encontrados, ignorando os que não foram encontrados
                
            #tratamento de erro
            if not encontrado: #caso o código não seja encontrado na varredura do for, a mensagem de erro a seguir aparece
                print('-'*20)
                print('Código não encontrado')
                print('-'*20)
        
        elif opcaoConsulta == '3': #caso escolha a opção 3
            fabricanteConsulta = (input('Digite o FABRICANTE da Peça: ')) #será necessário o usuário digitar o fabricante do produto, o qual será armazenado numa variável
            encontrado = False #setando a variável como False
            for produto in listaProdutos: #o for realiza a varredura entre os produtos, identificando todos que estão na lista
                if produto['fabricante'] == fabricanteConsulta: #caso o fabricante digitado seja igual o valor dentro da chave 'fabricante'
                    #será apresentado um print mostrando todos os produtos com aquele fabricante, apresentando todas as informações sobre ele
                    print('-'*20)
                    print('Código: ', produto['codigo'],
                        '\nNome : ', produto['nome'],
                        '\nFabricante: ', produto['fabricante'],
                        '\nValor: ', produto['valor'])
                    print('-'*20)
                    encontrado = True #quando encontrado o código, a variável é setada para True, o programa só mostra os produtos que forem encontrados, ignorando os que não foram encontrados
            
            #tratamento de erro
            if not encontrado: #caso o fabricante não seja encontrado na varredura do for, a mensagem de erro a seguir aparece
                print('-'*20)
                print('Fabricante não encontrado')
                print('-'*20)
        
        elif opcaoConsulta == '4': #caso a opção escolhida seja 4
            return #o programa retorna para o menu principal, saindo do looping das consultas
        
        else: #caso a digite um número diferente dos apresentados no if e elif, a seguinte mensagem aparecerá
            print('Opção não encontrada')

#função para remover peças
def removerPeca():
    try: #o Python tenta realizar a operação abaixo
        print('Você Selecionou a Opção de Remover Peça')
        num = int(input('Digite o código da peça a ser removida: ')) - 1 # a variável num armazena o código que o usuário digitar da peça que deseja remover (o -1 é usado pois o dicionário contendo todo o produto código 1 representa o elemento 0 dentro da lista)
        del listaProdutos[num] #deleta o elemento da lista na posição num, ou seja, se o usuário digitar 1, num se torna 0, deletando o primeiro elemento da lista
    
    except: #tratamento de erro caso o usuário digite um código que não existe na lista
        print('Código não encontrado')

#contador para identificar os códigos de cada produto
contador = 0

#looping para as opções do menu principal
while True :
    #menu principal
    print('Escolha a opção desejada')
    print('1 - Cadastrar Peças')
    print('2 - Consultar Peças')
    print('3 - Remover Peças')
    print('4 - Sair')

    #usuário digita a oção e a variável armazena a opção desejada
    opcao4491252 = (input('>> '))

    #condições para cada opção selecionada
    if opcao4491252 == '1': #caso escolha a opção 1
        contador += 1 #o contador dos códigos somará +1 a ele mesmo a cada produto adicionado
        print('Você selecionou a Opção de Cadastrar Peça') #mensagem para o usuário
        print(f'Código da Peça: 00{contador}') #print mostrando o código da peça adicionada
        cadastrarPeca(contador) #aqui chamamos a função que realiza toda a operação de cadastro das peças

    elif opcao4491252 == '2': #caso escolha a opção 2
        consultarPeca() #chamamos a função para realizar toda a operação de cadastro de peças

    elif opcao4491252 == '3': #caso escolha a opção 3
        removerPeca() #chamamos a função para realizar toda a operação de remoção de peças

    elif opcao4491252 == '4': #caso escolha a opção 4
        break #o programa é encerrado

    else: #caso o usuário digite algum número diferente dos disponíveis, a mensagem de erro aparece na tela
        print('Opção não existente') #mensagem de erro