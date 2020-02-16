#7.5


prompt = "Podaj swój wiek: "
prompt_2 = "Czy chcesz zakonczyc dzialanie programu? Wpisz 'tak' jesli chcesz zakonczyc: "


while True:
	wiek = input(prompt)
	wiek = int(wiek)
	
	if wiek < 3:
		print("Bilet jest bezłatny!")
	elif wiek < 12:
		print("Bilet kosztuje 10 zł!")
	elif wiek > 12:
		print("Bilet kosztuje 15 złotych!")
	
	zakonczenie = input(prompt_2)
	
	if zakonczenie == 'tak':
		break
		
	
