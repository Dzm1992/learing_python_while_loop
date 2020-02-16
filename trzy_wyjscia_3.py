#7.6c

wiadomosc = "Proszę wybierz swój dodatek do pizzy. "
wiadomosc += "\nJesli chces zakonczyc wpisz koniec: "
dodatek = ""


while True:
	dodatek = input(wiadomosc)
	if dodatek == 'koniec':
		break
