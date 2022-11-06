import random
import time

print("++++++++++++++++++++++++++++++++++++++")
print("==============BLACK JACK==============")
print("++++++++++++++++++++++++++++++++++++++\n")


def game():
    cards = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
    random.shuffle(cards)

    print("Lets play BlackJack\n")
    count = 0
    count_bot = 0

    while True:
        chois = input("Please,take a card? y/n\n")
        if chois == 'y':
            current = cards.pop()  # pop видаляє карту
            current_bot = cards.pop()
            count += current  # додали значення
            count_bot += current_bot
            print("You take: ", current)
            print("Bot take: ", current_bot, "\n")
            print("Player score: ", count)
            print("Bot score: ", count_bot, "\n")
            if count > 21:    # working
                if count_bot < 21:
                    print("Bot is win. Bot has:", count_bot, "\n","You are looser. You have", count,"\n")
                    break

            elif count > 21:
                if count_bot > 21:
                    print("Player is looser" "\n", "Plauyer:", count,"\n","Bot is looser\n", "BOT:", count_bot,"\n")
                    break

            elif count == 21:
                if count_bot > 21:
                    print("You are win. You have", count, "\n", "Bot is looser. He has", count_bot,"\n")
                    break

            elif count > 21:
                if count_bot == 21:
                    print("You are looser. You have", count, "\n", "Bot is win. He has", count_bot,"\n")
                    break

            elif count < 21:            # working
                if count_bot > 21:
                    print("You are win. You have", count, "\n", "Bot is looser. He has", count_bot,"\n")
                    break

            elif count == 21:
                if count_bot < 21:
                    print("You are win. You have", count, "\n", "Bot is looser. He has", count_bot,"\n")
                    break

            elif count == 21:         # did not working
                if count_bot == 21:
                    print("DRAWW\n", "BOT:", count_bot, "\n", "Plauyer:", count,"\n")
                    break



        elif chois == 'n':
            print ("Plauer score: ", count,"\n", "Bot score: ", count_bot,"\n")
            break

if __name__ == '__main__':
    a = 1
    while a == 1:
        game()
        exit = input("Do you want to play again? [YES] [NO]: ")
        if exit != "YES":
            a = 2
    else:
        print('GOOD BUY')
        time.sleep(5)





