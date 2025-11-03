import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# --- Paths ---
GIF_PATH = "F:/Projects/Meh/Evernight/giphy.gif"
ICON_PATH = "F:/Projects/Meh/Evernight/icon.ico"  # keeps window icon

class TransparentGIFOverlay(QWidget):
    def __init__(self):
        super().__init__()

        # ---- Window setup ----
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # ---- Label and GIF ----
        self.label = QLabel(self)
        self.label.setStyleSheet("background: transparent;")

        self.movie = QMovie(GIF_PATH)
        self.label.setMovie(self.movie)
        self.movie.start()

        # ---- Size and position ----
        self.resize(320, 320)
        screen = QApplication.primaryScreen().availableGeometry()
        margin = -15
        x = screen.right() - self.width() - margin
        y = screen.bottom() - self.height() - margin
        self.move(x, y)

        # ---- App icon ----
        self.setWindowIcon(QIcon(ICON_PATH))

        # ---- State ----
        self.dragging = False
        self.locked = True
        print("🔒 Press 'L' to lock/unlock movement")

    # ---- Keyboard Lock ----
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_L:
            self.toggle_lock()

    # ---- Mouse Events for Drag ----
    def mousePressEvent(self, e):
        if not self.locked and e.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_start = e.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        if not self.locked and self.dragging:
            self.move(e.globalPos() - self.drag_start)

    def mouseReleaseEvent(self, e):
        self.dragging = False

    def toggle_lock(self):
        self.locked = not self.locked
        print("🔓 Unlocked" if not self.locked else "🔒 Locked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = TransparentGIFOverlay()
    overlay.show()
    sys.exit(app.exec_())
