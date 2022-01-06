import random 
import string

#Gera um número inteiro entre A e B
inteiro = random.randint(10,20)

# Gera um numero de ponto flutuante 
flutuante = random.uniform(10,20)

#Gera um numero de ponto flutuante de 0 e 1
flutuante02 = random.random()

#Gera um número aleatório entre 9000 e 1000 usando a função range()
inteiro02 = random.randrange(900,1000,10)

#print( inteiro )
#print( inteiro02 )
#print( flutuante )
#print( flutuante02 )

lista  = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']

#sorteio = random.choice(lista) # Seleciona aleatório
#sorteio2 = random.choices(lista, k=2) # Permite escolher + 01 
#sorteio3 = random.sample(lista, k=2) # Não repete
#
#print(sorteio)
#print(sorteio2)
#print(sorteio3)

#Embaralhar uma lista. 
#random.shuffle(lista)
#print(lista)


letras = string.ascii_letters
digitos = string.digits
caracteres = '!#$%&*()+_@.'
geral = letras + digitos + caracteres

senha = "".join(random.choices(geral, k=20))


print(senha)