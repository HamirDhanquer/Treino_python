from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

dt = datetime.now()
mes_atual = int( dt.strftime("%m") )
format_dt = dt.strftime("%A, %d de %B de %Y")
format_dt02 = dt.strftime("%d/%m/%Y %H:%M:%S")
print(format_dt)
print(format_dt02)
print(mes_atual, mdays[mes_atual]) #Identificar os últimos dia do mês 