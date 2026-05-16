from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class TasksView(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        label = QLabel("Welcome on the Tasks Page!")
        self.main_layout.addWidget(label)
