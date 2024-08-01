import sys
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QScrollArea,
    QStackedWidget,
)
from PyQt5.QtGui import QPixmap
from io import BytesIO
from meal import Meal, get_random_meal
from tic_tac_toe import TicTacToe


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
        self.label = QLabel(label_text, self)

        self.button1 = QPushButton("Another random meal", self)
        self.button2 = QPushButton("Play Tic-Tac-Toe", self)

        self.button1.clicked.connect(self.show_random_meal)
        self.button2.clicked.connect(self.show_tic_tac_toe)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button1)
        h_layout.addWidget(self.button2)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(h_layout)

        self.stack = QStackedWidget(self)

        self.meal_area = QScrollArea(self)
        self.meal_content = QWidget()
        self.meal_layout = QVBoxLayout(self.meal_content)
        self.meal_area.setWidget(self.meal_content)
        self.meal_area.setWidgetResizable(True)
        self.stack.addWidget(self.meal_area)

        self.tic_tac_toe = TicTacToe()
        self.stack.addWidget(self.tic_tac_toe)

        self.v_layout.addWidget(self.stack)

        self.setLayout(self.v_layout)

    def show_random_meal(self):
        meal = get_random_meal()
        if meal:
            self.update_meal_display(meal)
            self.stack.setCurrentWidget(self.meal_area)

    def show_tic_tac_toe(self):
        self.stack.setCurrentWidget(self.tic_tac_toe)

    def update_meal_display(self, meal: Meal):
        for i in reversed(range(self.meal_layout.count())):
            widget = self.meal_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        response = requests.get(meal.strMealThumb)
        img_data = response.content
        img = QPixmap()
        img.loadFromData(BytesIO(img_data).read())
        img_label = QLabel(self)
        img_label.setPixmap(img.scaled(250, 250))

        name_label = QLabel(f"Name: {meal.strMeal}", self)
        name_label.setStyleSheet("font-size: 16px; font-weight: bold;")

        category_label = QLabel(f"Category: {meal.strCategory}", self)
        area_label = QLabel(f"Area: {meal.strArea}", self)

        instructions_label = QLabel("Instructions:", self)
        instructions_text = QTextEdit(self)
        instructions_text.setReadOnly(True)
        instructions_text.setText(meal.strInstructions)

        ingredients_label = QLabel("Ingredients:", self)
        ingredients_text = QTextEdit(self)
        ingredients_text.setReadOnly(True)
        ingredients_text.setText(
            "\n".join(
                [
                    f"{ingredient}: {measure}"
                    for ingredient, measure in zip(meal.ingredients, meal.measures)
                ]
            )
        )

        self.meal_layout.addWidget(img_label)
        self.meal_layout.addWidget(name_label)
        self.meal_layout.addWidget(category_label)
        self.meal_layout.addWidget(area_label)
        self.meal_layout.addWidget(instructions_label)
        self.meal_layout.addWidget(instructions_text)
        self.meal_layout.addWidget(ingredients_label)
        self.meal_layout.addWidget(ingredients_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
