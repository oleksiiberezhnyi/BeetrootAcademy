# Task 1
# Input string
s = input("Введіть строку: ")

if len(s) >= 2:
    s1 = s[0] + s[1]
    s2 = s[-2] + s[-1]
    print(f"{s1}{s2}")
else:
    print("Empty String")

print("\n")
# Task 2
# Input telephone
tel = input("Введіть номер телефону: +38")

if tel.isdecimal and len(tel) == 10:
    print("Ваш телефон: +38", tel, sep="")
else:
    print("Ви ввели неправильний номер!")
print("\n")
# Task 3
# Set name
name = "oleksii"
# Input name
sname = input("Введіть ваше ім'я: ")
if name == sname.lower():
    print("Ваш результат TRUE")
else:
    print("Ви ввели неправильне ім'я!")
