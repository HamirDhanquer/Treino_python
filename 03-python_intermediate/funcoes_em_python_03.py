"""
Funções def em Python - *args **kwargs
"""

''' Funções nomeadas 

def func( a1, a2, a3, a4, a5, nome=None, a6=None ):
    print( a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

var = func(1,2,3,4,5, nome='Hamir', a6=None )
print(var)
'''

'''
lista = [1,2,3,4,5]
n1, n2, *n = lista #desempacotou na última. 
print(lista)

lista = [1,2,3,4,5]
print(*lista, sep='-') #desempacotou a lista 
'''

''' Entendendo listas e tuplas. 
def func(*args):
    args = list(args) #Convertendo uma tupla para lista 
    print( args )
    print( args[0] )
    print( args[-1] )
    print( len(args) )
    
    for v in args:
        print(v)

#func(1,2,3,4,5)
'''

''' Explicando lista desempacotada.
def func(*args, **kwargs):
    print( args )

lista = [1,2,3,4,5]
lista2 = [100,200,300,400,500]
func(*lista,10,20,30,*lista2) #Lista desempacotada. 
'''


def func(*args, **kwargs): #argumentos nomeados
    print( args )
    print( kwargs )
    print( kwargs['nome'] )

    sobrenome = kwargs.get('sobrenome')
    print(sobrenome)

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else: 
        print('Idade não existe')


lista = [1,2,3,4,5]
func(*lista,nome='Hamir',sobrenome='Noleto', idade=32) #Lista desempacotada. 