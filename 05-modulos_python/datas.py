from datetime import datetime, timedelta

data = datetime(2019,4,20,10,53,20)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

data = datetime.strptime('12/04/2020','%d/%m/%Y')
#Obter timestamp
print(data.timestamp())

data = datetime.fromtimestamp(1586660400.0)
print(data)

#formatar data
data = datetime.strptime('12/04/2020 20:00:00','%d/%m/%Y %H:%M:%S')
#data = data + timedelta(days=5)
data = data + timedelta(seconds=50*60)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

#manipular
d1 = datetime.strptime('12/04/2020 20:00:00','%d/%m/%Y %H:%M:%S')
print(d1.time())
