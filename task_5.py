def print_ships(planet):
    print(f"{planet}: {d[planet]}")


with open("space.txt", encoding="utf8") as line:
    # парсим исходный файл
    arr = list(map(lambda p: p.strip().split("*"), line.readlines()))[1:]

    # cache
    d = {}

    for i in arr:
        if i[1] in d.keys():
            # если уже есть такая планета, добавляем туда код и номер корабля
            d[i[1]].append(i[0])
        else:
            # иначе создаем список и добавляем туда код и номер
            d[i[1]] = [i[0]]

    for i in arr[:11]:
        # выводим информацию о первых 10 кораблях
        print_ships(i[1])
