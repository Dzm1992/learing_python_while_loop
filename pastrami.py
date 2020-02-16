#7.9

sandwich_orders = ['Kanapka_1', 'Kanapka_Pastrami', 'Kanapka_2', 'Kanapka_Pastrami', 'Kanapka_3', 'Kanapka_Pastrami', 'Kanapka_4', 'Kanapka_5']

print(sandwich_orders)
print("\n")

print("W barze skonczylo sie pastrami")

while 'Kanapka_Pastrami' in sandwich_orders:
	sandwich_orders.remove('Kanapka_Pastrami')

print("\n")
print(sandwich_orders)
	

