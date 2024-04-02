def welcome(name):
    print('Hello',name,'and welcome to the World of Games(WoG),\nHere you can find many cool games to play')

welcome(input('Please input your name'))



def load_game():
    if  n <=3 and n>=1:
      if n== 1:
        print(n,'.Memory game - a sequence of numbers will appear for 1 second and you have to guess it back')
      elif n == 2:
        print(n,'.Guess Game - guess a number and see if you choose like the computer')
      else:
        print (n,'Currency Roulette - try and guess the value of a random amount of USD in ILS')
    else:
        print('Please choose from one of these numbers 1,2 or 3')

    if level >=1 and level <= 5 :
       print(level)

    else:
        print('Please input a number from 1 to 5')
n=int(input('Choose the game to play'))
level = int(input('choose the level of difficulty'))

load_game()



