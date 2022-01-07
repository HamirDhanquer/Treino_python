# Funções anônimas - sem nome 

def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)

#Expressões Lambda - A mesma função 

a = lambda x, y: x * y
#print( a(2, 2) )

lista = [
    ["P1", 13],
    ["P2", 6],
    ["P3", 7],
    ["P4", 50],
    ["P5", 8],
]

print(lista)

lista.sort()
print(lista)

def ord(item):
    return item[1]

lista.sort( key=ord, reverse=True ) #Editar lista original 
#print(lista)

#Fazendo a mesma coisa utilizando expressões lambda

lista.sort(key=lambda item: item[1], reverse=False)
print(lista)

print(sorted(lista, key=lambda i:i[0] )) # sem editar a lista original. 

