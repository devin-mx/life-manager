import sys
from PySide6.QtWidgets import QApplication
from db.database import engine
from ui.main_window import MainWindow
from db.models import Base

Base.metadata.create_all(engine)

app = QApplication(sys.argv)
window = MainWindow()

with open("style.qss", "r") as f:
    app.setStyleSheet(f.read())

window.show()
app.exec()
