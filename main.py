import random

class pick():
    options = ["Rock","Paper","Scissors"] #Rock =1 Paper = 2 Scissors = 3
    def __init__(self):
        self.choicereturn()
    def choicereturn(self):
        self.choice = random.choice(self.options)
        return self.choice
    def win7(self, player1, player2):
        if player1 == player2:
            return "Tie!"
        elif player1 == "Rock":
            if player2 == "Scissors":
                return "Player1 win"
            else:
                return "Player2 win"
        elif player1 == "Scissors":
            if player2 == "Paper":
                return "Player1 win"
            else:
                return "Player2 win"
        elif player1 == "Paper":
            if player2 == "Rock":
                return "Player1 win"
            else:
                return "Player2 win"

def main():
    option = int(input("Enter 1 for computer vs computer, 2 for human vs computer: "))
    if option == 1:
        p1 = pick()
        p1pick = p1.choicereturn()
        p2 = pick()
        p2pick = p2.choicereturn()
        result = p1.win7(p1pick,p2pick)
        print(f"P1 picked: {p1pick}, P2 picked: {p2pick} so therefore {result}!")
    if option == 2:
        p1 = pick()
        p1pick = p1.choicereturn()
        hpick = input("Enter your choice, Abreviations are R for Rock, P for Paper, and S for scissors: ")
        hpick = hpick.lower()
        #print(hpick)
        if hpick == "r" or hpick == "rock":
            hpick = "Rock"
        if hpick == "s" or hpick == "scissors":
            hpick = "Scissors"
        if hpick == "p" or hpick == "paper":
            hpick = "Paper"
        result = p1.win7(p1pick,hpick)
        result = result.split(" ")
        for i in result:
            if i == "Player2":
                result[result.index(i)] = "You"
            elif i == "Player1":
                result[result.index(i)] = "Computer"
        print(f"the computer picked {p1pick}, and you picked {hpick} so therfore: {result[0]} {result[1]}")


if __name__ == "__main__":
    main()