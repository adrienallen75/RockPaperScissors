import random
import string

class RockPaperScissors:

    def game(self):
        user_choice = []
        game_choice = []

        game_list = ['Rock', 'Paper', 'Scissors']


        usr_count = 0
        robo_count = 0

        play = True
        while play:

            print('enter either rock, paper or scissors:')
            userinput = input()
            user_choice.append(userinput)

            robo = random.choice(game_list)
            print('robots choice:',robo)

            if userinput.lower() == 'rock' and robo == 'Rock' or userinput.lower() == 'paper' and robo == 'Paper' or userinput.lower() == 'scissors' and robo == 'Scissors':
                print('Draw!')
                print('Would you like to try again?:')
                answer = input()
                if answer.lower() == 'yes':
                    play = True
                if answer.lower() == 'no':
                    break

            elif userinput.lower() == 'rock' and robo == 'Scissors'or userinput.lower() == 'paper' and robo == 'Rock' or userinput.lower() == 'scissors' and robo == 'Paper':
                print('User Wins!')
                usr_count+=1
                print('User:',usr_count, ' ', 'Robot:', robo_count)
                print('Would you like to try again?:')
                answer = input()
                if answer.lower() == 'yes':
                    play = True
                if answer.lower() == 'no':
                    break

            elif userinput.lower() == 'rock' and robo == 'Paper'or userinput.lower() == 'paper' and robo == 'Scissors' or userinput.lower() == 'scissors' and robo == 'Rock':
                print('Robot Wins!')
                robo_count+=1
                print('User:',usr_count, ' ', 'Robot:', robo_count)
                print('Would you like to try again?:')
                answer = input()
                if answer.lower() == 'yes':
                    play = True
                if answer.lower() == 'no':
                    break

c = RockPaperScissors()

g = c.game()
        







                
