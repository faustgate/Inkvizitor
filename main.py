from PyQt4 import QtCore, QtGui, uic
import sys
import engine


class Inkvizitor(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # widget.resize(250, 150)
        # widget.setWindowTitle('simple')
        uic.loadUi('main.ui', self)
        self.btn_open_folder.clicked.connect(self._get_start_folder_name)
        self.btn_open_list.clicked.connect(lambda: self._get_file_name("play"))
        self.btn_open_excpt.clicked.connect(lambda: self._get_file_name("exc"))
        self.btn_start.clicked.connect(self.start)
        # # self.pB.clicked.connect(self.draw_cross)
        # self.pushButton.clicked.connect(self.draw_ukraine)
        # self.pB_rus.clicked.connect(self.draw_parasha)
        # self.today = dt.datetime.now()

    def _get_start_folder_name(self):
        dialog = QtGui.QFileDialog()
        dialog.setFileMode(QtGui.QFileDialog.DirectoryOnly)
        options = QtGui.QFileDialog.ShowDirsOnly|QtGui.QFileDialog.DontResolveSymlinks
        filee = dialog.getExistingDirectory(self, "Open Files", '~', options=options)
        if filee != '':
            self.edit_folder_path.setText(filee)

    def _get_file_name(self, mode):
        dialog = QtGui.QFileDialog()
        options = QtGui.QFileDialog.ReadOnly
        filee = dialog.getOpenFileName(self, "Open Files", '~', "(*.m3u)")
        if filee != '':
            if mode == 'play':
                self.edit_playlist_path.setText(filee)
            else:
                self.edit_exceptions_path.setText(filee)

    def start(self):
        eng=engine.Engine()
        eng.start(str(self.edit_folder_path.text()),
                  str(self.edit_playlist_path.text()),
                  str(self.edit_exceptions_path.text()))


app = QtGui.QApplication(sys.argv)
renamer = Inkvizitor()
renamer.show()
sys.exit(app.exec_())