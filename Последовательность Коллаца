# Функция будет использована для проверки введённых пользователем данных на целочисленность. 
def isint(value):
	try:
		int(value)
		return True
	except:
		return False
		
# Функция обрабатывает введённое пользователем число согласно гипотезе Коллатца 
def collatz():
	global number
	if number % 2 == 0:
		number = number // 2
		print(number)
	else:
		number = number * 3 + 1
		print(number)

# Блок запроса целого числа и проверки на целочисленность
number = input("Введите целое число: ")
while not isint(number):
	number = input("Нужно ввести именно целое число: ")
number = int(number)

# Вычисление последовательности Коллатца
while number != 1:
	collatz()
