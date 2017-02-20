# Autor: Jhonatan Matheus
# 20/02/2017

def main():

	km = int( input() )
	consumo = float( input() )

	resultado = km/consumo

	print('%.3f km/l'%resultado)


if __name__ == '__main__':
	main()