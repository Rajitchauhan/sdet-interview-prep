def add_task(title):
    if not title:
        raise ValueError("Task title is required")

    return {
        "id": 1,
        "title": title,
        "completed": False
    }


def complete_task(task):
    task["completed"] = True
    return task


def is_task_completed(task):
    return task["completed"]