from ui.mainwindow.songlinewidget import SongLineWidget
from ..qt import *
import sys

from .view import UI_MainWindow
from core import *


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.view = UI_MainWindow()
        self.view.setup_ui(self)
        
        if len(sys.argv) == 1:
            self.opened_file = ''
        else:
            self.opened_file = sys.argv[1]
            self.read_file()
            
        self.view.button_add_song.clicked.connect(self.add_songline)
        self.view.button_remove_song.clicked.connect(self.remove_songline)
        self.view.button_search_links.clicked.connect(self.search_links)
        self.view.button_export_hymn.clicked.connect(self.export_hymn)
        
        self.view.action_new.triggered.connect(self.new_file)
        self.view.action_open.triggered.connect(self.open_file)
        self.view.action_save.triggered.connect(self.save_file)
        self.view.action_saveas.triggered.connect(self.saveas_file)
        self.view.action_close.triggered.connect(sys.exit)
        
        self.show()
        
        
    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clear_layout(child.layout())
        
        
    def new_file(self):
        self.verify_changes()
        self.opened_file = ''
        self.clear_layout(self.view.content_frame_layout)
        for i in range(5):
            self.view.content_frame_layout.addWidget(
                SongLineWidget(i+1, self.view.content_frame)
            )
        
        
    def open_file(self):
        self.verify_changes()
        self.opened_file = QFileDialog.getOpenFileUrl(self, 'Escolha um arquivo para abrir...', filter='*.hin')[0].path()
        
        if sys.platform == 'win32':
            self.opened_file = self.opened_file[1:]
        
        if self.opened_file:
            self.clear_layout(self.view.content_frame_layout)
            self.read_file()
            

    def read_file(self):
        try:
            with open(self.opened_file, 'r') as file:
                songs = file.read().splitlines()
            for i, song in enumerate(songs):
                title, name, artist, url = song.split('|')
                self.view.content_frame_layout.addWidget(
                    SongLineWidget(i+1, title=title, name=name, artist=artist, url=url)
                )
        except Exception:
            msgbox = QMessageBox(self)
            msgbox.setIcon(QMessageBox.Icon.Critical)
            msgbox.setWindowTitle('ERRO')
            msgbox.setText('Não foi possível abrir o arquivo')
            msgbox.show()

                
    def save_file(self):
        if self.opened_file:
            if sys.platform == 'win32':
                self.opened_file = self.opened_file[1:]
            
            with open(self.opened_file, 'w') as file:
                for widget in filter(lambda item: isinstance(item, SongLineWidget), self.view.content_frame.children()):
                    file.write('|'.join(widget.get_content()) + '\n')
        else:
            self.saveas_file()
    
        
    def saveas_file(self):
        self.opened_file = QFileDialog.getSaveFileUrl(self, 'Escolha um arquivo para abrir...', filter='*.hin')[0].path()        
        if not self.opened_file.endswith('.hin'):
            self.opened_file += '.hin'
        
        if self.opened_file:
            self.save_file()
            
            
    def add_songline(self):
        index = len(self.view.content_frame.children())
        self.view.content_frame_layout.addWidget(
            SongLineWidget(index, self.view.content_frame)
        )
        
        
    def remove_songline(self):
        last_song = self.view.content_frame.children()[-1]
        
        if any(bool(item) for item in last_song.get_content()):
            response = QMessageBox.warning(
                self, 'Aviso', 'O campo não está vazio. Deseja continuar?',
                QMessageBox.No, QMessageBox.Yes
            )
            if response == int(QMessageBox.No):
                return

        self.view.content_frame_layout.removeWidget(last_song)
        last_song.setParent(None)
        del last_song
        
        
    def search_links(self):
        self.setInputsEnabled(False)
        
        q = QMessageBox.information(self, "Aguarde", "Estamos coletando os links para você :)", QMessageBox.NoButton, QMessageBox.NoButton)
        
        with GetSongLinks() as browser:
            for song in self.view.content_frame.children()[1:]:
                _, name, artist, _ = song.get_content()
                link = browser.get_link(name, artist)
                print(link)
                song.input_url.setText(link)
        
        
        self.setInputsEnabled(True)
                
                
    def export_hymn(self):
        self.setInputsEnabled(False)
        
        if any(
            not song.input_url.text().startswith('https://www.letras.mus.br/') 
            for song in self.view.content_frame.children()[1:]
        ):
            self.setInputsEnabled(True)
            QMessageBox.critical(self, 'Erro', 'Há links inválidos')
            return
        
        savefile_path = QFileDialog.getSaveFileUrl(self, 'Escolha um arquivo para abrir...')[0].path()
        if not savefile_path.endswith('.docx'):
            savefile_path += '.docx'
        
        songslist = []
        for song in self.view.content_frame.children()[1:]:
            lyrics = get_lyrics(song.input_url.text())
            lyrics['title'] = song.input_title.text()
            songslist.append(lyrics)
        
        build_doc(songslist, savefile_path)
        
        self.setInputsEnabled(True)


    def setInputsEnabled(self, opt: bool):
        for songline in self.view.content_frame.children():
            if isinstance(songline, SongLineWidget):
                songline.input_title.setEnabled(opt)
                songline.input_name.setEnabled(opt)
                songline.input_artist.setEnabled(opt)
                songline.input_url.setEnabled(opt)


    def closeEvent(self, event) -> None:
        self.verify_changes()
            
            
    def verify_changes(self):
        if not len(self.view.content_frame.children()) == 1:
            newfile = ''
            for songline in self.view.content_frame.children()[1:]:
                newfile += '|'.join(songline.get_content()) + '\n' 
            
            with open(self.opened_file, 'r') as file:
                previous = file.read()
            
            if previous != newfile:
                response = QMessageBox.warning(
                    self, 'Aviso', 'O conteúdo do arquivo foi alterado. Deseja salvá-lo?',
                    QMessageBox.No, QMessageBox.Yes
                )
                if response == int(QMessageBox.No):
                    return
            
            self.save_file()