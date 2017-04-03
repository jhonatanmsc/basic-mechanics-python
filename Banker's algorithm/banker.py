from processo import Processo
def main():
	processos = []
	continuar = True

	print("###Digite a quantidade dos recursos A,B e C com um espaco entre os numeros###")
	recursos_disponiveis = input("Quanto de cada recurso o sistema tem disponível: ")
	recursos_disponiveis = recursos_disponiveis.split(" ")
	recursos_disponiveis = [int(element) for element in recursos_disponiveis]

	while(continuar):
		recursos_max_processo 			= input("Quanto de cada recurso este processo poderia solicitar: ")
		recursos_atuais_processo 		= input("Quanto de cada recurso este processo atualmente detém: ")
		
		#fazendo paradinhas...
		recursos_max_processo = recursos_max_processo.split(" ")
		recursos_atuais_processo = recursos_atuais_processo.split(" ")

		#realizando convercao das paradinhas...
		recursos_max_processo = [int(element) for element in recursos_max_processo]
		recursos_atuais_processo = [int(element) for element in recursos_atuais_processo]

		#criacao de um objeto so pra manipular...
		processo = Processo(recursos_max_processo, recursos_atuais_processo)

		#colocando em uma lista...
		processos.append(processo)

		if(input("Deseja criar outro processo?(1 - sim \ 2 - nao)_ ") != "1"):
			continuar = False 

	for i in range(len(processos)-1):
		print(Processo.to_string(processos[i]))

	while(len(processos) > 0):
		for i in range(len(processos)):
			deadlock = 0
			print("\n---			informacoes do processo: ")
			print("Recurso A do processo: ", processos[it]._max_recursos[0])
			print("Recurso B do processo: ", processos[it]._max_recursos[1])
			print("Recurso C do processo: ", processos[it]._max_recursos[2])

			for j in range(len(processos._max_recursos)):
				atuais = processos[i]._atuais_recursos[j] 				#recursos atuais do processo
				max_processo_recursos = processos[i]._max_recursos[j] 	#maximo derecursos que o processo precisa
				disponivel = recursos_disponiveis[j]					#recursos disponiveis
				if(not(max_processo_recursos - atuais <= disponivel)):
					deadlock += 1
					break

			if(deadlock == 0):
				for d in range(len(recursos_disponiveis)):
					recursos_disponiveis[d] += processos[j]._atuais_recursos[d]


			print("---			Recursos disponiveis")
			print("Recurso A: ", recursos_disponiveis[0])
			print("Recurso B: ", recursos_disponiveis[1])
			print("Recurso C: ", recursos_disponiveis[2])

		if(achou):
			processos.pop(it)
			break
		else:

			


if __name__ == '__main__':
	main()