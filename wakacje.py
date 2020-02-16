#7.10


wyniki_ankiety = {}

while True:
	osoba = input("Podaj swoje imie: ")
	miejsce = input("Podaj miejsce, do ktorego chcialbys udac sie na wakacje: ")
	
	wyniki_ankiety[osoba] = miejsce
	
	Zakonczenie_ankiety = input('Czy chcesz zrezygnowac? (T/N) ')
	if Zakonczenie_ankiety == 'T':
		break
	
print("\n--- Wyniki ankiety ---")
for name, place in wyniki_ankiety.items():
	print(name + " chce udac sie na wakacje do: " + place)

	
	
	
	
