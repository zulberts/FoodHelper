import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 800)

        label_text = (
            "Hello there, you can choose whether you can cook "
            "random meal or play tictactoe"
        )
        label = QLabel(label_text, self)

        button1 = QPushButton("Another random meal", self)
        button2 = QPushButton("Play Tic-Tac-Toe", self)

        h_layout = QHBoxLayout()
        h_layout.addWidget(button1)
        h_layout.addWidget(button2)

        v_layout = QVBoxLayout()
        v_layout.addWidget(label)
        v_layout.addLayout(h_layout)
        v_layout.addStretch(1)  # Add stretch to push buttons to the top

        self.setLayout(v_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
