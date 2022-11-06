health_pers = 20
armor_pers = 50
health_spider = 5
put = input ("[left] [up] [down] [right]")

if (put=="right"):
    print("Ви знайшли броню")
    print("Здоров'є 20; Броня 50")
    put = input ("[left] [up] [down] [right]")
elif (put=="left"):
    print("Ви знайшли меч")
    print("Сила удару +60")
    put = input ("[left] [up] [down] [right]")
elif (put == "up"):
    print("Ви зайшли в пусту кімнату")
    put = input("[left] [up] [down] [right]")
elif (put == "down"):
    print("Ви знайшли мішечок з золотом")
    print("У вас +100 золота")
    put = input("[left] [up] [down] [right]")

if (put=="up"):
    print("Ви зустріли павука")
    def my_funktion(x):
        return 5 * x
    print("Урон",my_funktion(0),"Ви промахнулись")
    print("Ви отримали урон", "-", my_funktion(2),"%")
    print("Паук отримав урон","-",my_funktion(3))
    print("Паук отримав урон","-",my_funktion(6))
    print("Паук отримав урон","-",my_funktion(4))
    print("Ви знищили павука")
    put = input("[left] [up] [down] [right]")
elif (put=="left"):
    print("В розломі стіни ви знайшли еліксір")
    print("Ваше здоров'є підвищилось на 50%")
    put = input("[left] [up] [down] [right]")
elif (put=="right"):
    print("Кімната пуста")
    put = input("[left] [up] [down] [right]")
elif (put=="down"):
    print("Кімната пуста")
    put = input("[left] [up] [down] [right]")

if (put=="down"):
    print("Ви потрапили в пастку")
    def my_funktion(x):
        return 5 * x
    print("Урон","-",my_funktion(3),"%")
    print("Урон","-",my_funktion(3),"%")
    print("Урон","-",my_funktion(3),"%")
    print("Ви втратили 45% здоров'я","Ви померли")
elif (put=="right"):
    print("Ви знайшли вихід")
elif (put=="up"):
    print("Ви знайшли вихід")
elif (put=="left"):
    print("Ви знайшли вихід")
import time
time.sleep(100)