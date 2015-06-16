
import sys

class TextError(Exception):
	pass
class AmountError(Exception):
	pass

def parz_mov(line):
	""" return word and import of a string line"""
	amount = None
	text = []
	line = line.split(" ")
	for token in line:
		try:
			amount = float(token)	
		except ValueError:		
			if token != 'EUR':
				text.append(token)			
	print(amount)	
	if len(text) == 0: #or len(amount) == 0:
		raise TextError('Errore! non hai inserito correttamente il testo ')

	if amount is None:
		raise AmountError('Errore! non hai inserito correttamente l\'importo')

	return text, amount
	
	
def test():
	print('Running tests . . . ')
	assert parz_mov('enel 30.5 EUR') == (['enel'], 30.5)
	assert parz_mov('enel EUR 30.5') == (['enel'], 30.5)
	assert parz_mov('enel 30.5 elettricita') == (['enel', 'elettricita'], 30.5)
	print ('All tests ok!')

if __name__ == "__main__":

    if len(sys.argv) == 1:
        test()
        sys.exit(0)


    in_file = sys.argv[1]


    		