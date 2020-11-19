# Import
import random
import math
from datetime import datetime

# Check correct inputs
while True:
	# User input task number
	task_number = input("\nВведи номер завдання від 1 до 4. Якщо хочеш завершити роботи – введи 0: ")

	if task_number.isalpha():  # If letter than repeat input
		print("Потрібно ввести цифру від 1 до 4!")
		continue

	elif int(task_number) == 1:  # Run task 1
		print("\nВиконуємо завдання №1\n")
		random_number = random.randrange(1, 10, 1)  # Random number
		while True:  # Compare random_number with user_number
			user_number = input("Введи число від 1 до 10: ")
			if user_number.isalpha():
				print(f"Потрібно ввести число!")
				continue
			elif int(user_number) == random_number:
				print(f"Вітаю! Ти вгадав!\nПрограма дійсно згенерувала число {user_number}!")
				break
			else:
				print(f"Нажаль, це не число {user_number}. Спробуй ще раз!")
				continue
		continue

	elif int(task_number) == 2:  # Run task 2
		print("\nВиконуємо завдання №2\n")
		user_name = input("Привіт! Як тебе звати? ")
		print(f"Приємно познайомитися, {user_name}")
		# Check correct data
		while True:
			user_birthday = input("Введи свою дату народження (ДД.ММ.РРРР):")
			# Check entered dataformat
			if len(user_birthday) != 10\
				or user_birthday[2] != "."\
				or user_birthday[5] != "."\
				or user_birthday[0: 2].isalpha()\
				or user_birthday[3: 5].isalpha()\
				or user_birthday[6:].isalpha():
				print("Ти використав неправильний формат дати!")
				continue
			# Calculate
			else:
				today = datetime.now()
				birthday = datetime.strptime(user_birthday, "%d.%m.%Y")  # format bithday to DD.MM.YYYY
				age = today - birthday  # calculate full age
				next_birthday = datetime(birthday.year + int(age.days // 365.2425) + 1, birthday.month, birthday.day)
				next_birthday_days = next_birthday - today  # calculate remaining days
				print(f"ОГО! На сьогодні тобі повних аж: "
					f"{int(age.days // 365.2425)} років та "
					f"{int((age.days / 365.2425 - age.days // 365.2425) * 365.2425 // 30)} місяців! "
					f"До {int(age.days // 365.2425 + 1)}-річчя тобі лишилося: {next_birthday_days.days} днів",
					sep=("")
				)
				break
		continue

	elif int(task_number) == 3:  # Run task 3
		print("\nВиконуємо завдання №3\n")
		text = input("Введіть довільний текст: ")
		i = 1
		# random letters from text
		while i <= 5:
			random_text = random.sample(text, k=len(text))
			print(f"Варіант №{i}:", "".join(random_text))
			i += 1
		continue

	elif int(task_number) == 4:  # Run task 4
		print("\nВиконуємо завдання №4\n")
		print("Перевіримо, чи пам'ятаєш ти тригонометрію")
		alpha = math.radians(30)  # translate to degrees
		beta = math.radians(60)  # translate to degrees
		res = math.sin(alpha) * math.cos(beta) + math.cos(alpha) * math.sin(beta)
		print("Дано:\n"
			"\u03B1 = 30\u00B0\n"
			"\u03B2 = 60\u00B0\n"
		)
		user_res = input("Яке значення виразу \x1B[3msin\x1B[23m\u03B1\x1B[3mcos\x1B[23m\u03B2 + "
			"\x1B[3mcos\x1B[23m\u03B1\x1B[3msin\x1B[23m\u03B2 = "
		)  # italic(sin a cos b + cos a sin b)
		if user_res.isalpha():
			print("Результат - це число, а не літера!")
		elif float(user_res) == float(res):
			print("ОГО! Да ти геній!")
		else:
			print(f"Неправильно!\nНічого, я також не знав, поки в Google не спитав. Насправді, значення виразу:\n"
				f"\x1B[3msin\x1B[23m\u03B1\x1B[3mcos\x1B[23m\u03B2 + "
				f"\x1B[3mcos\x1B[23m\u03B1\x1B[3msin\x1B[23m\u03B2 = "
				f"\x1B[3msin\x1B[23m(\u03B1+\u03B2) = \x1B[3msin\x1B[23m(30\u00B0 + 60\u00B0) = 1"
			)  # italic(sin a cos b + cos a sin b = sin(a + b) = sin(30 + 60) = )
		continue

	elif int(task_number) == 0:  # Exit
		print("Бувай! Гарного тобі дня!")
		break

	else:  # if other number input
		print("Такого завдання не існує!")
		continue
