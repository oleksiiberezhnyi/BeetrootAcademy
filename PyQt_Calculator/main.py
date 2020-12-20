from ui import CalculatorUI
from controller import CalculatorController
import sys
from PyQt5.QtWidgets import QApplication


def main():
    calculator = QApplication(sys.argv)
    ui = CalculatorUI()
    ui.show()
    CalculatorController(ui=ui)
    sys.exit(calculator.exec_())


if __name__ == '__main__':
    main()
