import sys
from PySide6.QtWidgets import QApplication
from db.database import engine
from ui.main_window import MainWindow
from db.models import Base

Base.metadata.create_all(engine)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
