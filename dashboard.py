from database import Database
from tabulate import tabulate
from queries import player_scores, rolling_average, cumulative_average, shot_percent, cumulative_score

from PySide6 import QtWidgets
from ui.ui_dashboard import Ui_magDartDashboard
import pyqtgraph as pg

from gamerecorder import QSeries
from plotting import QPlot

class MainWindow(QtWidgets.QMainWindow, Ui_magDartDashboard):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # load Database
        self.db = Database('P:\Employees\Employee Folders\Stubbles\mag\mag.db')
        # Add plots
        self.score_layout.addWidget(QPlot(self.db, player_scores))
        self.aggregate_layout.addWidget(QPlot(self.db, cumulative_score))
        # add actions
        self.submit_dash.clicked.connect(self.dashboard_poulate)
        self.verticalLayout_2.addWidget(QSeries(self.db))

    def dashboard_poulate(self):
        header = ['Player', 'Wins', 'AGG Score', 'AVG Score', 'AVG Score R1', 'AVG Score R2', 'AVG Score R3', 'MAX Score', 'MIN Score']
        data = []
        players = ('alex', 'james', 'richard')
        for player in players:
            # player_ID
            plyr_id = self.db.search_one("""SELECT player_ID FROM Players WHERE player_name='{0}'""".format(player))[0]
            # Wins
            num_wins = self.db.search_one("""SELECT COUNT(*) FROM Games WHERE winner_id={0}""".format(plyr_id))
            # AGG/AVG score
            avg_score = self.db.search_one("""SELECT SUM(score), AVG(score), AVG(round1), AVG(round2), AVG(round3)
                                            From Scores WHERE player_id={0}""".format(plyr_id))
            # High Score
            outliers = self.db.search_one("""SELECT MAX(score), MIN(score) From Scores WHERE player_id={0}""".format(plyr_id))
            data.append([*((player,)+num_wins+avg_score+outliers)])
        self.display_dash.clear()
        print(tabulate(data, headers=header))
        self.display_dash.setText(tabulate(data, headers=header))

    def plot_score(self):
        players = ('alex', 'james', 'richard')
        data = []
        self.scorePlot.addLegend()
        for i, name in enumerate(players):
            data = player_scores(self.db, name)
            self.scorePlot.plot(*zip(*data), pen=(i, 3), name=name)

    def plot_avg(self):
        players = ('alex', 'james', 'richard')
        data = []
        self.averagePlot.clear()
        self.averagePlot.addLegend()
        n = self.roll_sld.value()
        if n == 51:
            # total average
            self.roll_lbl.setText('Inf')
            for i, name in enumerate(players):
                data = cumulative_average(self.db, name)
                self.averagePlot.plot(*zip(*data), pen=(i, 3), name=name)
        else:
            # rolling average
            self.roll_lbl.setText(str(n))
            for i, name in enumerate(players):
                data = rolling_average(self.db, name, n)
                self.averagePlot.plot(*zip(*data), pen=(i, 3), name=name)

    def plot_accuracy(self):
        players = ('alex', 'james', 'richard')
        color = ('r', 'g', 'b')
        self.accuracyPlot.clear()
        self.accuracyPlot.addLegend()
        rings = [0, 1, 2, 3]
        for player, c in zip(players, color):
            rings = [x+0.2 for x in rings]
            r0 = shot_percent(self.db, player, ring='=0', face='=0', stack='=0')
            r1 = shot_percent(self.db, player, ring='=1')
            r2 = shot_percent(self.db, player, ring='=2')
            r3 = shot_percent(self.db, player, ring='=3')
            p_bar = pg.BarGraphItem(x=rings, height=r0+r1+r2+r3, width=0.2, name=player, brush=c)
            self.accuracyPlot.addItem(p_bar)
