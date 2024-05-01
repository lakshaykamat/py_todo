import sys

from PyQt5.QtWidgets import QApplication

from TodoApp import TodoApp


def main():
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    todo_app.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
