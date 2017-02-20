import math
def main():
	cedula = {
	'100':0,'50':0,'20':0,'10':0,'5':0,'2':0,'1':0
	}
	stock = int( input() )
	contabilizar(stock, cedula)

	print(stock)
	print('%d nota(s) de R$ 100,00'%(cedula['100']))
	print('%d nota(s) de R$ 50,00'%(cedula['50']))
	print('%d nota(s) de R$ 20,00'%(cedula['20']))
	print('%d nota(s) de R$ 10,00'%(cedula['10']))
	print('%d nota(s) de R$ 5,00'%(cedula['5']))
	print('%d nota(s) de R$ 2,00'%(cedula['2']))
	print('%d nota(s) de R$ 1,00'%(cedula['1']))

def contabilizar(var,cedula):
	numero = 100
	cont = 0
	while numero > 0:
		if numero != 25:
			cont = var//numero
			cedula[str(numero)] = cont
			var -= cont*numero
			numero = numero//2
		else:
			numero = 20