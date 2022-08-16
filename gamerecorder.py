from database import Database
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGridLayout
from ui.ui_game_widget import Ui_game
from ui.ui_player_widget import Ui_player
from ui.ui_series_widget import Ui_series

class QSeries(QWidget, Ui_series):
    def __init__(self, db, parent=None):
        super(QSeries, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.addGame_btn.clicked.connect(self.add_game_widget)
        self.add_game_widget()
        self.submit_series_btn.clicked.connect(self.submit_series)

    def add_game_widget(self):
        game_count = self.s_layout.count()
        self.s_layout.insertWidget(game_count-1, QGame(self.db, game_count))

    def submit_series(self):
        print(self.s_layout.count())
        for obj in self.s_widget.children():
            if isinstance(obj, QGame):
                game = obj.get_game()
                self.db.record_game('next', game['players'], game['lead'], game['winner'], game['tosses'])
                self.db.push()
                obj.rm_game_widget()

class QGame(QWidget, Ui_game):
    def __init__(self, db, game_count, parent=None):
        super(QGame, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.pushButton.clicked.connect(self.add_player_widget)
        self.rm_GAME.clicked.connect(self.rm_game_widget)
        self.add_player_widget()
        self.add_player_widget()
        self.label.setText(f"Game: {game_count}")

    def add_player_widget(self):
        self.game_player_layout.insertWidget(-1, QPlayer(self.db))

    def rm_game_widget(self):
        self.setParent(None)

    def get_game(self):
        game = {'players': (),
                'lead': (),
                'winner': (),
                'tosses': ()}
        for obj in self.children():
            if isinstance(obj, QPlayer):
                game['tosses'] += (obj.plyr_score_edit.text(),)
                game['players'] += (obj.plyr_name_edit.text(),)
                if obj.lead_chk.isChecked():
                    game['lead'] = obj.plyr_name_edit.text()
                if obj.win_chk.isChecked():
                    game['winner'] = obj.plyr_name_edit.text()
        return game

class QPlayer(QWidget, Ui_player):
    def __init__(self, db, parent=None):
        super(QPlayer, self).__init__(parent)
        self.setupUi(self)
        self.db = db
        self.remove_player.clicked.connect(self.rm_player_widget)
        self.plyr_score_edit.textChanged.connect(self.score_changed)
    
    def rm_player_widget(self):
        self.setParent(None)

    def score_changed(self):
        tosses_str = self.plyr_score_edit.text()
        tosses = [int(a) for a in tosses_str]
        if len(tosses) != int(3*9) or any([p > 4 for p in tosses]):
            self.label.setText(f"Score: ---")
        else:
            score = self.db._score(tosses)
            self.label.setText(f"Score: {sum(score)}")