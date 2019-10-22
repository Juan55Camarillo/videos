'''
Created on 1 oct 2019

@author: Usuario
'''
# Structure of Qt5 GUIs

#Imports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.Qt import QIcon, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,\
    QWidget

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.iniUI()
    
    
    
    def initUI(self):
        self.setWindowsTitle('PyQt5 GUI')
        self.resize(400, 300)
        self.add_menus_and_status()
        
        self.horizontal_vertical_box_layout()
        
    def horizontal_vertical_box_layout(self):
        label_1 = QLabel('First Label')
        label_2 = QLabel('Another label')
        
        button_1 = QPushButton('Click 1')
        button_2 = QPushButton('Click 2')
        
        hbox_1 =QHBoxLayout()
        hbox_2 =QHBoxLayout()
        
        hbox_1.addWidget(label_1)
        hbox_1.addWidget(button_1)
        
        hbox_2.addWidget(label_2)
        hbox_2.addWidget(button_2)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        
        layout_widget = QWidget()
        layout_widget.setCentralWidget(layout_widget)
    
    def add_menus_and_status(self):
        self.statusBar().ShowMessage('Text in status bar')
        
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu('File')
        
        new_icon = QIcon('/icons/new_icon.png')
        new_action = QAction(new_icon, 'New', self)
        new_action.setStatusTip('New File')
        file_menu.addAction(new_action)
        
        file_menu.addSeparator()
        
        exit_icon = QIcon('/icons/exit_icon.png')
        exit_action = QAction(exit_icon, 'Exit', self)
        exit_action.setStatusTip('Click to exit th application')
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')
        file_menu.addAction(exit_action)
             
        edit_menu = menubar.addMenu('Edit')

        
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        gui = GUI()
        gui.show()
        sys.exit(app.exec_())
    
