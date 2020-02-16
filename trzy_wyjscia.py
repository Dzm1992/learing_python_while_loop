#7.6

wiadomosc = "Proszę wybierz swój dodatek do pizzy. "
wiadomosc += "\nJesli chces zakonczyc wpisz koniec: "
dodatek = ""
active = 'True'

while active:
	dodatek = input(wiadomosc)
	
	if dodatek == 'koniec':
		active = False
	else:
		print(dodatek)
