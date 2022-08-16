from PySide6 import QtWidgets
from dashboard import MainWindow
import pyqtgraph.graphicsItems.ViewBox.axisCtrlTemplate_pyside6
import pyqtgraph.graphicsItems.PlotItem.plotConfigTemplate_pyside6
import pyqtgraph.imageview.ImageViewTemplate_pyside6
import pyqtgraph.console.template_pyside6
import qdarkstyle
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))

    window = MainWindow()
    window.show()
    app.exec()