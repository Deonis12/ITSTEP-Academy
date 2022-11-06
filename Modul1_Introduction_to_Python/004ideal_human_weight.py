c=1
while c==1:

    a = (input("Введіть вашу стать (чоловік/жінка): "))

    if a == "чоловік":
        print('Ідеальна вага чоловіка')

        man_name = (input ("Ваше ім'я: "))
        man_height = int (input ("Ваш зріст: "))
        man_weight = float(man_height - (100 + (man_height - 100) / 20))
        print(man_name, ":""Ваша ідеальна вага: ", man_weight)  #Навчитись виділяти жирним
        print("Якщо ви хочите вийти,натисніть CTR+C")

    elif a == "жінка":
        print('Ідеальна вага жінки')

        woman_name = (input ("Ваше ім'я: "))
        woman_height = int(input ("Ваш зріст: "))
        woman_weight = float(woman_height - ( 100 + (woman_height - 100) / 10))
        print(woman_name,":""Ваша ідеальна вага: ",woman_weight)  #Навчитись виділяти жирним
        print("Якщо ви хочите вийти,натисніть CTR+C")