import sys    
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
  
class GifWidget(QWidget):  
    def __init__(self, gif_path):  
        super().__init__()  
        self.initUI(gif_path)  
    def quit(self):  
        self.close()  
        QApplication.quit()  
    def initUI(self, gif_path):
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.SubWindow)  #|Qt.WindowStaysOnTopHint 置顶
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.repaint()
        layout = QVBoxLayout()  
        self.label = QLabel()  
        layout.addWidget(self.label)  
        self.setLayout(layout)  
        self.movie = QMovie(gif_path)  
        self.movie.setSpeed(400)  
        self.label.setMovie(self.movie) 
        self.movie.start()  
        iconpath = os.path.join('Elaina.jpg')
        quit_action = QAction('退出', self, triggered=self.quit)
        quit_action.setIcon(QIcon(iconpath))
        self.tray_icon_menu = QMenu(self)
        self.tray_icon_menu.addAction(quit_action)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(iconpath))
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True
            self.mouse_drag_pos = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos() - self.mouse_drag_pos)
            event.accept()
    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))
 
  
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    gif_path = 'gif.gif'  
    widget = GifWidget(gif_path)  
    widget.show()  
    sys.exit(app.exec_())