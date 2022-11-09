import random
from easygui import *

msgbox("WELKOME TO BLACK JACK GAME","==BLACK JACK==","Lets play BlackJack")

def game():
    cards = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
    random.shuffle(cards)
    count = 0
    count_bot = 0
    while True:
        chois = buttonbox("Please,take a card?",'==BLACK JACK==',['Yes','No'])
        if chois == 'Yes':
            current = cards.pop()  # pop видаляє карту
            current_bot = cards.pop()
            count += current  # додали значення
            count_bot += current_bot
            msgbox(f'You take:{current}\nBot take:{current_bot}\n***********\nPlayer score:{count}\nBot    score:{count_bot}','==Black Jack==')
            if count > 21:    # working
                if count_bot < 21:
                    msgbox(f"**Bot is win**\nPlayer:{count}\nBot:{count_bot}",'==Black Jack==')
                    break

            if count > 21:    # working
                if count_bot > 21:
                    msgbox(f"**Player and Bot are loose**\nPlauyer:{count}\nBot:{count_bot}",'==Black Jack==')
                    break

            if count == 21:   # working
                if count_bot > 21:
                    msgbox(f"**Player is win**\nPlayer:{count}\nBot:{count_bot}",'==Black Jack==')
                    break

            if count > 21: # working
                if count_bot == 21:
                    msgbox(f"**Bot is win**\nPlayer:{count}\nBot:{count_bot}",'==Black Jack==')
                    break

            if count < 21:            # working
                if count_bot > 21:
                    msgbox(f"**Player is win**\nPlayer:{count}\nBot:{count_bot}",'==Black Jack==')
                    break

            if count < 21:
                if count_bot == 21:
                    msgbox(f"**Bot is win**\nPlayer:{count}\nBot:{count_bot}",'==Black Jack==')
                    break

            if count == 21:           # working
                if count_bot < 21:
                    msgbox(f"**Player is win**\nPlayer:{count}\nBot:{count_bot}",'==Black Jack==')
                    break

            if count == 21:         # did not working
                if count_bot == 21:
                    msgbox(f"**DRAWW**\nPlauyer:{count}\nBot:{count_bot}",'==Black Jack==')
                    break

        if chois == 'No':
            if count > count_bot:
                msgbox(f'**Player is win**\nPlauyer:{count}\nBot:{count_bot}','==Black Jack==')
                break
            if count < count_bot:
                msgbox(f"**Bot is win**\nPlauyer:{count}\nBot:{count_bot}",'==Black Jack==')
                break
            if count == count_bot:
                msgbox(f'**DRAW**\nPlauyer:{count}\nBot:{count_bot}','==Black Jack==')
                break

if __name__ == '__main__':
    a = 1
    while a == 1:
        game()
        exit = buttonbox("Do you want to play again?","==Black Jack==", ['YES','NO'])
        if exit != "YES":
            a = 2
    else:
        msgbox(f'GOOD BUY','==Black Jack==')





