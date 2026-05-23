import os
import sys
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QApplication
from db.database import engine
from ui.main_window import MainWindow
from db.models import Base

Base.metadata.create_all(engine)

app = QApplication(sys.argv)

font_path = os.path.join("ui", "fonts", "Perfect DOS VGA 437.ttf")
if os.path.exists(font_path):
    font_id = QFontDatabase.addApplicationFont(font_path)

    if font_id != -1:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        terminal_font = QFont(font_family, 12)
        terminal_font.setStyleStrategy(QFont.StyleStrategy.NoAntialias)
        app.setFont(terminal_font)
        print("Font Loaded Successfully!")
    else:
        print("Font file found, but failed to register with Qt.")
else:
    print(f"Could not find font at {font_path}. Using fallback.")


window = MainWindow()

with open("style.qss", "r") as f:
    app.setStyleSheet(f.read())

window.show()
app.exec()
