import time
import datetime

k = [1,2,3,4,5,6,7,8,9,10]
passanger = []
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
k.reverse()
k.pop(1)
count = 10

while (count > 0):
    print('Кількість вільних камер схову: ',count)
    num = int(input('Введіть кількість пасажирів: '))
    count = count - num
    for i in range (1, num +1):
        if count > num:
            name = input('Введіть ім`я пасажира: ')
            time_entry = input('Введіть час бронювання шафи /hh:mm/:')
            hours, minutes = map(int, time_entry.split(':'))
            t = datetime.time(hours, minutes)
            t1 = datetime.time(hours + 2, minutes)

            passanger.append('Номер камери схову:')
            passanger.append(k.pop())
            passanger.append('Ім`я пасажира:')
            passanger.append(name)
            passanger.append('Час бронювання камери схову:')
            passanger.append(t)
            passanger.append('Час здачі камери схову:')
            passanger.append(t1)

            print('Кількість вільних камер схову: ',count,*passanger,sep='\n')
            continue
else:
    print('Вибачте,немає вільних камер схову.\nГАРНОГО ДНЯ')
    time.sleep(10)