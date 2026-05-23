from PySide6.QtWidgets import (
    QGraphicsDropShadowEffect,
    QLabel,
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
from ui.crt_overlay import CRTOverlay


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

        # CRT Overlay - Keep on the bottom

        self._crt = CRTOverlay(self.centralWidget())
        self._crt.resize(self.centralWidget().size())

    def setup_central_widget(self) -> None:
        central_widget = QWidget()
        self.central_layout = QHBoxLayout()
        central_widget.setLayout(self.central_layout)
        self.setCentralWidget(central_widget)

    def create_sidebar(self) -> None:

        self.sidebar_widget = QWidget()
        self.sidebar_widget.setObjectName("sidebar")
        self.sidebar_layout = QVBoxLayout()
        self.sidebar_widget.setLayout(self.sidebar_layout)

        sidebar_title = QLabel("== CORESYS v0.0 ==")
        sidebar_title.setStyleSheet(
            """
            color: #FFB000;
            margin-bottom: 10px;
            font-weight: bold;
            padding: 10px;
            background-color: transparent;
            """
        )
        self.apply_amber_glow(sidebar_title, 10)
        self.sidebar_layout.addWidget(sidebar_title)

        self.central_layout.addWidget(self.sidebar_widget)

    def create_nav_buttons(self) -> None:

        self.buttons_dict: dict[str, QPushButton] = {}

        button_labels = ["Tasks", "Goals", "Journal", "Finances"]
        for label_name in button_labels:
            button = QPushButton(f"█ {label_name}")
            self.sidebar_layout.addWidget(button)
            self.buttons_dict[label_name] = button

            self.apply_amber_glow(button, 15)

        self.sidebar_layout.addStretch(1)

    def create_view_stack(self):
        self.stack_widget = QStackedWidget()
        self.central_layout.addWidget(self.stack_widget)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._crt.resize(self.centralWidget().size())
        self._crt.raise_()

    def apply_amber_glow(self, widget: QWidget, radius=12) -> None:

        glow = QGraphicsDropShadowEffect(widget)
        glow.setOffset(0, 0)
        glow.setColor("#FFB000")
        glow.setBlurRadius(radius)
        widget.setGraphicsEffect(glow)
