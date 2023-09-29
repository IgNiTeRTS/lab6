import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        '''Оси выравнивания'''
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_irst = QHBoxLayout()
        self.hbox_result = QHBoxLayout()
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_irst)
        self.vbox.addLayout(self.hbox_result)
        '''Виджеты к осям'''
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)
        self.b_1 = QPushButton("1", self)
        self.hbox_irst.addWidget(self.b_1)
        self.b_2 = QPushButton("2", self)
        self.hbox_irst.addWidget(self.b_2)
        self.b_3 = QPushButton("3", self)
        self.hbox_irst.addWidget(self.b_3)
        self.b_plus = QPushButton("+", self)
        self.hbox_irst.addWidget(self.b_plus)
        self.b_minus = QPushButton("-", self)
        self.hbox_irst.addWidget(self.b_minus)
        self.b_multiply = QPushButton("*", self)
        self.hbox_irst.addWidget(self.b_multiply)
        self.b_divide = QPushButton("/", self)
        self.hbox_irst.addWidget(self.b_divide)
        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)
        '''Реакции на кнопки'''
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiply.clicked.connect(lambda: self._operation("*"))
        self.b_divide.clicked.connect(lambda: self._operation("/"))
        self.b_result.clicked.connect(self._result)
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    def _operation(self, op):
        self.num_1 = int(self.input.text())
        self.op = op
        self.input.setText("")

    def _result(self):
        self.num_2 = int(self.input.text())
        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))
        if self.op == '-':
            self.input.setText(str(self.num_1 - self.num_2))
        if self.op == '*':
            self.input.setText(str(self.num_1 * self.num_2))
        if self.op == '/':
            if self.num_2 == '0':
                self.input.setText('На ноль делить нельзя')
            else:
                self.input.setText(str(self.num_1 / self.num_2))
app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())