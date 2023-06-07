#RU 4491252

print('Bem vindo a loja do Lucas Viganó da Silva')

#Solicitando os valores
valor = int(input('Entre com o valor do produto: ')) #inserindo valor do produto
qtd = int(input('Entre com a quantidade: ')) #inserindo a quantidade
desc4491252 = 0 #criando a variavel de desconto

#cálculo do preço
preco = valor * qtd

#condições para aplicar o desconto

if qtd <= 9 : #condição em quantidades até 9
    desc4491252 = 1 #como não há desconto, o 1 representa 100% do valor
    #calculando o preço com desconto
    precoDesconto = (valor * qtd) * desc4491252 
    #imprimindo as informações necessárias
    print(f'O valor sem desconto foi: R$ {preco:.2f}') #imprimindo valor sem desconto
    print(f'O valor com desconto foi: R$ {precoDesconto:.2f}   (sem desconto)') #imprimindo valor com desconto

elif qtd >= 10 and qtd <= 99 : #condições entre 10 e 99 unidades
    desc4491252 = 0.95 #0.95 representa 5% de desconto, pois aplica 95% do valor total
    precoDesconto = (valor * qtd) * desc4491252 #calculando preço com desconto
    print(f'O valor sem desconto foi: R$ {preco:.2f}') #imprimindo valor sem desconto
    print(f'O valor com desconto foi: R$ {precoDesconto:.2f}   (desconto de 5%)') #imprimindo valor com desconto

elif qtd >= 100 and qtd <= 999 : #condições entre 10 e 99 unidades
    desc4491252 = 0.9 #0.9 representa 10% de desconto, pois aplica 90% do valor total
    precoDesconto = (valor * qtd) * desc4491252 #calculando preço com desconto
    print(f'O valor sem desconto foi: R$ {preco:.2f}') #imprimindo valor sem desconto
    print(f'O valor com desconto foi: R$ {precoDesconto:.2f}   (desconto de 10%)') #imprimindo valor com desconto

else : #as únicas opções que sobram são de 1000 para cima, por isso utilizei else
    desc4491252 = 0.85 #0.85 representa 15% de desconto, pois aplica 85% do valor total
    precoDesconto = (valor * qtd) * desc4491252 #calculando preço com desconto
    print(f'O valor sem desconto foi: R$ {preco:.2f}') #imprimindo valor sem desconto
    print(f'O valor com desconto foi: R$ {precoDesconto:.2f}   (desconto de 15%)') #imprimindo valor com desconto
