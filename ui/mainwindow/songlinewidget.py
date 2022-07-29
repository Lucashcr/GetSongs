from ..style import *
from ..qt import *

class SongLineWidget(QFrame):
    
    def __init__(self, index, parent=None, f=Qt.WindowFlags(), title='', name='', artist='', url='https://www.letras.mus.br/...') -> None:
        super().__init__(parent, f)
        
        self.setFixedHeight(90)
        self.setObjectName('SongLineWidget')
        
        self.layout = QGridLayout(self)
        
        self.layout.addWidget(QLabel(f'Música {index}', self), 0, 0, 1, 4)
        
        self.layout.addWidget(QLabel('Título', self), 1, 0, 1, 1)
        self.layout.addWidget(QLabel('Música', self), 1, 1, 1, 1)
        self.layout.addWidget(QLabel('Artista', self), 1, 2, 1, 1)
        self.layout.addWidget(QLabel('URL', self), 1, 3, 1, 1)
        
        self.input_title = QLineEdit(self)
        self.input_title.setText(title)
        self.layout.addWidget(self.input_title, 2, 0, 1, 1)
        
        self.input_name = QLineEdit(self)
        self.input_name.setText(name)
        self.layout.addWidget(self.input_name, 2, 1, 1, 1)
        
        self.input_artist = QLineEdit(self)
        self.input_artist.setText(artist)
        self.layout.addWidget(self.input_artist, 2, 2, 1, 1)
        
        self.input_url = QLineEdit(self)
        self.input_url.setText(url)
        self.layout.addWidget(self.input_url, 2, 3, 1, 1)
        
        self.setLayout(self.layout)
        
        
    def get_content(self):
        return (
            self.input_title.text(),
            self.input_name.text(),
            self.input_artist.text(),
            self.input_url.text()
        )