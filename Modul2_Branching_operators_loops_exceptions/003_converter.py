import time

def konv():

    b = input(" Введіть в яку одиницю виміру ви хочете перевести метри [милі] [дюйми] [ярди] ")
    n = input("Введіть метри: ")

    if (b=="милі"):
        mile = float(n) * 0.62137
        print(n, "метрів= ", mile, "милів")
    elif (b=="дюйми"):
        inch = float(n) * 39.3701
        print(n, "метрів= ", inch, "дюймів")
    elif (b=="ярди"):
        yard = float(n) * 1.0936
        print(n, "метрів= ", yard, "ярдів")

if __name__ == '__main__':
    konv()
    a = 1
    while a == 1:
        konv ()
        exit = input ("Чи бажаєте перевести метри в інші одиниці виміру так/ні\n")
        if exit != 'так':
            a = 2
    else:
        print("Гарного дня")
        time.sleep(5)