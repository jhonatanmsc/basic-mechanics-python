import math
def main():
	cedula = [10000, 5000, 2000, 1000, 500, 200]
	moedas = [100, 50, 25, 10, 5, 1]

	stock = float( input() )
	cents = stock*100
	print('NOTAS:')
	for i in range(6):
		print( "%d nota(s) de R$ %.2f"%( cents/cedula[i], cedula[i]/100) )
		cents = (cents)%cedula[i]
	print('MOEDAS:')
	for i in range(6):
		print( "%d moeda(s) de R$ %.2f"%(cents/moedas[i], moedas[i]/100) )
		cents = (cents)%moedas[i]



if __name__ == '__main__':
	main()