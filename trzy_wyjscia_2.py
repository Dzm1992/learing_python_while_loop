#7.6b

wiadomosc = "Proszę wybierz swój dodatek do pizzy. "
wiadomosc += "\nJesli chces zakonczyc wpisz koniec: "
dodatek = ""


while dodatek != 'koniec':
	dodatek = input(wiadomosc)
	if dodatek != 'koniec':
		print(dodatek)
