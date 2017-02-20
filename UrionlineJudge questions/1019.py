# Autor: Jhonatan Matheus
# 20/02/2017

import math
def main():
	
	stock = int( input() )
	
	print('%d:%d:%d'%(stock/3600, (stock%3600)/60, (stock%3600)%60))

if __name__ == '__main__':
	main()