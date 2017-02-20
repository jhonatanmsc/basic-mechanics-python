# Autor: Jhonatan Matheus
# 20/02/2017

import math
def main():

	pontos_1 = input().split(' ')
	pontos_2 = input().split(' ')
	pontos_1[0], pontos_2[0] = float(pontos_1[0]), float(pontos_2[0])
	pontos_1[1], pontos_2[1] = float(pontos_1[1]), float(pontos_2[1])

	resultado = math.sqrt( ((pontos_1[0]-pontos_2[0])**2)+((pontos_1[1]-pontos_2[1])**2) )

	print('%.4f'%resultado)


if __name__ == '__main__':
	main()