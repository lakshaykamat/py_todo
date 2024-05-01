from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from TodoList import TodoList
from PyQt5.QtCore import Qt


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(300, 200)
        self.setMaximumSize(600, 400)
        self.todo_list = TodoList()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Todo List App')
        layout = QVBoxLayout()

        self.task_input = QLineEdit()
        self.task_input.setFont(QFont("Arial", 12))
        layout.addWidget(self.task_input)

        add_button = QPushButton('Add Task')
        add_button.setFont(QFont("Arial", 12))
        add_button.clicked.connect(self.add_task)
        layout.addWidget(add_button)

        self.task_list = QListWidget()
        self.task_list.setFont(QFont("Arial", 12))
        self.task_list.itemClicked.connect(
            self.mark_task_completed)  # Connect itemClicked signal to mark_task_completed
        layout.addWidget(self.task_list)

        self.setLayout(layout)

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.todo_list.add_todo(task)
            self.update_task_list()

    def update_task_list(self):
        self.task_list.clear()
        todos = self.todo_list.get_todos()
        for todo in todos:
            task_text = todo["task"]
            completed = todo["completed"]
            task_item = QListWidgetItem(task_text)  # Create a QListWidgetItem
            task_item.setFlags(task_item.flags() | Qt.ItemIsUserCheckable)  # Enable checkable behavior
            task_item.setCheckState(Qt.Checked if completed else Qt.Unchecked)  # Set initial check state
            self.task_list.addItem(task_item)

    def mark_task_completed(self, item):
        index = self.task_list.row(item)
        self.todo_list.mark_completed(index)
        self.update_task_list()
