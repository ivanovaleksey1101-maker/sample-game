from coloriestili import Color, сброс
from random import randint, random, choice
from time import sleep

текст = Color.зеленый
обычный = сброс
редкий = Color.желтый
опасно = Color.красный
легендарный = Color.голубой
print(текст, end="")

enemies = [
    {'имя': f"{обычный}Гоблин", 'урон': 6, 'хп': 15, 'шанс попадания по нему': 100, 'тип': "обычный"},
    {'имя': f"{обычный}Волк", 'урон': 8, 'хп': 9, 'шанс попадания по нему': 80, 'тип': "обычный"},
    {'имя': f"{обычный}Лиса", 'урон': 7, 'хп': 6, 'шанс попадания по нему': 70, 'тип': "обычный"},
    {'имя': f"{обычный}Дикарь", 'урон': 6, 'хп': 14, 'шанс попадания по нему': 95, 'тип': "обычный"}
]

enemies_hard = [
    {'имя': f"{редкий}Разбойник", 'урон': 8, 'хп': 25, 'шанс попадания по нему': 95, 'тип': "редкий"},
    {'имя': f"{редкий}Гоблин Шахтёр", 'урон': 10, 'хп': 20, 'шанс попадания по нему': 100, 'тип': "редкий"},
    {'имя': f"{редкий}Древний Волк", 'урон': 10, 'хп': 12, 'шанс попадания по нему': 70, 'тип': "редкий"}
]

player = {
    'урон': 5,
    'хп': 20,
    'макс_хп': 20,
    'монет': 90
}

inventory = ["Малое зелье исцеления", "Точный сломаный кинжал"]

def atack(damage, log=False):
	result = damage
	result = max(0.1, result)
	if log:
		print(f"Default damage: {damage}")
	result += (randint(-damage, damage) * 0.5) / 10
	while damage == result:
		result += (randint(-damage, damage) * 0.5) / 10
	if log:
		print(f"Random damage (±5%): {result:.2f} ({(-damage * 0.5) / 10} - {(damage * 0.5) / 10})")
	result = int((result * 0.9) * 100) / 100
	result = max(0.1, result)
	if log:
		print(f"Post-processing: {result}")
	return result

def shop():
    price_mzi = randint(35, 40)
    price_bzi = randint(70, 95)
    price_ok = randint(100, 125)
    price_zzh = randint(120, 150)
    price_m = randint(130, 170)
    items = []
    for _ in range(randint(1, 5)):
        items.append(choice([{"Острый кинжал": price_ok}, {"Малое зелье исцеления": price_mzi}, {"Большое зелье исцеления": price_bzi}, {"Меч": price_m}, {"Зелье живучести": price_zzh}]))
    while True:
        print(f"{редкий}Торговец{текст}: Здравствуй, {обычный}странник{текст}! Что хочешь приобрести или продать?")
        print("\nВведите:")
        print("1. Купить")
        print("2. Продать")
        print("3. Уйти")
        print(f"4. Сражатся с {редкий}Торговцем{текст}")
        act = input(">>> ").strip()
        sleep(0.5)
        
        if act == "1":
            print(f"\n{редкий}Торговец{текст}: Вот мой товар!")
            sleep(1)
            for i, item_dict in enumerate(items):
                for item_name, price in item_dict.items():
                    sleep(0.5)
                    print(f"{i+1}. {item_name}: {price} монет")
            
            print(f"\nУ {обычный}тебя{текст} есть {player['монет']} монет")
            print("Выбери товар для покупки (или 0 чтобы отменить)")
            try:
                choice_num = int(input(">>> ").strip())
                if choice_num == 0:
                    continue
                if 1 <= choice_num <= len(items):
                    selected_item = items[choice_num-1]
                    item_name, price = list(selected_item.items())[0]
                    if player['монет'] >= price:
                        player['монет'] -= price
                        inventory.append(item_name)
                        print(f"{обычный}Ты{текст} купил {item_name} за {price} монет!")
                        items.pop(choice_num-1)  # Убираем предмет из асортимента торговца
                    else:
                        print("У вас недостаточно монет!")
                else:
                    print("Неверный выбор!")
            except ValueError:
                print("Пожалуйста, введи число!")
                
        elif act == "2":
            if not inventory:
                print(f"У {обычный}тебя{текст} нет предметов для продажи!")
                continue
                
            print("\nВаши предметы:")
            for i, item in enumerate(inventory):
                sleep(0.5)
                print(f"{i+1}. {item}")
            
            print("\nВыбери предмет для продажи (или 0 чтобы отменить)")
            try:
                choice_num = int(input(">>> ").strip())
                sleep(0.5)
                if choice_num == 0:
                    continue
                if 1 <= choice_num <= len(inventory):
                    item = inventory[choice_num-1]
                    if item == "Малое зелье исцеления":
                        price = 15
                    elif item == "Точный сломаный кинжал":
                        price = 15
                    elif item == "Мясо":
                        price = 25
                    else:
                        print(f"{редкий}Торговец{текст}: Меня это не интересует!")
                        sleep(1)
                        continue
                    
                    player['монет'] += price
                    inventory.pop(choice_num-1)
                    print(f"Ты продал {item} за {price} монет!")
                else:
                    print("Неверный выбор!")
            except ValueError:
                print("Пожалуйста, введите число!")
                
        elif act == "3":
            print(f"{редкий}Торговец{текст}: До новых встреч!")
            return "live"
        elif act == "4":
            print(f"{обычный}Ты{текст} бьёшь {редкий}Торговца{текст}!")
            sleep(1)
            print(f"{редкий}Торговец{текст}: А вот это ты зря сделал!")
            sleep(0.5)
            return battle(player, {'имя': f"{редкий}Торговец", 'урон': 6, 'хп': 35, 'шанс попадания по нему': 60, 'тип': "редкий"}, "атака")
        else:
            print("Пожалуйста, выберите действие 1-4!")

def battle(player, enemy, status):
    if status == "призыв":
        print(f"{обычный}Ты{текст} призвал {enemy['имя']}{текст}!")
    print(f"{обычный}Тебя{текст} атакует {enemy['имя']}{текст}!")
    sleep(0.5)
    if status == "засада":
        damage = randint(enemy['урон'] - 2, enemy['урон'] + 2)
        print(f"{enemy['имя']}{текст} нанёс {damage} урона тебе!")
        player['хп'] -= damage
        sleep(0.5)
    
    while enemy['хп'] > 0 and player['хп'] > 0:
        print(f"\n{обычный}Ты: {player['хп']}/{player['макс_хп']} хп{текст} vs {enemy['имя']}: {enemy['хп']} хп{текст}")
        print("Введите:")
        print("1. Атака (разброс ± 2 урона, 20% шанс дать критический урон (×2))")
        print("2. Лечить себя (+2-5 хп)")
        if status != "призыв" and status != "атака":
            print("3. Сбежать (шанс 50%)")
        print("4. Использовать предмет")
        print("5. Посмотреть статы")
        
        act = input(">>> ").strip()
        sleep(0.5)
        
        if act == "1":
            if random() < enemy['шанс попадания по нему'] / 100:
                damage = player['урон']
                if random() < 0.2 and enemy['хп'] > damage * 2:
                    print(f"{обычный}Ты{текст} нанёс {damage*2} критического урона противнику!")
                    enemy['хп'] -= atack(damage * 2)
                elif enemy['хп'] > damage:
                    print(f"{обычный}Ты{текст} нанёс {damage} урона противнику!")
                    enemy['хп'] -= atack(damage)
                else:
                    print(f"{обычный}Ты{текст} добил противника!")
                    enemy['хп'] = 0
            else:
                print(f"{обычный}Ты{текст} промахнулся!")
        elif act == "2":
            if player['хп'] == player['макс_хп']:
                print(f"{обычный}Ты{текст} полностью здоров!")
                continue
            hp = randint(2, 5)
            print(f"{обычный}Ты{текст} лечишь {hp} хп!")
            player['хп'] += hp
            if player['хп'] > player['макс_хп']:
                player['хп'] = player['макс_хп']
        elif act == "3" and status != "призыв" and status != "атака":
            if random() < 0.5:
                print(f"У {обычный}тебя{текст} получилось сбежать!")
                return "live"
            else:
                print(f"У {обычный}тебя{текст} не получилось сбежать!")
        elif act == "4":
            if len(inventory) == 0:
                print("Твой инвентарь пуст!")
                continue
            else:
                sleep(1)
                print("Введите:")
                for i, item in enumerate(inventory):
                    sleep(0.5)
                    print(f"{i+1}. {item}")
                
                try:
                    num = int(input("Номер предмета: ")) - 1
                    sleep(0.5)
                    if num < 0 or num >= len(inventory):
                        print("Неверный номер предмета!")
                        continue
                except ValueError:
                    print("Пожалуйста, введите число!")
                    continue
                
                sleep(0.5)
                if inventory[num] == "Малое зелье исцеления":
                    inventory.pop(num)
                    player['хп'] += 4
                    print("Ты использовал Малое зелье исцеления!")
                    if player['хп'] > player['макс_хп']:
                        player['хп'] = player['макс_хп']
                    sleep(0.5)
                    continue
                elif inventory[num] == "Мясо":
                    inventory.pop(num)
                    player['хп'] += 2
                    print("Ты съел мясо!")
                    if player['хп'] > player['макс_хп']:
                        player['хп'] = player['макс_хп']
                    sleep(0.5)
                    continue
                elif inventory[num] == "Точный сломаный кинжал":
                    inventory.pop(num)
                    damage = atack(randint(6, 8))
                    print(f"{обычный}Ты{текст} нанёс {damage} урона противнику при помощи Точный сломаный кинжал!")
                    enemy['хп'] -= damage
                    sleep(0.5)
                elif inventory[num] == "Острый кинжал":
                    if random() < enemy['шанс попадания по нему'] / 100:
                        damage = atack(randint(7, 9))
                        print(f"{обычный}Ты{текст} нанёс {damage} урона противнику при помощи Острый кинжал!")
                        enemy['хп'] -= damage
                    else:
                        print(f"{обычный}Ты{текст} промахнулся!")
                    sleep(0.5)
                elif inventory[num] == "Большое зелье исцеления":
                    inventory.pop(num)
                    player['хп'] += 10
                    print("Ты использовал Большое зелье исцеления!")
                    if player['хп'] > player['макс_хп']:
                        player['хп'] = player['макс_хп']
                    sleep(0.5)
                    continue
                elif inventory[num] == "Меч":
                    if random() < enemy['шанс попадания по нему'] / 100:
                        damage = randint(10, 12)
                        print(f"{обычный}Ты{текст} нанёс {damage} урона противнику при помощи Меч!")
                        enemy['хп'] -= damage
                    else:
                        print(f"{обычный}Ты{текст} промахнулся!")
                    sleep(0.5)
                elif inventory[num] == "Зелье живучести":
                    inventory.pop(num)
                    player['макс_хп'] += 5
                    print(f"{обычный}Ты{текст} использовал Зелье живучести!")
                    sleep(0.5)
                    continue
                else:
                    print("Неизвестный предмет!")
                    continue
        elif act == "5":
            print("Твои статы:\n", player)
            sleep(2)
            print("Твой инвентарь:\n", inventory)
            sleep(2)
            print("Статы противника:\n", enemy)
            sleep(2)
            continue
        else:
            print("Пожалуйста, введите цифру действия от 1 до 5!")
            continue
        
        sleep(0.5)
        if enemy['хп'] <= 0:
            break
        
        if enemy['хп'] < 6 and random() < 0.5 and enemy['тип'] == "обычный":
            print(f"{enemy['имя']}{текст} убежал с {enemy['хп']} хп!")
            print("Ты получил 5 монет!")
            player["монет"] += 5
            return "live"
        
        damage = max(1, randint(enemy['урон'] - 2, enemy['урон'] + 2))
        rand = random()
        if rand > 0.2 and rand < 0.8 and player['хп'] > damage:
            print(f"{enemy['имя']}{текст} нанёс {damage} урона тебе!")
            player['хп'] -= damage
        elif rand < 0.8 and player['хп'] > damage * 2:
            print(f"{enemy['имя']}{текст} нанёс {damage*2} критического урона тебе!")
            player['хп'] -= damage * 2
        elif player['хп'] <= damage or player['хп'] <= damage * 2:
            print(f"{enemy['имя']}{текст} добил тебя!")
            player['хп'] = 0
        else:
            print(f"{enemy['имя']}{текст} промахнулся!")
        
        sleep(1)
    
    if player['хп'] <= 0:
        print(f"{обычный}Ты{опасно} проиграл!")
        return "no live"
    else:
        print(f"{enemy['имя']}{текст} повержен!")
        rand = random()
        item = None
        if enemy['имя'] == f"{редкий}Торговец" and rand < 0.75:
            item = choice(["Острый кинжал", "Большое зелье исцеления"])
        elif enemy['имя'] in [f"{обычный}Волк", f"{обычный}Лиса"] and rand < 0.5:
            item = choice(["Малое зелье исцеления", "Мясо"])
        elif enemy['имя'] in [f"{редкий}Разбойник", f"{обычный}Гоблин"] and rand < 0.5:
            item = choice(["Точный сломаный кинжал", "Малое зелье исцеления"])
        elif rand < 0.5:
            item = "Малое зелье исцеления"
        
        if item is not None:
            print(f"{обычный}Ты{текст} получил 1 {item}!")
            inventory.append(item)
        coins = randint(10, 20)
        print(f"{обычный}Ты{текст} получил {coins} монет!")
        player['монет'] += coins
        print(f"{обычный}Ты{текст} выиграл!")
        sleep(1)
        print("Твои статы:\n", player)
        sleep(0.5)
        print("Твой инвентарь:\n", inventory)
        return "live"

game_status = "live"
while game_status == "live":
    sleep(1)
    print("\nЧто хочешь сделать?")
    print("1. Искать приключения")
    print("2. Разбить временный лагерь (20% шанс на нападение)")
    print("3. Посмотреть статы")
    print("4. Использовать предмет")
    print("5. Покинуть игру")
    
    act = input(">>> ").strip()
    sleep(0.5)
    
    if act == "1":
        while True:
            print(f"{обычный}Ты{текст} искаешь приключения...")
            sleep(2)
            rand = random()
            if rand < 0.3:
                enemy = choice(enemies).copy()
                if player['хп'] >= 30 and "Меч" in inventory:
                    enemy = choice(enemies_hard).copy()
                print(f"{обычный}Ты{текст} встретил {enemy['имя']}{текст}!")
                sleep(0.5)
                game_status = battle(player, enemy, "поиск")
                break
            elif rand < 0.5:
                print(f"{обычный}Ты{текст} встретил {редкий}Торговца{текст}!")
                sleep(0.5)
                game_status = shop()
                break
            else:
                print(f"{обычный}Ты{текст} никого не нашёл!")
                print("Идём дальше?")
                sleep(1)
                dn = input("(да/нет) ").strip().lower()
                sleep(0.5)
                if dn in ["д", "да"]:
                    continue
                elif dn in ["н", "нет"]:
                    break
                else:
                    print("Пожалуйста, введите д - да или н - нет.")
                    break
    elif act == "2":
        print(f"{обычный}Ты{текст} разбил временный лагерь!")
        sleep(1)
        print(f"{обычный}Ты{текст} засыпаешь...")
        sleep(3)
        if random() < 0.2:
            player['хп'] += player['макс_хп'] // 2
            if player['хп'] > player['макс_хп']:
                player['хп'] = player['макс_хп']
            print("На твой временный лагерь напали!\n")
            enemy = choice(enemies).copy()
            game_status = battle(player, enemy, "засада")
        else:
            player['хп'] = player['макс_хп']
            print(f"{обычный}Ты{текст} хорошо отдохнул!")
    elif act == "3":
        print("Твои статы:\n", player)
        sleep(2)
        print("Твой инвентарь:\n", inventory)
        sleep(2)
    elif act == "4":
        if len(inventory) == 0:
            print("Твой инвентарь пуст!")
        else:
            sleep(1)
            print("Введите:")
            for i, item in enumerate(inventory):
                sleep(0.5)
                print(f"{i+1}. {item}")
            try:
                num = int(input("Номер предмета: ")) - 1
                sleep(0.5)
                if num < 0 or num >= len(inventory):
                    print("Неверный номер предмета!")
                    continue
            except ValueError:
                print("Пожалуйста, введите число!")
            
            if inventory[num] == "Малое зелье исцеления":
                inventory.pop(num)
                player['хп'] += 4
                print(f"{обычный}Ты{текст} использовал Малое зелье исцеления!")
                if player['хп'] > player['макс_хп']:
                    player['хп'] = player['макс_хп']
            elif inventory[num] == "Мясо":
                inventory.pop(num)
                player['хп'] += 2
                print(f"{обычный}Ты{текст} съел мясо!")
                if player['хп'] > player['макс_хп']:
                    player['хп'] = player['макс_хп']
            elif inventory[num] == "Большое зелье исцеления":
                inventory.pop(num)
                player['хп'] += 10
                print(f"{обычный}Ты{текст} использовал Большое зелье исцеления!")
                if player['хп'] > player['макс_хп']:
                    player['хп'] = player['макс_хп']
            elif inventory[num] == "Зелье живучести":
                inventory.pop(num)
                player['макс_хп'] += 5
                print(f"{обычный}Ты{текст} использовал Зелье живучести!")
            else:
                print("Неизвестный предмет или его нельзя использовать вне боя!")
    elif act == "5":
        print("Игра завершена.")
        break
    elif act == "Hello, World!":
        print(f"{редкий}Ты активировал единственный чит-код в этой игре!{текст}\n")
        sleep(1)
        game_status = battle(player, {'имя': f"{легендарный}World", 'урон': 999999, 'хп': 999999, 'шанс попадания по нему': 100, 'тип': "легендарный"}, "призыв")
    else:
        print("Пожалуйста, введите цифру действия от 1 до 5!")