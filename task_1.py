with open("space.txt", encoding="utf8") as line, open("space_new.txt", "w", encoding="utf8") as lene:
    # парсим исходный файл
    arr = list(map(lambda p: p.strip().split("*"), line.readlines()))[1:]
    for i in arr:
        # Номер корабля
        ship_number = i[0].split("-")[1]

        # первая цифра
        n = int(ship_number[0])

        # вторая цифра
        m = int(ship_number[1])

        # кол-во букв в родной планете корабля
        t = len(i[1])

        # координаты корабля
        x, y = map(int, i[2].split(" "))

        # координаты направления
        x_d, y_d = map(int, i[3].split(" "))

        # меняем координаты в соответствии с таблицей (она в условии)
        if n > 5:
            x = n + x_d
        else:
            x = -(n + x_d) * 4 + t

        if m > 3:
            y = m + t + y_d
        else:
            y = -(n + y_d) * m

        lene.write(f"{i[0]}*{i[1]}*{x} {y}*{x_d} {y_d}" + "\n")

        if i[0].split("-")[0][-1] == "V":
            print(f"{i[0]} - ({x}, {y})")
