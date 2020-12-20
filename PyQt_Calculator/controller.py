from ui import CalculatorUI
from functools import partial


class CalculatorController:

    def __init__(self, ui: CalculatorUI):
        self._ui = ui
        # self._exp = exp
        self._connect_signals()

    def _connect_signals(self):
        for button_text, position in self._ui.buttons_digits.items():
            position.clicked.connect(partial(self._ui.set_display_text,
                                             button_text
                                             )
                                     )
        self._ui.buttons_operand['AC'].clicked.connect(self._ui.clear_display)
        self._ui.buttons_operand['='].clicked.connect(
            partial(self._ui.set_display_text,
                    '='
                    )
            )
        self._ui.buttons_operand['+'].clicked.connect(
            partial(self._ui.set_display_text,
                    '+'
                    )
            )
        self._ui.buttons_operand['−'].clicked.connect(
            partial(self._ui.set_display_text,
                    '-'
                    )
            )
        self._ui.buttons_operand['×'].clicked.connect(
            partial(self._ui.set_display_text,
                    '*'
                    )
            )
        self._ui.buttons_operand['÷'].clicked.connect(
            partial(self._ui.set_display_text,
                    '/'
                    )
            )
        self._ui.buttons_operand[','].clicked.connect(
            partial(self._ui.set_display_text,
                    '.'
                    )
            )
        self._ui.buttons_operand['('].clicked.connect(
            partial(self._ui.set_display_text,
                    '('
                    )
            )
        self._ui.buttons_operand[')'].clicked.connect(
            partial(self._ui.set_display_text,
                    ')'
                    )
            )

    def _calculate_result(self):
        self._ui.display.setText('result')
