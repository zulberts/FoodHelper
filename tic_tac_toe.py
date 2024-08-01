from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.turn = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[QPushButton("") for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setFixedSize(100, 100)
                font = QFont()
                font.setPointSize(24)
                self.buttons[i][j].setFont(font)
                self.buttons[i][j].clicked.connect(
                    lambda _, x=i, y=j: self.make_move(x, y)
                )
                self.grid.addWidget(self.buttons[i][j], i, j)

        self.status_label = QLabel("Turn: X")
        self.grid.addWidget(self.status_label, 3, 0, 1, 3, Qt.AlignCenter)

    def make_move(self, x, y):
        if self.board[x][y] == "":
            self.board[x][y] = self.turn
            self.buttons[x][y].setText(self.turn)
            if self.check_win():
                self.status_label.setText(f"{self.turn} wins!")
                self.disable_buttons()
            elif self.check_draw():
                self.status_label.setText("It's a draw!")
            else:
                self.turn = "O" if self.turn == "X" else "X"
                self.status_label.setText(f"Turn: {self.turn}")

    def check_win(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)
