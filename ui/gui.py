import sys
import os
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog,QFileDialog,QWidget,QFrame,QLineEdit,QMainWindow,QLabel,QPushButton
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt
from ui.functions import main_p1,main_p6,download
fpath=os.path.dirname(__file__)
class App(QMainWindow):
    def __init__(self, folder_p=None, account_p=None, pipeline=None,):
        super().__init__()
        self.folder_p = folder_p
        self.account_p = account_p
        self.subj_info_p = None
        self.pipeline = pipeline
        self.title = 'LINIP Brain Extraction Tool'
        self.left = 10
        self.right = 10
        self.width = 400
        self.height = 600
        self.setFixedSize(self.width, self.height)
        self.setObjectName('main_window')
        stylesheet = ""
        with open(os.path.join(fpath,'design.qss'),'r') as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.initUI()
        
    def initUI(self):
        #-----------------------------main window-----------------------------------#
        # # lab logo
        self.label = QLabel(self)
        self.pixmap = QPixmap(os.path.join(fpath,'logo150.png'))
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.label.move(130,30)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.right, self.width, self.height)
        self.uploader_bubble = QFrame(self)
        self.uploader_bubble.setObjectName("uploader_bubble")
        self.uploader_bubble.move(50,200)
        self.uploader_bubble.mousePressEvent = self.uploader_bubble_clicked
        
        self.uploader_bubble_heading = QLabel(self.uploader_bubble)
        self.uploader_bubble_heading.setObjectName("bubble_heading")
        self.uploader_bubble_heading.setText('Uploader')
        self.uploader_bubble_heading.move(120,8)
        
        self.uploader_bubble_para = QLabel(self.uploader_bubble)
        self.uploader_bubble_para.setObjectName("bubble_para")
        self.uploader_bubble_para.setText('Click here to UPLOAD your structral data!!! :)')
        self.uploader_bubble_para.move(1,50)
        
        self.downloader_bubble = QFrame(self)
        self.downloader_bubble.setObjectName("downloader_bubble")
        self.downloader_bubble.move(50,375)
        self.downloader_bubble.mousePressEvent = self.downloader_bubble_clicked
        
        self.downloader_bubble_heading = QLabel(self.downloader_bubble)
        self.downloader_bubble_heading.setObjectName("bubble_heading")
        self.downloader_bubble_heading.setText('Downloader')
        self.downloader_bubble_heading.move(110,8)
        
        self.downloader_bubble_para = QLabel(self.downloader_bubble)
        self.downloader_bubble_para.setObjectName("bubble_para")
        self.downloader_bubble_para.setText('Click here to DOWNLOAD your structral data!!! :)')
        self.downloader_bubble_para.move(1,50)


        #-----------------------------end main window-----------------------------------#
        
        #-----------------------------uploader bubble expand-----------------------------------#
        self.uploader_bubble_expanded = QFrame(self)
        self.uploader_bubble_expanded.setObjectName("bubble_expanded")
        self.uploader_bubble_expanded.move(10,20)
        self.uploader_bubble_expanded.setVisible(False)
        
        self.back_arrow_up = QLabel(self.uploader_bubble_expanded)
        self.back_arrow_up.move(30,0)
        self.back_arrow_up.setObjectName("back_arrow")
        self.back_arrow_up.setTextFormat(Qt.RichText)
        self.back_arrow_up.setText("&#8592;")
        self.back_arrow_up.mousePressEvent = self.back_arrow_clicked
    
        self.uploader_bubble_heading = QLabel(self.uploader_bubble_expanded)
        self.uploader_bubble_heading.setObjectName("bubble_heading")
        self.uploader_bubble_heading.setText('Volbrain Uploader')
        self.uploader_bubble_heading.move(125,8)

        # Data path
        self.uploader_bubble_para = QLabel(self.uploader_bubble_expanded)
        self.uploader_bubble_para.setObjectName("bubble_para")
        self.uploader_bubble_para.setText('Choose Data Folder:')
        self.uploader_bubble_para.move(1,40)
         
        self.folder_path = QLineEdit(self.uploader_bubble_expanded)
        self.folder_path.setGeometry(QtCore.QRect(20, 74, 300, 31))
        self.folder_path.setObjectName("path_text")
        
        self.browse_button = QPushButton(self.uploader_bubble_expanded)
        self.browse_button.setText('...')
        self.browse_button.setObjectName('browse_button')
        self.browse_button.move(320,74)
        self.browse_button.clicked.connect(self.selectdirpath)


        # account file
        self.uploader_bubble_para = QLabel(self.uploader_bubble_expanded)
        self.uploader_bubble_para.setObjectName("bubble_para")
        self.uploader_bubble_para.setText('Choose Account File:')
        self.uploader_bubble_para.move(1,140)
         
        self.account_path = QLineEdit(self.uploader_bubble_expanded)
        self.account_path.setGeometry(QtCore.QRect(20, 170, 300, 31))
        self.account_path.setObjectName("path_text")
        
        self.browse_button_2 = QPushButton(self.uploader_bubble_expanded)
        self.browse_button_2.setText('...')
        self.browse_button_2.setObjectName('browse_button')
        self.browse_button_2.move(320,174)
        self.browse_button_2.clicked.connect(self.selectfilepath)

        # subject info file
        self.uploader_bubble_para = QLabel(self.uploader_bubble_expanded)
        self.uploader_bubble_para.setObjectName("bubble_para_opt")
        self.uploader_bubble_para.setText('Choose Subject Info File (Optional, just leave it empty):')
        self.uploader_bubble_para.move(1,240)
         
        self.subj_path = QLineEdit(self.uploader_bubble_expanded)
        self.subj_path.setGeometry(QtCore.QRect(20, 270, 300, 31))
        self.subj_path.setObjectName("path_text_opt")
        
        self.browse_button_3 = QPushButton(self.uploader_bubble_expanded)
        self.browse_button_3.setText('...')
        self.browse_button_3.setObjectName('browse_button_opt')
        self.browse_button_3.move(120,270)
        self.browse_button_3.clicked.connect(self.selectfilepath_2)

        # pipeline
        self.groupBox = QtWidgets.QGroupBox(self.uploader_bubble_expanded)
        self.groupBox.setGeometry(QtCore.QRect(20, 330, 340, 61))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("Pipeline:")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.move(5,30)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setText('volBrain 1.0')
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.move(200,30)
        self.radioButton_2.setObjectName("radioButton2")
        self.radioButton_2.setText('vol2Brain 1.0')

        # Button
        self.pushButton = QtWidgets.QPushButton(self.uploader_bubble_expanded)
        self.pushButton.move(160,430)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('Upload!')
        self.pushButton.clicked.connect(self.call_volbrain_uploader)


        #-----------------------------end single bubble expand-----------------------------------#

        #-----------------------------dir bubble expand-----------------------------------#
        self.downloader_bubble_expanded = QFrame(self)
        self.downloader_bubble_expanded.setObjectName("bubble_expanded")
        self.downloader_bubble_expanded.move(10,20)
        self.downloader_bubble_expanded.setVisible(False)
        
        self.back_arrow_d = QLabel(self.downloader_bubble_expanded)
        self.back_arrow_d.move(30,0)
        self.back_arrow_d.setObjectName("back_arrow")
        self.back_arrow_d.setTextFormat(Qt.RichText)
        self.back_arrow_d.setText("&#8592;")
        self.back_arrow_d.mousePressEvent = self.back_arrow_clicked

        # Output path
        self.uploader_bubble_para = QLabel(self.downloader_bubble_expanded)
        self.uploader_bubble_para.setObjectName("bubble_para")
        self.uploader_bubble_para.setText('Choose Data Folder:')
        self.uploader_bubble_para.move(1,40)
        self.uploader_bubble_para2 = QLabel(self.downloader_bubble_expanded)
        self.uploader_bubble_para2.setText('Note that you should use the SAME structural data path as the uploader.')
        self.uploader_bubble_para2.setObjectName("warning")
        self.uploader_bubble_para2.setGeometry(QtCore.QRect(15, 45, 340, 61))

         
        self.outdir_path = QLineEdit(self.downloader_bubble_expanded)
        self.outdir_path.setGeometry(QtCore.QRect(20, 94, 300, 31))
        self.outdir_path.setObjectName("path_text")
        
        self.out_button = QPushButton(self.downloader_bubble_expanded)
        self.out_button.setText('...')
        self.out_button.setObjectName('browse_button')
        self.out_button.move(320,94)
        self.out_button.clicked.connect(self.selectoutpath)

        # account file
        self.downloader_bubble_para = QLabel(self.downloader_bubble_expanded)
        self.downloader_bubble_para.setObjectName("bubble_para")
        self.downloader_bubble_para.setText('Choose Account File:')
        self.downloader_bubble_para.move(1,140)
         
        self.account_path_d = QLineEdit(self.downloader_bubble_expanded)
        self.account_path_d.setGeometry(QtCore.QRect(20, 170, 300, 31))
        self.account_path_d.setObjectName("path_text")
        
        self.browse_button_2_d = QPushButton(self.downloader_bubble_expanded)
        self.browse_button_2_d.setText('...')
        self.browse_button_2_d.setObjectName('browse_button')
        self.browse_button_2_d.move(320,174)
        self.browse_button_2_d.clicked.connect(self.selectfilepath_d)

        # pipeline
        self.groupBox_d = QtWidgets.QGroupBox(self.downloader_bubble_expanded)
        self.groupBox_d.setGeometry(QtCore.QRect(20, 250, 340, 61))
        self.groupBox_d.setObjectName("groupBox")
        self.groupBox_d.setTitle("Pipeline:")
        self.radioButton_d = QtWidgets.QRadioButton(self.groupBox_d)
        self.radioButton_d.move(5,30)
        self.radioButton_d.setObjectName("radioButton")
        self.radioButton_d.setText('MNI')
        self.radioButton_2_d = QtWidgets.QRadioButton(self.groupBox_d)
        self.radioButton_2_d.move(130,30)
        self.radioButton_2_d.setObjectName("radioButton2")
        self.radioButton_2_d.setText('Native')
        self.radioButton_3_d = QtWidgets.QRadioButton(self.groupBox_d)
        self.radioButton_3_d.move(255,30)
        self.radioButton_3_d.setObjectName("radioButton")
        self.radioButton_3_d.setText('ALL')

        # Button
        self.pushButton_d = QtWidgets.QPushButton(self.downloader_bubble_expanded)
        self.pushButton_d.move(150,430)
        self.pushButton_d.setObjectName("pushButton")
        self.pushButton_d.setText('Download!')
        self.pushButton_d.clicked.connect(self.call_downloader)

        #-----------------------------end dir bubble expand-----------------------------------#

    #-----------------------------function-----------------------------------#
    def uploader_bubble_clicked(self,event):
        self.uploader_bubble.setVisible(False)
        self.downloader_bubble.setVisible(False)
        self.uploader_bubble_expanded.setVisible(True)
        self.downloader_bubble_expanded.setVisible(False)

        
    def downloader_bubble_clicked(self,event):
        self.uploader_bubble.setVisible(False)
        self.downloader_bubble.setVisible(False)
        self.uploader_bubble_expanded.setVisible(False)
        self.downloader_bubble_expanded.setVisible(True)

    def back_arrow_clicked(self,event):
        self.uploader_bubble.setVisible(True)
        self.downloader_bubble.setVisible(True)
        self.uploader_bubble_expanded.setVisible(False)
        self.downloader_bubble_expanded.setVisible(False)

    def selectdirpath(self):
        folder = QFileDialog.getExistingDirectory()
        if folder:
            self.folder_path.setText(folder)

    def selectfilepath(self):
        filepath,_ = QFileDialog.getOpenFileName()
        if filepath:
            self.account_path.setText(filepath)
    
    def selectfilepath_2(self):
        infopath,_ = QFileDialog.getOpenFileName()
        if infopath:
            self.subj_path.setText(infopath)

    def call_volbrain_uploader(self):
        if self.subj_path.text():
            self.subj_info_p = self.subj_path.text()
        if self.radioButton.isChecked():
            self.pipeline = 1
            print('Structural Data Folder is:',self.folder_path.text())
            print('Account infomation path is:',self.account_path.text())
            main_p1(self.folder_path.text(),self.account_path.text(),self.subj_info_p)
        elif self.radioButton_2.isChecked():
            self.pipeline = 2
            print('Structural Data Folder is:',self.folder_path.text())
            print('Account infomation path is:',self.account_path.text())
            main_p6(self.folder_path.text(),self.account_path.text(),self.subj_info_p)

    # downloader
    def selectoutpath(self):
        ofolder = QFileDialog.getExistingDirectory()
        if ofolder:
            self.outdir_path.setText(ofolder)
    def selectfilepath_d(self):
        ofilepath,_ = QFileDialog.getOpenFileName()
        if ofilepath:
            self.account_path_d.setText(ofilepath)

            
    def call_downloader(self):
        if self.radioButton_d.isChecked():
            download(self.outdir_path.text(),self.account_path_d.text(),'MNI')
        elif self.radioButton_2_d.isChecked():
            download(self.outdir_path.text(),self.account_path_d.text(),'native')
        elif self.radioButton_3_d.isChecked():
            download(self.outdir_path.text(),self.account_path_d.text(),'all')

if __name__ == "__main__":
    app =  QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())