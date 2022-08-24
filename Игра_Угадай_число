# Подготовка к программе
import random

no = ["Нет", "нет", "Не-а", "не-а", "неа", "Не", "не"]

def isint(value):
	try:
		int(value)
		return True
	except:
		return False

# Чтобы можно было играть сколько душе угодно
while input("Играем? ") not in no:
	
	# Подготовка к игре
	secret_number = random.randint(1, 20)
	print("Я загадал число от одного до двадцати. Попробуйте угадать это число за шесть попыток. Каждый раз я буду говорить, больше или меньше вашего моё число, либо скажу, что вы угадали.")
	
	# Игра
	for token in range(1, 7):
		number = input("Ваш вариант: ")
		while not isint(number):
			number = input("Надо написать целое число цифрами: ")
		number = int(number)
		if number < secret_number:
			print("Загаданное число больше")
		elif number > secret_number:
			print("Загаданное число меньше")
		else:
				break
	
	# Подведение итогов
	if number == secret_number:
		print("Вы угадали число! Количество попыток — " + str(token))
	else:
		print("Вам не удалось угадать число. Загаданное число — " + str(secret_number))
	print()
	print()
	print()
