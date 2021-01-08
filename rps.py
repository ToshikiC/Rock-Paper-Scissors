import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        while True:
            human_move = input("rock, paper, scissors?")
            if human_move in moves:
                return human_move
                break
            else:
                print("invalid move, try again")


class ReflectPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.my_move = None

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            index = moves.index(self.my_move) + 1
            if index == len(moves):
                index = 0
        return moves[index]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print("Player 1 Wins!")
            self.score_p1 += 1
        elif move1 == move2:
            print("Tie!")
        else:
            print("Player 2 Wins!")
            self.score_p2 += 1
        print(self.score_p1)
        print(self.score_p2)

    def play_game(self):
        print("Game start!")
        while True:
            try:
                rounds = int(input("How many rounds?"))
                for round in range(rounds):
                    print(f"Round {round+1}:")
                    self.play_round()
                if self.score_p1 > self.score_p2:
                    print("Player 1 Wins!")
                    print("Game over!")
                    break
                elif self.score_p2 > self.score_p1:
                    print("Player 2 Wins!")
                    print("Game over!")
                    break
                else:
                    print("Its a tie!")
                    print("Game over!")
                    break
            except ValueError:
                print("invalid number, try again")


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
        [CyclePlayer(), ReflectPlayer(), RandomPlayer(), Player()]))
    game.play_game()
