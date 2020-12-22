from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLineEdit

ERROR = 'ERROR'


class CalculatorUI(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(310, 460)
        self.main_window = QWidget(self)
        self.general_layout = QVBoxLayout(self)
        self._create_display()
        self._create_buttons()
        QWidget.setStyleSheet(self, 'background: rgba(200,225,250,1);'
                              )
        self.general_layout.setContentsMargins(20, 20, 20, 20)
        self.general_layout.setSpacing(20)
        self.general_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.display_text = ''

    def _create_display(self):
        self.display = QLineEdit()
        self.display.setFixedSize(270, 60)
        self.display.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet('background: rgba(250,253,255,0.7);'
                                   'border-radius: 10px;'
                                   'padding: 10px;'
                                   'margin: 0;'
                                   'font-size: 30px;')
        self.general_layout.addWidget(self.display)

    def _create_buttons(self):
        buttons_digits = {'7': (1, 0),
                          '8': (1, 1),
                          '9': (1, 2),
                          '4': (2, 0),
                          '5': (2, 1),
                          '6': (2, 2),
                          '1': (3, 0),
                          '2': (3, 1),
                          '3': (3, 2),
                          '0': (4, 0, 1, 2)
                          }
        buttons_operand = {'AC': (0, 0),
                           '(': (0, 1),
                           ')': (0, 2),
                           '÷': (0, 3),
                           '×': (1, 3),
                           '−': (2, 3),
                           '+': (3, 3),
                           ',': (4, 2),
                           '=': (4, 3)
                           }

        self.buttons_digits = {}
        self.buttons_operand = {}
        buttons_grid = QGridLayout()
        buttons_grid.setSpacing(10)
        for button_text, position in buttons_digits.items():
            self.buttons_digits[button_text] = QPushButton(button_text)
            self.buttons_digits[button_text].setStyleSheet('QPushButton'
                                                           '{'
                                                           'background: rgba(145,150,155,1);'
                                                           'border-radius: 30px;'
                                                           'color: black;'
                                                           'margin: 0;'
                                                           'padding: 0;'
                                                           'font-size: 24px;'
                                                           '}'
                                                           'QPushButton::pressed'
                                                           '{'
                                                           'background: rgba(60,120,170,1);'
                                                           'border-radius: 30px;'
                                                           'color: white;'
                                                           'margin: 0;'
                                                           'padding: 0;'
                                                           'font-size: 24px;'
                                                           'font-weight: bold;'
                                                           '}'
                                                           )
            if len(position) == 2:
                self.buttons_digits[button_text].setFixedSize(60, 60)
                buttons_grid.addWidget(self.buttons_digits[button_text],
                                       position[0],
                                       position[1]
                                       )
            elif len(position) == 4:
                self.buttons_digits[button_text].setFixedSize(130, 60)
                buttons_grid.addWidget(self.buttons_digits[button_text],
                                       position[0],
                                       position[1],
                                       position[2],
                                       position[3]
                                       )
            self.general_layout.addLayout(buttons_grid)
        for button_text, position in buttons_operand.items():
            self.buttons_operand[button_text] = QPushButton(button_text)
            self.buttons_operand[button_text].setStyleSheet('QPushButton'
                                                            '{'
                                                            'background: rgba(35,70,100,1);'
                                                            'border-radius: 30px;'
                                                            'color: white;'
                                                            'margin: 0;'
                                                            'padding: 0;'
                                                            'font-size: 22px;'
                                                            '}'
                                                            'QPushButton::pressed'
                                                            '{'
                                                            'background: rgba(60,120,170,1);'
                                                            'border-radius: 30px;'
                                                            'color: black;'
                                                            'margin: 0;'
                                                            'padding: 0;'
                                                            'font-size: 22px;'
                                                            'font-weight: bold;'
                                                            '}'
                                                            )
            self.buttons_operand[button_text].setFixedSize(60, 60)
            buttons_grid.addWidget(self.buttons_operand[button_text],
                                   position[0],
                                   position[1]
                                   )
            self.general_layout.addLayout(buttons_grid)

    def set_display_text(self, text):
        operand = ['+', '-', '*', '/', '.']
        if self.display_text[-1:] in operand and text in operand:
            pass
        elif text == '=':
            try:
                self.display_text = str(round(eval(self.display_text), 6))
            except:
                self.display_text = ERROR
        else:
            self.display_text += text
        self.display.setText(self.display_text)
        self.display.setFocus()

    def clear_display(self):
        self.display.setText('')
        self.display_text = ''
