from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QStackedWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Life Manager")

        self.setup_central_widget()
        self.create_sidebar()
        self.create_nav_buttons()

        self.create_view_stack()
        self.create_tasks_view()
        self.create_goals_view()
        self.create_journal_view()
        self.create_finances_view()

        self.buttons_dict["tasks"].clicked.connect(
            lambda: self.stack_widget.setCurrentIndex(self.tasks_index)
        )
        self.buttons_dict["goals"].clicked.connect(
            lambda: self.stack_widget.setCurrentIndex(self.goals_index)
        )
        self.buttons_dict["journal"].clicked.connect(
            lambda: self.stack_widget.setCurrentIndex(self.journal_index)
        )
        self.buttons_dict["finances"].clicked.connect(
            lambda: self.stack_widget.setCurrentIndex(self.finances_index)
        )

    def setup_central_widget(self) -> None:
        central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        central_widget.setLayout(self.central_layout)
        self.setCentralWidget(central_widget)

    def create_sidebar(self) -> None:

        self.sidebar_widget = QWidget()
        self.sidebar_layout = QVBoxLayout()
        self.sidebar_widget.setLayout(self.sidebar_layout)
        self.central_layout.addWidget(self.sidebar_widget)

    def create_nav_buttons(self) -> None:

        self.buttons_dict: dict[str, QPushButton] = {}

        button_labels = ["tasks", "goals", "journal", "finances"]
        for label_name in button_labels:
            button = QPushButton(label_name)
            self.sidebar_layout.addWidget(button)
            self.buttons_dict[label_name] = button

    def create_view_stack(self):
        self.stack_widget = QStackedWidget()
        self.central_layout.addWidget(self.stack_widget)

    def create_tasks_view(self):
        widget = QWidget()
        self.tasks_layout = QVBoxLayout()
        widget.setLayout(self.tasks_layout)

        tasks_label = QLabel("Welcome to the Tasks Page!")
        self.tasks_layout.addWidget(tasks_label)

        self.tasks_index = self.stack_widget.addWidget(widget)

    def create_goals_view(self):
        widget = QWidget()
        self.goals_layout = QVBoxLayout()
        widget.setLayout(self.goals_layout)

        goals_label = QLabel("Welcome to the Goals Page!")
        self.goals_layout.addWidget(goals_label)

        self.goals_index = self.stack_widget.addWidget(widget)

    def create_journal_view(self):
        widget = QWidget()
        self.journal_layout = QVBoxLayout()
        widget.setLayout(self.journal_layout)

        journal_label = QLabel("Welcome to the Journal Page!")
        self.journal_layout.addWidget(journal_label)

        self.journal_index = self.stack_widget.addWidget(widget)

    def create_finances_view(self):
        widget = QWidget()
        self.finances_layout = QVBoxLayout()
        widget.setLayout(self.finances_layout)

        finances_label = QLabel("Welcome to the Finances Page!")
        self.finances_layout.addWidget(finances_label)

        self.finances_index = self.stack_widget.addWidget(widget)
