from PyQt5.QtWidgets import QApplication
from gui.main_window import RedEyeMainWindow
import sys

def main():
    app = QApplication(sys.argv)
    window = RedEyeMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
