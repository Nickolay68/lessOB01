class Task:
    def __init__(self, description, due_date, status=False):
        """
        Инициализация задачи
        :param description: строка, описание задачи
        :param due_date: строка, срок выполнения задачи
        :param status: логическое значение, статус выполнения задачи (False - не выполнено, True - выполнено)
        """
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"Описание: {self.description}, Срок: {self.due_date}, Статус: {'Выполнено' if self.status else 'Не выполнено'}"


class TaskManager:
    def __init__(self):
        """
        Инициализация менеджера задач
        """
        self.tasks = []

    def add_task(self, task):
        """
        Добавление задачи в список
        :param task: объект Task
        """
        self.tasks.append(task)

    def remove_completed_tasks(self):
        """
        Удаление выполненных задач из списка
        """
        self.tasks = [task for task in self.tasks if not task.status]

    def show_pending_tasks(self):
        """
        Вывод всех невыполненных задач
        """
        print("Текущие невыполненные задачи:")
        for task in self.tasks:
            if not task.status:
                print(task)


# Пример использования
task_manager = TaskManager()

# Добавление задач
task1 = Task("Купить продукты", "2024-08-10", True)
task2 = Task("Сделать домашнее задание", "2024-08-15", True)
task3 = Task("Позвонить маме", "2024-09-12")


# Показать невыполненные задачи
task_manager.show_pending_tasks()

# Удалить выполненные задачи
task_manager.remove_completed_tasks()

task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

print("\nПосле удаления выполненных задач:")
task_manager.show_pending_tasks()