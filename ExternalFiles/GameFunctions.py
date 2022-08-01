# Functions for game
from random import randint


def rockPaperScissors(player, bot):
    player.score = 0
    bot.score = 0
    rpsDictionary = {1: "Rock", 2: "Paper", 3: "Scissors"}
    # Game is over when either player gets 3 wins.
    while player.score != 3 and bot.score != 3:
        bot.hand = rpsDictionary[randint(1, 3)]
        player.hand = int(input("Choose: 1 - Rock, 2 - Paper, 3 - Scissors: "))
        if player.hand < 1 or player.hand > 3:
            print("Please choose valid input")
            continue
        # elif player.hand != 1 and player.hand != 2 and player.hand != 3:
            # print("Please choose valid input")
            continue
        else:
            player.hand = rpsDictionary[player.hand]
        # Conditions for different results
        if player.hand == "Scissors" and bot.hand == "Paper":
            player.score += 1
            print(player.hand + " VS " + bot.hand)
            print("You win.")
            print("Score: "+str(player.score) + ":" + str(bot.score))
        elif player.hand == "Scissors" and bot.hand == "Rock":
            bot.score += 1
            print(player.hand + " VS " + bot.hand)
            print("You lose.")
            print("Score: "+str(player.score) + ":" + str(bot.score))
        elif player.hand == "Rock" and bot.hand == "Paper":
            bot.score += 1
            print(player.hand + " VS " + bot.hand)
            print("You lose.")
            print("Score: "+str(player.score) + ":" + str(bot.score))
        elif player.hand == "Rock" and bot.hand == "Scissors":
            player.score += 1
            print(player.hand + " VS " + bot.hand)
            print("You win.")
            print("Score: " + str(player.score) + ":" + str(bot.score))
        elif player.hand == "Paper" and bot.hand == "Rock":
            player.score += 1
            print(player.hand + " VS " + bot.hand)
            print("You win.")
            print("Score: " + str(player.score) + ":" + str(bot.score))
        elif player.hand == "Paper" and bot.hand == "Scissors":
            bot.score += 1
            print(player.hand + " VS " + bot.hand)
            print("You lose.")
            print("Score: " + str(player.score) + ":" + str(bot.score))
        elif player.hand == bot.hand:
            print(player.hand + " VS " + bot.hand)
            print("Draw!")
            print("Score: " + str(player.score) + ":" + str(bot.score))
    # Prompts user to play again
    while True:
        playAgain = str(input("Want to play again? Y or N: "))
        if playAgain.upper() == "Y":
            rockPaperScissors(player, bot)
            break
        elif playAgain.upper() == "N":
            break
        else:
            print("Please enter valid input")
