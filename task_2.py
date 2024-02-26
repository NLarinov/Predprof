with open("space_new.txt", encoding="utf8") as line:
    # парсим исходный файл
    arr = list(map(lambda x: x.strip().split("*"), line.readlines()))
    # сортируем
    sort = sorted(arr, key=lambda x: x[0].split("-")[1])
    # принтим
    [print(i[0]) for i in sort[:11]]
