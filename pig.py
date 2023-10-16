import random

class Player:
    player_score = 0
    turn_total = 0
    def __init__(self, pos, turn):
        self.pos = pos
        self.turn = turn
    def get_score(self):
        return player_score
    def switch_turn(self):
        if self.turn is True:
            self.turn = False
        else:
            self.turn = True
    def get_turn(self):
        return self.turn

def die_roll():
    random.seed(0)
    die = random.randrange(1, 7)
    return die

def new_game():
    pig_run = 0
    while pig_run == 0:
        new_game = input("Would you like to play again (Y/N)? ")
        if new_game == 'Y' or new_game.upper() == 'Y':
            pig_game()
        elif new_game == 'N' or new_game.upper() == 'N':
            pig_run = 1
        else:
            print("\nINVALID INPUT\n")

def pig_game():
    new_line = '\n'
    roll = 0
    p1 = Player(1, False)
    p2 = Player(2, False)
    print('\nWelcome to The Game of Pig.')
    first_turn = random.randrange(1, 11)
    if first_turn > 6:
        print("Player 1 goes first.")
        p1.switch_turn()
    else:
        print("Player 2 goes first.")
        p2.switch_turn()
    while p1.player_score < 100 and p2.player_score < 100:
        while p1.get_turn() is True:
            print("\nPlayer 1's turn")
            print(f"Score: {p1.player_score}{new_line}Turn Total: {p1.turn_total}")
            choice = input("Enter 'r' to roll or 'h' to hold: ")
            if choice == 'r' or choice.lower() == 'r':
                roll = die_roll()
                print(f"You rolled: {roll}")
                if roll == 1:
                    p1.turn_total = 0
                    p2.switch_turn()
                    p1.switch_turn()
                else:
                    p1.turn_total += roll
                if p1.turn_total + p1.player_score >= 100:
                    p1.player_score += p1.turn_total
                    break
            elif choice == 'h' or choice.lower() == 'h':
                p1.player_score += p1.turn_total
                p1.turn_total = 0
                p2.switch_turn()
                p1.switch_turn()
            else:
                print("\n---INVALID INPUT---")
        if p1.player_score >= 100:
            break
        while p2.get_turn() is True:
            print("\nPlayer 2's turn")
            print(f"Score: {p2.player_score}{new_line}Turn Total: {p2.turn_total}")
            choice = input("Enter 'r' to roll or 'h' to hold: ")
            if choice == 'r' or choice.lower() == 'r':
                roll = die_roll()
                print(f"You rolled: {roll}")
                if roll == 1:
                    p2.turn_total = 0
                    p1.switch_turn()
                    p2.switch_turn()
                else:
                    p2.turn_total += roll
                if p2.turn_total + p2.player_score >= 100:
                    p2.player_score += p2.turn_total
                    break
            elif choice == 'h' or choice.lower() == 'h':
                p2.player_score += p2.turn_total
                p2.turn_total = 0
                p1.switch_turn()
                p2.switch_turn()
            else:
                print("\nINVALID INPUT\n")
    p1.turn_total = 0
    p2.turn_total = 0
    if p1.player_score > p2.player_score:
        print("\nPlayer 1 Wins!")
        print(f"P1: {p1.player_score}{new_line}P2: {p2.player_score}")
    else:
        print("\nPlayer 2 Wins!")
        print(f"P2: {p2.player_score}{new_line}P1: {p1.player_score}")

        p1.player_score = 0
        p2.player_score = 0


if __name__ == "__main__":
   pig_game()
   new_game()