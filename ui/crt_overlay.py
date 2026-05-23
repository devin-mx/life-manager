from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QImage, QPainter, QPixmap


class CRTOverlay(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.scanline_gap = 8
        self.scanline_alpha = 50
        self.rgb_alpha = 6
        self.dot_size = 2

        self.blend_mode = QPainter.CompositionMode.CompositionMode_SourceOver

        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)
        self.setAutoFillBackground(False)
        self.raise_()

        self._cache: QPixmap | None = None

    def refresh(self):
        self._cache = None
        self.update()

    def resizeEvent(self, event):
        self._cache = None
        super().resizeEvent(event)

    def paintEvent(self, event):
        if self._cache is None or self._cache.size() != self.size():
            self._cache = self._build_cache()

        painter = QPainter(self)
        painter.setCompositionMode(self.blend_mode)
        painter.drawPixmap(0, 0, self._cache)
        painter.end()

    def _build_cache(self) -> QPixmap:
        dpr = self.devicePixelRatio()
        w = self.width()
        h = self.height()

        phys_w = int(w * dpr)
        phys_h = int(h * dpr)
        gap = max(1, int(self.scanline_gap * dpr))
        line_h = max(1, int(gap * 0.75))
        dark_h = gap - line_h
        dot = max(1, int(self.dot_size * dpr))

        img = QImage(phys_w, phys_h, QImage.Format.Format_ARGB32_Premultiplied)
        img.fill(Qt.GlobalColor.transparent)

        p = QPainter(img)
        p.setRenderHint(QPainter.RenderHint.Antialiasing, False)

        p.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QColor(0, 0, 0, self.scanline_alpha))

        y = line_h
        while y < phys_h:
            p.drawRect(0, y, phys_w, dark_h)
            y += gap

        rgb = self.rgb_alpha
        stripe_color = [
            QColor(255, 0, 0, rgb),
            QColor(0, 255, 0, rgb),
            QColor(0, 0, 255, rgb),
        ]

        x = 0
        while x < phys_w:
            for i, color in enumerate(stripe_color):
                p.setBrush(color)
                p.drawRect(x + i * dot, 0, dot, phys_h)
            x += dot * 4

        p.end()

        px = QPixmap.fromImage(img)
        px.setDevicePixelRatio(dpr)
        return px
