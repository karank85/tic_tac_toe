import tkinter as tk
from tkinter.font import Font

root = tk.Tk()

canvas = root.geometry("320x480")


class Game:
    def __init__(self):
        self.player_turn = 0
        # 1 will represent X
        # 0 will represent O
        self.data_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        bigFont = Font(
            family="Arial",
            size=16,
            weight="bold",
        )
        mediumFont = Font(
            family="Arial",
            size=16,
            weight="bold",


        )
        self.button1 = tk.Button(root, text=" ", command=self.position1, width=10, height=10)
        self.button1.grid(row=0, column=0)
        self.button2 = tk.Button(root, text=" ", command=self.position2, width=10, height=10)
        self.button2.grid(row=0, column=1)
        self.button3 = tk.Button(root, text=" ", command=self.position3, width=10, height=10)
        self.button3.grid(row=0, column=2)
        self.button4 = tk.Button(root, text=" ", command=self.position4, width=10, height=10)
        self.button4.grid(row=1, column=0)
        self.button5 = tk.Button(root, text=" ", command=self.position5, width=10, height=10)
        self.button5.grid(row=1, column=1)
        self.button6 = tk.Button(root, text=" ", command=self.position6, width=10, height=10)
        self.button6.grid(row=1, column=2)
        self.button7 = tk.Button(root, text=" ", command=self.position7, width=10, height=10)
        self.button7.grid(row=2, column=0)
        self.button8 = tk.Button(root, text=" ", command=self.position8, width=10, height=10)
        self.button8.grid(row=2, column=1)
        self.button9 = tk.Button(root, text=" ", command=self.position9, width=10, height=10)
        self.button9.grid(row=2, column=2)
        self.button10 = tk.Button(root, text="Restart", command=self.restart, width=10, height=10)
        self.button10.grid(row=0,column=3)
        self.status = tk.Label(root, text="O", font=mediumFont, fg="#4245f5")
        self.status.grid(row=1, column=3)
        self.credit = tk.Label(root, text="Tic\nTac\nToe", font=bigFont)
        self.credit.grid(row=2,column=3)

    def position1(self):
        x = 0
        y = 0
        if not self.checkPlayed(x, y):
            if self.player_turn == 0:
                self.button1['text'] = "O"
                self.data_array[y][x] = "0"
                self.player_turn = 1
                self.status['text'] = "X"
            else:
                self.button1['text'] = "X"
                self.data_array[y][x] = "1"
                self.player_turn = 0
                self.status['text'] = "O"
        self.isGameOver()

    def position2(self):
        x = 1
        y = 0
        if not self.checkPlayed(x, y):
            if self.player_turn == 0:
                self.button2['text'] = "O"
                self.data_array[y][x] = "0"
                self.player_turn = 1
                self.status['text'] = "X"
            else:
                self.button2['text'] = "X"
                self.data_array[y][x] = "1"
                self.player_turn = 0
                self.status['text'] = "O"
        self.isGameOver()

    def position3(self):
        x = 2
        y = 0
        if not self.checkPlayed(x, y):
            if self.player_turn == 0:
                self.button3['text'] = "O"
                self.data_array[y][x] = "0"
                self.player_turn = 1
                self.status['text'] = "X"
            else:
                self.button3['text'] = "X"
                self.data_array[y][x] = "1"
                self.player_turn = 0
                self.status['text'] = "O"
        self.isGameOver()

    def position4(self):
        x = 0
        y = 1
        if not self.checkPlayed(x, y):
            if self.player_turn == 0:
                self.button4['text'] = "O"
                self.data_array[y][x] = "0"
                self.player_turn = 1
                self.status['text'] = "X"
            else:
                self.button4['text'] = "X"
                self.data_array[y][x] = "1"
                self.player_turn = 0
                self.status['text'] = "O"
        self.isGameOver()

    def position5(self):
        x = 1
        y = 1
        if not self.checkPlayed(x, y):
            if self.player_turn == 0:
                self.button5['text'] = "O"
                self.data_array[y][x] = "0"
                self.player_turn = 1
                self.status['text'] = "X"
            else:
                self.button5['text'] = "X"
                self.data_array[y][x] = "1"
                self.player_turn = 0
                self.status['text'] = "O"
        self.isGameOver()

    def position6(self):
        x = 2
        y = 1
        if not self.checkPlayed(x, y):
            if self.player_turn == 0:
                self.button6['text'] = "O"
                self.data_array[y][x] = "0"
                self.player_turn = 1
                self.status['text'] = "X"
            else:
                self.button6['text'] = "X"
                self.data_array[y][x] = "1"
                self.player_turn = 0
                self.status['text'] = "O"
        self.isGameOver()

    def position7(self):
        x = 0
        y = 2
        if not self.checkPlayed(x, y):
            if self.player_turn == 0:
                self.button7['text'] = "O"
                self.data_array[y][x] = "0"
                self.player_turn = 1
                self.status['text'] = "X"
            else:
                self.button7['text'] = "X"
                self.data_array[y][x] = "1"
                self.player_turn = 0
                self.status['text'] = "O"
        self.isGameOver()

    def position8(self):
        x = 1
        y = 2
        if not self.checkPlayed(x, y):
            if self.player_turn == 0:
                self.button8['text'] = "O"
                self.data_array[y][x] = "0"
                self.player_turn = 1
                self.status['text'] = "X"
            else:
                self.button8['text'] = "X"
                self.data_array[y][x] = "1"
                self.player_turn = 0
                self.status['text'] = "O"
        self.isGameOver()

    def position9(self):
        x = 2
        y = 2
        if not self.checkPlayed(x, y):
            if self.player_turn == 0:
                self.button9['text'] = "O"
                self.data_array[y][x] = "0"
                self.player_turn = 1
                self.status['text'] = "X"
            else:
                self.button9['text'] = "X"
                self.data_array[y][x] = "1"
                self.player_turn = 0
                self.status['text'] = "O"
        self.isGameOver()

    def checkPlayed(self, x, y):
        if self.data_array[y][x] == " ":
            return False
        else:
            return True

    def isGameOver(self):
        x_condition = "111"
        o_condition = "000"
        if x_condition in self.sumVertical() or x_condition in self.sumHorizontal() or x_condition in self.diagSum():
            self.declareWinner(1)
        elif o_condition in self.sumVertical() or o_condition in self.sumHorizontal() or o_condition in self.diagSum():
            self.declareWinner(0)
        elif self.isEmpty():
            self.declareWinner(-1)

    def isEmpty(self):
        for j in self.data_array:
            for i in j:
                if i == " ":
                    return False
        return True

    def sumVertical(self):
        sum_string = ""
        for i in range(3):
            for j in range(3):
                sum_string += self.data_array[j][i]
            sum_string += " "
        return sum_string

    def sumHorizontal(self):
        sum_string = ""
        for j in range(3):
            for i in range(3):
                sum_string += self.data_array[j][i]
            sum_string += " "
        return sum_string

    def diagSum(self):
        sum_string = ""
        for index in range(3):
            sum_string += self.data_array[index][index]
        sum_string += " "
        x = 2
        y = 0
        while x > -1 and y < 3:
            sum_string += self.data_array[y][x]
            x -= 1
            y += 1
        return sum_string

    def declareWinner(self, player):
        if player == 1:
            self.status['text'] = "Winner\n\nX"
        elif player == 0:
            self.status['text'] = "Winner\n\nO"
        else:
            self.status['text'] = "Tie"
        self.lockButton()

    def lockButton(self):
        self.button1['state'] = tk.DISABLED
        self.button2['state'] = tk.DISABLED
        self.button3['state'] = tk.DISABLED
        self.button4['state'] = tk.DISABLED
        self.button5['state'] = tk.DISABLED
        self.button6['state'] = tk.DISABLED
        self.button7['state'] = tk.DISABLED
        self.button8['state'] = tk.DISABLED
        self.button9['state'] = tk.DISABLED

    def restart(self):
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.button5.destroy()
        self.button6.destroy()
        self.button7.destroy()
        self.button8.destroy()
        self.button9.destroy()
        self.button10.destroy()
        self.status.destroy()
        Game()




Game()


root.mainloop()
