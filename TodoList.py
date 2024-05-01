class TodoList:
    def __init__(self):
        self.__all_todos = []

    def add_todo(self, todo):
        self.__all_todos.append({"task": todo, "completed": False})

    def mark_completed(self, index):
        if 0 <= index < len(self.__all_todos):
            self.__all_todos[index]["completed"] = True

    def get_todos(self):
        return self.__all_todos
