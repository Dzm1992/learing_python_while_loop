#7.8

sandwich_orders = ['Kanapka_1', 'Kanapka_2', 'Kanapka_3', 'Kanapka_4', 'Kanapka_5']
print(sandwich_orders)

finished_sandwiches = []

while sandwich_orders:
	current_kanapka = sandwich_orders.pop()
	finished_sandwiches.append(current_kanapka)
	print(current_kanapka + " jest gotowa! Przechodzimy do zrobienia kolejnej!")

finished_sandwiches.sort()
finished_sandwiches.sort(reverse=True)
finished_sandwiches.reverse()
len(finished_sandwiches)
print(sorted(finished_sandwiches))

print("\nKanapki sa gotowe:")
print(finished_sandwiches)
		
