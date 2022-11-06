import random
import time

def game():
    print("Welcome to the GAME:\'Stone,paper,scissors'")
    print('The game will go against the computer')
    print('Use big letters to select:')
    print('[R]-rock')
    print('[S]-stone')
    print('[P]-paper')

    user_score = 0
    user_choice = 0
    bot_score = 0
    bot_choice = 0

    print('---GAME STARTING---')
    for i in range(3):
        print('\n---ROUND #', str(i + 1), '---')
        bot_choice = random.choice(['R', 'S', 'P'])
        user_choice = input('Your choice')
        print('You choice:', user_choice,"\n",'     &')
        print('Bot choice:', bot_choice,'\n------------')
        if user_choice == bot_choice:
            print('DRAW')
        elif user_choice =='R':
            if bot_choice =='S':
                user_score = user_score+1
                print('PLAYER IS WIN')
            else:
                bot_score = bot_score + 1
                print ('BOT WON ROUND')
        elif user_choice == 'S':
            if bot_choice == 'P':
                user_score = user_score + 1
                print('PLAUER WON ROUND')
            else:
                bot_score = bot_score + 1
                print('BOT WON ROUND')
        elif user_choice == 'P':
            if bot_choice == 'R':
                user_score = user_score + 1
                print('PLAUER WON ROUND')
            else:
                bot_score = bot_score + 1
                print('BOT WON ROUND')
        else:
            print('Error')
        continue

    if user_score > bot_score:
        print ('\nUser win: ', user_score,'\n','**********','\n','User score: ', user_score,'\n','Bot  score: ',bot_score)
    elif user_score < bot_score:
        print ('\nBot win: ', bot_score,'\n','**********','\n','User score: ', user_score,'\n','Bot  score: ',bot_score)
    elif user_score == bot_score:
        print('\nDraw','\n','**********','\n','User score: ',user_score,'\n','Bot  score: ',bot_score)

if __name__ == '__main__':
    a = 1
    while a == 1:
        game()
        exit = input("Do you want to play again? [YES] [NO]\n")
        if exit !='YES':
            a=2
    else:
        print('GOOD BUY')
        time.sleep(5)