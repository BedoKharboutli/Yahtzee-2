from die import Die


class YahtzeeMainClass:
    def __init__(self):
        self.dice = []  # fix name of variable

        for i in range(5):  # loop to create five dices
            self.dice.append(Die())

        self.keepItGoing = True

        while self.keepItGoing == True:
            turn = 0

            print("Welcome to Yahtzee!")

            while turn < 3:
                print(f"Starting turn: {turn+1} of 3, rolling dice")
                rollDice(self.dice)
                isYahtzee = checkIfYahtzee(self.dice)

                if isYahtzee == True:
                    print(f"You got YAHTZEE! in {self.dice[0].value}'s")
                    return
                else:
                    # Here we check if there is no Yahtzee: then we check what turn we are on and ask the player if we want to continue or not
                    if turn != 2:
                        if (
                            input(
                                "Want to throw again? (y for yes, anything else for no) "
                            )
                            == "y"
                        ):
                            turn += 1
                        else:
                            self.keepItGoing = False
                            break
                    else:
                        if input("Game over! Want to play again? ") == "y":
                            turn = 0
                        else:
                            self.keepItGoing = False
                            break


def rollDice(dice):
    for i, die in enumerate(dice):
        die.Roll()
        print(f"{i}: {die}")


def checkIfYahtzee(dice):
    isYahtzee = True
    for j in range(1, 5):
        if dice[j].value != dice[j - 1].value:
            isYahtzee = False
    return isYahtzee


def main():
    YahtzeeMainClass()


if __name__ == "__main__":
    main()
