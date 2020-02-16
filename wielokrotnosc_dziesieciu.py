#7.3

liczba = input("Spradź, czy dana liczba jest wielokrotnością 10! Podaj liczbę: ")
liczba = int(liczba)

if liczba % 10 == 0:
	liczba = str(liczba)
	print(liczba + " jest wielokrotnościa 10!")
else:
	liczba = str(liczba)
	print(liczba + " nie jest wielokrotnościa 10!")
