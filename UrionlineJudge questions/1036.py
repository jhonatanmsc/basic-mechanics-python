import math
def main():
	num = input().split(' ')
	A, B, C = float( num[0] ), float( num[1] ), float( num[2] )

	delta = B**2 - 4*(A*C)
	if (A != 0)and(delta > 0):
		X1 = (-B + math.sqrt(delta))/(2*A)
		X2 = (-B - math.sqrt(delta))/(2*A)
		print('R1 = %.5f'%(X1))
		print('R2 = %.5f'%(X2))
	else:
		print('Impossivel calcular')

if __name__ == '__main__':
	main()