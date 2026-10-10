import random

health = 100
mana = 50


def attack():
    damage = random.randint(10, 30)
    return damage


def magic():
    damage = random.randint(20, 40)
    return damage


def enemy_attack():
    damage = random.randint(5, 20)
    return damage


print("=== ВЫЖИТЬ В НПК ===")
print("Ты оказался в политехе.")

name = input("Как тебя зовут? ")
print("Привет,", name + "!")

print("\nТвоё здоровье:", health)
print("Твоя мана:", mana)

choice = input("\nТы видишь кабинет. Войти? (да/нет): ")

if choice == "да":

    print("\nТам оказался злой перпод")
    enemy_health = 50

    while health > 0 and enemy_health > 0:

        print("\nТвоё здоровье:", health)
        print("Твоя мана:", mana)
        print("Здоровье монстра:", enemy_health)

        print("\n1 - Обычная атака")
        print("2 - СУПЕР атака")

        action = input("Выбери действие: ")

        if action == "1":
            damage = attack()
            enemy_health -= damage
            print("Ты нанёс", damage, "урона!")

        elif action == "2":

            if mana >= 10:
                mana -= 10
                damage = magic()
                enemy_health -= damage
                print("Ты использовал СУПЕР!")
                print("Ты нанёс", damage, "урона!")
            else:
                print("Недостаточно маны!")

        else:
            print("Неверный выбор!")

        if enemy_health > 0:
            damage = enemy_attack()
            health -= damage
            print("Волков нанёс тебе", damage, "урона!")

    if health <= 0:
        print("\nТы проиграл!")

    elif enemy_health <= 0:
        print("\nТы победил его")
        print("Ты прошёл квест, но какой ценой?")

else:
    print("\nТы решил не заходить в кабинет.")
    print("Квест окончен. Ты выжил")