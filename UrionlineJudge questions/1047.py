# Autor: Jhonatan Matheus
# 20/02/2017

def main():
	
	word = input().split(' ')

	for i in range(4):
		word[i] = int(word[i])

	word[0] *= 60
	word[2] *= 60

	hr_ini = word[0]+word[1]
	hr_fim = word[2]+word[3]

	if hr_ini >= hr_fim:
		hr_fim += 1440

	print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)'%( (hr_fim - hr_ini)/60, (hr_fim - hr_ini)%60 ))

if __name__ == '__main__':
	main()