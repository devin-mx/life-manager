from PySide6.QtWidgets import (
    QCheckBox,
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
)
from core.tasks import get_all_tasks, delete_task, add_task, toggle_task_done
from db.models import Task
from ui.dialogs.add_tasks_dialog import AddTaskDialog


class TasksView(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Done", "Title", "Description", "Due Date", "X"]
        )
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setAlternatingRowColors(True)

        self.table.setColumnWidth(0, 60)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 500)
        self.table.setColumnWidth(3, 100)
        self.table.setColumnWidth(4, 100)

        self.main_layout.addWidget(self.table)

        self.create_add_task_button()

        self.refresh_tasks()

    def _on_delete(self, tid: int) -> None:
        delete_task(tid)
        self.refresh_tasks()

    def _on_toggle_done(self, tid: int) -> None:
        toggle_task_done(tid)
        self.refresh_tasks()

    def refresh_tasks(self) -> None:
        tasks: list[Task] = get_all_tasks()
        self.table.setRowCount(len(tasks))

        for i, task in enumerate(tasks):
            done_check_box = QCheckBox()
            done_check_box.blockSignals(True)
            done_check_box.setChecked(task.done)
            done_check_box.blockSignals(False)
            done_check_box.clicked.connect(
                lambda _, tid=task.id: self._on_toggle_done(tid)
            )
            self.table.setCellWidget(i, 0, done_check_box)

            self.table.setItem(i, 1, QTableWidgetItem(task.title))

            if task.description == "":
                self.table.setItem(i, 2, QTableWidgetItem("No Description"))
            else:
                self.table.setItem(i, 2, QTableWidgetItem(task.description))

            self.table.setItem(
                i, 3, QTableWidgetItem(task.due_date.strftime("%d %m %Y"))
            )
            delete_button = QPushButton("Delete")
            self.table.setCellWidget(i, 4, delete_button)

            delete_button.clicked.connect(lambda _, tid=task.id: self._on_delete(tid))

    def open_dialog(self):
        dialog = AddTaskDialog(self)
        if dialog.exec():
            title, due_date, description = dialog.get_data()
            add_task(title, due_date, description)
            self.refresh_tasks()

    def create_add_task_button(self):
        button = QPushButton("Add Task")
        self.main_layout.addWidget(button)
        button.clicked.connect(self.open_dialog)
