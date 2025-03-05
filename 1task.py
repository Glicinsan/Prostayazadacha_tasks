def task1():
    a = []  # массив, в который будут добавляться простые числа
    try:
        begin = int(input("input begin number "))
        end = int(input("input end number "))
        for c in range(begin, end + 1):
                if all([c % b for b in range(2, c)]) != 0: #проверка числа на отсутствие делителей
                    a.append(c)
    except:
        print("invalid data")
        task1() #Возвращает программу в начало
    print(a)

task1()