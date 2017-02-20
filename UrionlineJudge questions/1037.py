# Autor: Jhonatan Matheus
# 20/02/2017

def main():
	num = float( input() )

	if(num >100):
		print("Fora de intervalo")
	elif(num>75):
		print("Intervalo (75,100]")
	elif(num>50):
		print("Intervalo (50,75]")
	elif(num>25):
		print("Intervalo (25,50]")
	elif(num>=0):
		print("Intervalo [0,25]")
	else:
		print("Fora de intervalo")


if __name__ == '__main__':
	main()