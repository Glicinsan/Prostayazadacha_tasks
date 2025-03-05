from random import randint #С помощью этой функции будем ограничивать диапазон

def binar(n, mini, maxi):
    """
    :param:
        n (int): Число, по которому ограничивается диапазон возможных чисел
        mini (int): Минимальное число диапазона
        maxi (int): Максимальное число диапазона
    """
    try:
        n = randint(mini, maxi)
        a = input(f"is your num > {n}?")
        if a == 'да':
                mini = n + 1 #Ограничиваем диапазон возможных загаданных чисел
                if mini == maxi:
                    print(f"your number is {n}") #Ограничиваем диапазон возможных загаданных чисел
                else:
                    binar(randint(mini, maxi), mini, maxi)
        else:
            maxi = n
            if mini == maxi:
                print(f"your number is {n}")
            else:
                binar(randint(mini, maxi), mini, maxi)
    except:
        print("something is wrong")
        binar(randint(0, 1000), 0, 1000) #Возвращает игру к началу

binar(randint(0, 1000), 0, 1000)
