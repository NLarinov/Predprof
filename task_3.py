with open("space_new.txt", encoding="utf8") as line:
    # парсим исходный файл
    arr = list(map(lambda x: x.strip().split("*"), line.readlines()))
    # кешируем данные
    d = {}
    for i in arr:
        d[i[0]] = i

    while True:
        a = input()
        if a == "stop":
            break
        if a in d.keys():
            print(f"Корабль {a} был отправлен с планеты: {d[a][1]} и его направление движения было: {d[a][-1]}")
        else:
            print("error.. er.. ror..")
