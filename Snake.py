from random import randint
import os
import time
import sys
from pynput import keyboard

keys = set()


def on_press(key):
    try:
        keys.add(key.char)
    except:
        pass


def on_release(key):
    try:
        keys.remove(key.char)
    except:
        pass


def clear():
    # to clear screen after every move
    os.system('cls' if os.name == 'nt' else 'clear')


class playArea:
    # head position
    # size list - all positions of body
    # 0=empty   1=snake     2=head  3=apple
    def __init__(self, high_score=0):
        self.board = []
        self.head_x = 0
        self.head_y = 0
        self.snake_position = [[0, 0]]
        self.length = 40  # board width
        self.height = 20  # board height
        self.dir = "d"  # initially move towards right
        self.apple = [1, 3]  # apple spawns firstly at position (1,3) always
        self.score = 0
        self.high_score = high_score

    def apple_spawn(self):
        while True:
            apple = [randint(0, self.length-1), randint(0, self.height-1)]

            if apple not in self.snake_position:
                self.apple = apple
                break

    def move(self):
        if "w" in keys and self.dir != "s":
            self.dir = "w"
        elif "a" in keys and self.dir != "d":
            self.dir = "a"
        elif "s" in keys and self.dir != "w":
            self.dir = "s"
        elif "d" in keys and self.dir != "a":
            self.dir = "d"

        match self.dir:
            case "w":
                self.head_y -= 1
                if self.game_over():
                    return 0  # game over
                self.snake_position.insert(0, [self.head_x, self.head_y])
                if self.snake_position[0] == self.apple:
                    self.apple_spawn()
                    self.score += 1
                else:
                    self.snake_position.pop()
                return 1
            case "a":
                self.head_x -= 1
                if self.game_over():
                    return 0  # game over
                self.snake_position.insert(0, [self.head_x, self.head_y])
                if self.snake_position[0] == self.apple:
                    self.apple_spawn()
                    self.score += 1
                else:
                    self.snake_position.pop()
                return 1
            case "s":
                self.head_y += 1
                if self.game_over():
                    return 0  # game over
                self.snake_position.insert(0, [self.head_x, self.head_y])
                if self.snake_position[0] == self.apple:
                    self.apple_spawn()
                    self.score += 1
                else:
                    self.snake_position.pop()
                return 1
            case "d":
                self.head_x += 1
                if self.game_over():
                    return 0  # game over
                self.snake_position.insert(0, [self.head_x, self.head_y])
                if self.snake_position[0] == self.apple:
                    self.apple_spawn()
                    self.score += 1
                else:
                    self.snake_position.pop()
                return 1

    def game_over(self):
        if (
            0 > self.head_x or self.head_x >= self.length or
            0 > self.head_y or self.head_y >= self.height or
            [self.head_x, self.head_y] in self.snake_position
        ):
            print("GAME OVER!")
            print(f"SCORE = {self.score}")
            self.update_high_score()
            input("\nPress Enter To Continue")
            return 1
        return 0

    def update_board(self):
        # initialize board by 0's
        self.board = [[0 for _ in range(self.length)]
                      for _ in range(self.height)]
        # snake body
        for x, y in self.snake_position:
            if 0 <= x < self.length and 0 <= y < self.height:
                self.board[y][x] = 1
        # snake head
        if 0 <= self.head_x < self.length and 0 <= self.head_y < self.height:
            self.board[self.head_y][self.head_x] = 2
        # apple
        ax, ay = self.apple
        if 0 <= ax < self.length and 0 <= ay < self.height:
            self.board[ay][ax] = 3

    def display_board(self):
        clear()
        print(f"Score= {self.score}")
        print(f"High Score= {self.high_score}")
        print("#"*(self.length+2))

        for i in range(0, self.height):
            print("#", end="")
            for j in range(0, self.length):
                if self.board[i][j] == 0:
                    print(" ", end="")
                elif self.board[i][j] == 1:
                    print("O", end="")
                elif self.board[i][j] == 2:
                    print("@", end="")
                elif self.board[i][j] == 3:
                    print("A", end="")
            print("#")

        print("#"*(self.length+2))

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as hs:
                hs.write(f"{self.high_score}")
            print("NEW HIGH SCORE!")


def main():
    while True:
        clear()
        print("1. Play")
        print("2. Instructions")
        print("3. Exit")
        try:
            choice = int(input("\nChoose Option ( 1-3 )"))

        except ValueError:
            print("Choose only from 1-3!")
            input("Press Enter To Go Back")
            continue

        match choice:
            case 1:

                with open("high_score.txt", "a+") as hs:
                    hs.seek(0)
                    high_score = hs.read().strip()
                    if high_score == "":
                        high_score = 0
                    else:
                        high_score = int(high_score)

                listener = keyboard.Listener(
                    on_press=on_press, on_release=on_release)
                listener.start()
                clear()
                game = playArea(high_score)
                while True:
                    if not game.move():
                        break
                    game.update_board()
                    game.display_board()
                    time.sleep(0.25)
                listener.stop()
                keys.clear()

            case 2:
                clear()
                print("HOLD THE KEYS (W, A, S, D) TO MOVE THE SNAKE\n")
                print("w = up")
                print("s = down")
                print("a = left")
                print("d = right")
                input("\nPress Enter To Go Back")
            case 3:
                sys.exit("GAME EXITED!")


if __name__ == "__main__":
    main()
