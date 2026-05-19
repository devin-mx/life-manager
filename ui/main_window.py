from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QStackedWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
)
from ui.views.tasks import TasksView
from ui.views.goals import GoalsView
from ui.views.journal import JournalView
from ui.views.finances import FinancesView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Life Manager")

        self.setup_central_widget()
        self.create_sidebar()
        self.create_nav_buttons()

        self.create_view_stack()
        self.tasks_view = TasksView()
        self.tasks_index = self.stack_widget.addWidget(self.tasks_view)
        self.goals_view = GoalsView()
        self.goals_index = self.stack_widget.addWidget(self.goals_view)
        self.journal_view = JournalView()
        self.journal_index = self.stack_widget.addWidget(self.journal_view)
        self.finances_view = FinancesView()
        self.finances_index = self.stack_widget.addWidget(self.finances_view)

        self.buttons_dict["Tasks"].clicked.connect(
            lambda: self.stack_widget.setCurrentIndex(self.tasks_index)
        )
        self.buttons_dict["Goals"].clicked.connect(
            lambda: self.stack_widget.setCurrentIndex(self.goals_index)
        )
        self.buttons_dict["Journal"].clicked.connect(
            lambda: self.stack_widget.setCurrentIndex(self.journal_index)
        )
        self.buttons_dict["Finances"].clicked.connect(
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

        button_labels = ["Tasks", "Goals", "Journal", "Finances"]
        for label_name in button_labels:
            button = QPushButton(label_name)
            self.sidebar_layout.addWidget(button)
            self.buttons_dict[label_name] = button

    def create_view_stack(self):
        self.stack_widget = QStackedWidget()
        self.central_layout.addWidget(self.stack_widget)
