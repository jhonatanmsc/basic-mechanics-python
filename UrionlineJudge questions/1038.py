# Autor: Jhonatan Matheus
# 20/02/2017

def main():
	codigos = {'1':4.00, '2':4.50, '3':5.0, '4':2.0, '5':1.50}
	total = 0
	num = input().split(' ')

	total = codigos[num[0]]*int( num[1] )

	print('Total: R$ %.2f'% total)

if __name__ == '__main__':
	main()