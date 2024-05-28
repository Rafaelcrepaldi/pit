class TaskManager:
    tasks = []

    @staticmethod
    def add_task(task):
        TaskManager.tasks.append(task)

    @staticmethod
    def remove_task(task_index):
        if 0 <= task_index < len(TaskManager.tasks):
            del TaskManager.tasks[task_index]

    @staticmethod
    def get_tasks():
        return TaskManager.tasks
