import csv


# функция создания пароля
def password(element):
    # три последние буквы планеты
    a = element[1][-3:]

    # две центральные буквы слова кода корабля (т.к. все названия длиной 4), в обратном порядке
    b = element[0][1:3][::-1]

    # первые три буквы названия планеты в обратном порядке
    c = element[1][:3][::-1]

    return (a + b + c).upper()


with open("space.txt", encoding="utf8") as line, open("space_uniq_password.csv", "w", encoding="utf8") as lene:
    # парсим исходный файл
    arr = list(map(lambda x: x.strip().split("*"), line.readlines()))[1:]

    # список
    data = []

    # csv
    writer = csv.writer(lene, delimiter=";")

    # header
    writer.writerow(["ShipName", "planet", "coord_place", "direction", "password"])

    for i in arr:
        # создаем пароль
        pssw = password(i)
        # записываем в список
        i.append(pssw)
        data.append(i)

    writer.writerows(data)