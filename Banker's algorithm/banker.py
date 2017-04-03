from processo import Processo
def main():
	processos = []
	continuar = True
	while(continuar):
		print("###Digite os recursos A,B e C da com um espaco entre os numeros###")

		recursos_max_processo 			= input("Quanto de cada recurso cada processo poderia solicitar: ")
		recursos_atuais_processo 		= input("Quanto de cada recurso cada processo atualmente detém: ")
		recursos_disponiveis			= input("Quanto de cada recurso o sistema tem disponível: ")
		
		#fazendo paradinhas...
		recursos_max_processo = recursos_max_processo.split(" ")
		recursos_atuais_processo = recursos_atuais_processo.split(" ")
		recursos_disponiveis = recursos_disponiveis.split(" ")

		#realizando convercao das paradinhas...
		recursos_max_processo = [int(element) for element in recursos_max_processo]
		recursos_atuais_processo = [int(element) for element in recursos_atuais_processo]
		recursos_disponiveis = [int(element) for element in recursos_disponiveis]

		#criacao de um processo...
		processo = Processo(recursos_max_processo, recursos_atuais_processo)
		#processo.__init__(processo, )
		processos.append(processo)

		if(input("Deseja criar outro processo?(1 - sim \ 2 - nao)_ ") != "1"):
			continuar = False 

	for i in range(len(processos)):
		print(Processo.to_string(processos[i]))

	while(True):
		achou = False
		print("\n---			processo #1")
		print("Recurso A do processo: ", recursos_max_processo[0])
		print("Recurso B do processo: ", recursos_max_processo[1])
		print("Recurso C do processo: ", recursos_max_processo[2])
		print("---			Recursos disponiveis")
		print("Recurso A: ", recursos_disponiveis[0])
		print("Recurso B: ", recursos_disponiveis[1])
		print("Recurso C: ", recursos_disponiveis[2])

		for i in range(3):
			atuais = recursos_atuais_processo[i] 		#recursos atuais do processo
			max_recursos = recursos_max_processo[i] 	#maximo derecursos que o processo precisa
			disponivel = recursos_disponiveis[i]		#recursos disponiveis
			if(max_recursos - atuais <= disponivel):
				disponivel += atuais
				recursos_max_processo[i] = 0
				recursos_disponiveis[i] = disponivel
				achou = True
			else:
				break

		if(not achou):
			print("\nEstado nao seguro")
			break
		else:
			print("\nestado seguro")
			break


if __name__ == '__main__':
	main()