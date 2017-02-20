def main():
	vet = [365, 30]
	stock = int( input() )
	
	print( "%d ano(s)"%(stock/365) )
	stock = stock%365
	print( "%d mes(es)"%(stock/30) )
	stock = stock%30 
	print( "%d dia(s)"%(stock) )


if __name__ == '__main__':
	main()