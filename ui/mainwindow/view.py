from ..qt import *
from ..style import *

class UI_MainWindow(object):
    
    def setup_ui(self, parent) -> None:
        
        if not parent.objectName():
            parent.setObjectName('MainWindow')
            
        with open('./ui/style/default.qss', 'r') as file:
            style = file.read()
            
        parent.setWindowTitle("GetSongs")
        parent.resize(1280, 720)
        parent.setMinimumSize(800, 600)
        parent.setStyleSheet(style)
        parent.showMaximized()
                        
        self.central_frame = QFrame(parent)
        self.central_frame.setObjectName('central_frame')

        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self.superior_bar = QFrame(parent)
        self.superior_bar.setObjectName('superior_bar')
        self.superior_bar.setFixedHeight(40)

        self.superior_bar_layout = QHBoxLayout(self.superior_bar)
        self.superior_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.superior_bar_layout.setSpacing(0)

        self.menu_bar = QMenuBar(self.superior_bar)
        self.menu_bar.setFixedHeight(40)
        self.menu_bar.setContentsMargins(10, 10, 10, 10)
        self.file_menu = QMenu('Arquivo', self.menu_bar)
        self.action_new = QAction('Novo', self.file_menu)
        self.action_open = QAction('Abrir', self.file_menu)
        self.action_save = QAction('Salvar', self.file_menu)
        self.action_saveas = QAction('Salvar como', self.file_menu)
        self.action_close = QAction('Fechar', self.file_menu)
        self.file_menu.addAction(self.action_new)
        self.file_menu.addAction(self.action_open)
        self.file_menu.addAction(self.action_save)
        self.file_menu.addAction(self.action_saveas)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.action_close)
        self.menu_bar.addMenu(self.file_menu)
        self.superior_bar_layout.addWidget(self.menu_bar, alignment=Qt.AlignLeft)
        
        self.blank_space = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.superior_bar_layout.addItem(self.blank_space)
                
        self.main_layout.addWidget(self.superior_bar)
        
        self.content_frame = QWidget(parent)
        self.content_frame.setObjectName('content_frame')
        
        self.content_frame_layout = QVBoxLayout(self.content_frame)
        self.content_frame_layout.setAlignment(Qt.AlignTop)
        self.content_frame.setLayout(self.content_frame_layout)
        
        self.scroll_area = QScrollArea(parent)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.content_frame)
        
        self.main_layout.addWidget(self.scroll_area)
        
        self.buttons_bar = QFrame(parent)
        self.buttons_bar.setObjectName('buttons_bar')
        self.buttons_bar.setFixedHeight(40)
        
        self.buttons_bar_layout = QHBoxLayout(self.buttons_bar)
        self.buttons_bar_layout.setContentsMargins(5, 5, 5, 5)
        self.buttons_bar_layout.setSpacing(5)
        
        self.button_add_song = QPushButton('Adicionar música', self.buttons_bar)
        self.buttons_bar_layout.addWidget(self.button_add_song)
        
        self.button_remove_song = QPushButton('Remover música', self.buttons_bar)
        self.buttons_bar_layout.addWidget(self.button_remove_song)
        
        # self.bottom_bar_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        # self.buttons_bar_layout.addSpacerItem(self.bottom_bar_spacer)
        
        self.progress_bar = QProgressBar(self.buttons_bar)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setEnabled(False)
        self.buttons_bar_layout.addWidget(self.progress_bar)

        self.button_search_links = QPushButton('Buscar links', self.buttons_bar)
        self.buttons_bar_layout.addWidget(self.button_search_links)
        
        self.button_export_hymn = QPushButton('Exportar hinário', self.buttons_bar)
        self.buttons_bar_layout.addWidget(self.button_export_hymn)
        
        self.main_layout.addWidget(self.buttons_bar)

        parent.setCentralWidget(self.central_frame)
        self.parent = parent