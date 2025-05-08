import sys
from PyQt5 import QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Week 9 - F1D022072")
        MainWindow.resize(600, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.menu_file = self.menubar.addMenu("File")
        self.menu_fitur = self.menubar.addMenu("Fitur")
        self.action_keluar = QtWidgets.QAction("Keluar", MainWindow)
        self.action_input_nama = QtWidgets.QAction("Input Nama", MainWindow)
        self.action_pilih_font = QtWidgets.QAction("Pilih Font", MainWindow)
        self.action_buka_file = QtWidgets.QAction("Buka File", MainWindow)
        self.menu_file.addAction(self.action_keluar)
        self.menu_fitur.addAction(self.action_input_nama)
        self.menu_fitur.addAction(self.action_pilih_font)
        self.menu_fitur.addAction(self.action_buka_file)
        self.action_keluar.triggered.connect(MainWindow.close)
        self.action_input_nama.triggered.connect(lambda: self.tabs.setCurrentIndex(0))
        self.action_pilih_font.triggered.connect(lambda: self.tabs.setCurrentIndex(1))
        self.action_buka_file.triggered.connect(lambda: self.tabs.setCurrentIndex(2))
        self.tabs = QtWidgets.QTabWidget()
        self.main_layout.addWidget(self.tabs)
        self.tab1 = QtWidgets.QWidget()
        self.layout_tab1 = QtWidgets.QVBoxLayout(self.tab1)

        self.btn_input_nama = QtWidgets.QPushButton("Input Nama")
        self.btn_input_nama.clicked.connect(self.input_nama)
        self.layout_tab1.addWidget(self.btn_input_nama)

        self.label_nama_tab1 = QtWidgets.QLabel("Nama:")
        self.layout_tab1.addWidget(self.label_nama_tab1)
        self.nama = ""
        self.tabs.addTab(self.tab1, "Input Nama")
        self.tab2 = QtWidgets.QWidget()
        self.layout_tab2 = QtWidgets.QVBoxLayout(self.tab2)

        self.btn_pilih_font = QtWidgets.QPushButton("Pilih Font")
        self.btn_pilih_font.clicked.connect(self.pilih_font)
        self.layout_tab2.addWidget(self.btn_pilih_font)

        self.label_nama_font = QtWidgets.QLabel("Nama:")
        self.layout_tab2.addWidget(self.label_nama_font)
        self.tabs.addTab(self.tab2, "Pilih Font")
        self.tab3 = QtWidgets.QWidget()
        self.layout_tab3 = QtWidgets.QVBoxLayout(self.tab3)

        self.btn_buka_file = QtWidgets.QPushButton("Buka File .txt")
        self.btn_buka_file.clicked.connect(self.buka_file)
        self.layout_tab3.addWidget(self.btn_buka_file)

        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setReadOnly(True)
        self.layout_tab3.addWidget(self.text_edit)
        self.tabs.addTab(self.tab3, "Buka File")
        MainWindow.setCentralWidget(self.centralwidget)


    def input_nama(self):
        nama, ok = QtWidgets.QInputDialog.getText(None, "Input Nama", "Masukkan nama:")
        if ok and nama:
            self.nama = nama
            self.label_nama_tab1.setText(f"Nama: {nama}")
            self.label_nama_font.setText(f"Nama: {nama}")

    def pilih_font(self):
        font, ok = QtWidgets.QFontDialog.getFont()
        if ok:
            self.label_nama_font.setFont(font)

    def buka_file(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Buka File", "", "Text Files (*.txt)")
        if fname:
            try:
                with open(fname, 'r', encoding='utf-8') as file:
                    self.text_edit.setText(file.read())
            except Exception as e:
                QtWidgets.QMessageBox.warning(None, "Error", f"Tidak bisa membuka file:\n{str(e)}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
