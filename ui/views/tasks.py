from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
)
from core.tasks import get_all_tasks, delete_task
from db.models import Task


class TasksView(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Done", "Title", "Description", "Due Date", "🗑️"]
        )
        self.main_layout.addWidget(self.table)

        self.refresh_tasks()

    def _on_delete(self, tid: int) -> None:
        delete_task(tid)
        self.refresh_tasks()

    def refresh_tasks(self) -> None:
        tasks: list[Task] = get_all_tasks()
        self.table.setRowCount(len(tasks))

        for i, task in enumerate(tasks):
            self.table.setItem(i, 0, QTableWidgetItem(str(task.done)))
            self.table.setItem(i, 1, QTableWidgetItem(task.title))
            self.table.setItem(
                i, 3, QTableWidgetItem(task.due_date.strftime("%d %m %Y"))
            )

            if task.description == "":
                self.table.setItem(i, 2, QTableWidgetItem("No Description"))
            else:
                self.table.setItem(i, 2, QTableWidgetItem(task.description))

            delete_button = QPushButton("Delete")
            self.table.setCellWidget(i, 4, delete_button)

            delete_button.clicked.connect(lambda _, tid=task.id: self._on_delete(tid))
