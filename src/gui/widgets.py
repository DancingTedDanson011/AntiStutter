"""
Custom Qt Widgets for AntiStutter GUI
"""

from PyQt5.QtWidgets import (QWidget, QSlider, QLabel, QVBoxLayout,
                             QHBoxLayout, QCheckBox, QGroupBox)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QLinearGradient


class LabeledSlider(QWidget):
    """Slider with label and value display"""

    valueChanged = pyqtSignal(int)

    def __init__(self, label, min_val, max_val, default_val, suffix="", parent=None):
        super().__init__(parent)
        self.suffix = suffix

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # Label and value
        header_layout = QHBoxLayout()
        self.label = QLabel(label)
        self.value_label = QLabel(f"{default_val}{suffix}")
        self.value_label.setStyleSheet("font-weight: bold;")
        header_layout.addWidget(self.label)
        header_layout.addStretch()
        header_layout.addWidget(self.value_label)

        # Slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(min_val)
        self.slider.setMaximum(max_val)
        self.slider.setValue(default_val)
        self.slider.valueChanged.connect(self._on_value_changed)

        layout.addLayout(header_layout)
        layout.addWidget(self.slider)
        self.setLayout(layout)

    def _on_value_changed(self, value):
        self.value_label.setText(f"{value}{self.suffix}")
        self.valueChanged.emit(value)

    def value(self):
        return self.slider.value()

    def setValue(self, value):
        self.slider.setValue(value)


class LevelMeter(QWidget):
    """Audio level meter widget"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.level = 0.0
        self.setMinimumHeight(30)
        self.setMaximumHeight(30)

    def setLevel(self, level):
        """Set level (0.0 to 1.0)"""
        self.level = max(0.0, min(1.0, level))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Background
        painter.fillRect(self.rect(), QColor(50, 50, 50))

        # Level bar
        bar_width = int(self.width() * self.level)

        # Create gradient (green -> yellow -> red)
        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0.0, QColor(76, 175, 80))   # Green
        gradient.setColorAt(0.7, QColor(255, 235, 59))  # Yellow
        gradient.setColorAt(1.0, QColor(244, 67, 54))   # Red

        painter.fillRect(0, 0, bar_width, self.height(), gradient)

        # Border
        painter.setPen(QColor(100, 100, 100))
        painter.drawRect(0, 0, self.width() - 1, self.height() - 1)


class ToggleSwitch(QWidget):
    """Custom toggle switch widget"""

    toggled = pyqtSignal(bool)

    def __init__(self, label, default_state=False, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.checkbox = QCheckBox(label)
        self.checkbox.setChecked(default_state)
        self.checkbox.toggled.connect(self.toggled.emit)

        layout.addWidget(self.checkbox)
        self.setLayout(layout)

    def isChecked(self):
        return self.checkbox.isChecked()

    def setChecked(self, checked):
        self.checkbox.setChecked(checked)


class ParameterGroup(QGroupBox):
    """Group box for parameter controls"""

    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Styling
        self.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #2196F3;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)

    def addWidget(self, widget):
        self.layout.addWidget(widget)

    def addLayout(self, layout):
        self.layout.addLayout(layout)
