
var = 'valor' 

def func():
    print(var)

def func2():
    global var # Não é uma boa prática de programação.
    var = 'Outro Valor'
    print(var)

def func3(arg=var):
    arg = arg.replace('v','c')
    return arg

func()
func2()
var2 = func3()
print(var)
print(var2)