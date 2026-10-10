password = "сокровище"
answer = input("Введи начало пароля (первые 3 буквы): ").lower().strip()

if answer == password[0:3]:
    print("Дверь открылась!")
else:
    print("Неверно. Дверь осталась закрытой.")
