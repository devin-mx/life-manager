from datetime import datetime
from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import (
    QDateTimeEdit,
    QDialog,
    QDialogButtonBox,
    QLineEdit,
    QTextEdit,
    QVBoxLayout,
)


class AddTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Enter Task Data!")

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.title_entry = QLineEdit()
        self.main_layout.addWidget(self.title_entry)

        self.description_entry = QTextEdit()
        self.main_layout.addWidget(self.description_entry)

        self.due_date_entry = QDateTimeEdit()
        self.due_date_entry.setDateTime(QDateTime.currentDateTime())
        self.due_date_entry.setDisplayFormat("dd MM yyyy")
        self.due_date_entry.setCalendarPopup(True)
        self.main_layout.addWidget(self.due_date_entry)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.main_layout.addWidget(buttons)

    def get_data(self) -> tuple[str, datetime, str]:
        title = self.title_entry.text()
        description = self.description_entry.toPlainText()

        qt_dt = self.due_date_entry.dateTime()
        due_date = datetime(
            qt_dt.date().year(), qt_dt.date().month(), qt_dt.date().day()
        )

        return title, due_date, description
