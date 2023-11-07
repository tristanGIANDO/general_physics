from qtpy.QtCore import Qt
from qtpy.QtWidgets import QApplication

from superqt import QLabeledDoubleSlider

app = QApplication([])

slider = QLabeledDoubleSlider(Qt.Orientation.Horizontal)
slider.setRange(0, 2000.5999)
slider.setValue(1.3)
slider.show()

app.exec_()
