from database import Database
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGridLayout
from PySide6.QtGui import QPen, QColor
from PySide6.QtCore import Qt
from ui.ui_plotter import Ui_plotter
from ui.ui_player_item_widget import Ui_player_list_item
import seaborn as sns

class QPlot(QWidget, Ui_plotter):
    def __init__(self, db, plot_fnc, parent=None):
        super(QPlot, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.plot_fnc = plot_fnc
        self.player_names = self.db.search("SELECT player_name From Players")
        self.colors = sns.color_palette("husl", len(self.player_names))
        for nm, clr in zip(self.player_names, self.colors):
            name = nm[0]
            color = tuple(int(c*255) for c in clr)
            self.verticalLayout.insertWidget(0, QLegendItem(name, color))
        self.plot.setBackground("#303338")
        self.plot_data()
    
    def plot_data(self):
        player_names = self.db.search("SELECT player_name From Players")
        for nm, clr in zip(self.player_names, self.colors):
            name = nm[0]
            r, g, b = tuple(int(c*255) for c in clr)
            data = self.plot_fnc(self.db, name)
            pen = QPen(QColor(r, g, b))
            pen.setWidth(9)
            pen.setCapStyle(Qt.RoundCap)
            pen.setJoinStyle(Qt.RoundJoin)
            self.plot.plot(*zip(*data), pen=QColor(r, g, b), name=name)
        

class QLegendItem(QWidget, Ui_player_list_item):
    def __init__(self, name, color, parent=None):
        super(QLegendItem, self).__init__(parent)
        self.setupUi(self)
        self.display_check.setText(name)
        self.display_check.setChecked(True)
        self.color.setStyleSheet(f"background-color: rgb({color[0]}, {color[1]}, {color[2]})")