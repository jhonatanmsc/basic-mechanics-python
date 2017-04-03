
class Processo(object):
	
	def __init__(self, max_processo, atuais_processo):
		#super(Processo, self).__init__(self)
		self._max_processo = max_processo
		self._atuais_processo = atuais_processo

	def to_string(self):
		print("Quantos processos requer: ", self._max_processo, "\nQuantos processos tem: ", self._atuais_processo)