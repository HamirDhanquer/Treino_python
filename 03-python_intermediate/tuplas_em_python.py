# Tupla não é variável. Não pode editar. 

t3 = ()
t1 = (1,2,3,4,5,'Hamir')
t2 = 10,20,30,40,"Custom"
t4 = t1 + t2 


print( type(t1) )
print( t1[4] )
print( t1[2:] )

for v in t1:
    print(v)

print(t2)
print(t4)

n1, n2, n3, *_, n10, n11 = t1  
print(n11)


#Convertendo tupla para lista 

t5 = list(t3)
print(type(t5))
t5 = tuple(t3)
print(type(t5))

