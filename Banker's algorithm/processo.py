
class Processo(object):
	
	def __init__(self, max_recursos, atuais_recursos):
		#super(Processo, self).__init__(self)
		self._max_recursos = max_recursos
		self._atuais_recursos = atuais_recursos

	def to_string(self):
		print("Quantos processos requer: ", self._max_recursos, "\nQuantos processos tem: ", self._atuais_recursos)