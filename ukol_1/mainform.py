# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from draw import Draw
from algorithms import *

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Canvas.sizePolicy().hasHeightForWidth())
        self.Canvas.setSizePolicy(sizePolicy)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDraw = QtWidgets.QMenu(parent=self.menubar)
        self.menuDraw.setObjectName("menuDraw")
        self.menuAnalyze = QtWidgets.QMenu(parent=self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)
        self.toolBar_2 = QtWidgets.QToolBar(parent=MainForm)
        self.toolBar_2.setObjectName("toolBar_2")
        MainForm.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar_2)
        self.actionOpen = QtGui.QAction(parent=MainForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(parent=MainForm)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionPoint_Polygon = QtGui.QAction(parent=MainForm)
        self.actionPoint_Polygon.setCheckable(True)
        self.actionPoint_Polygon.setChecked(True)
        self.actionPoint_Polygon.setObjectName("actionPoint_Polygon")
        self.actionClear = QtGui.QAction(parent=MainForm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear.setIcon(icon2)
        self.actionClear.setObjectName("actionClear")
        self.actionPoint_Polygon_2 = QtGui.QAction(parent=MainForm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/polygon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPoint_Polygon_2.setIcon(icon3)
        self.actionPoint_Polygon_2.setObjectName("actionPoint_Polygon_2")
        self.actionRay_Algorithm = QtGui.QAction(parent=MainForm)
        self.actionRay_Algorithm.setCheckable(True)
        self.actionRay_Algorithm.setObjectName("actionRay_Algorithm")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuDraw.addAction(self.actionPoint_Polygon)
        self.menuDraw.addAction(self.actionClear)
        self.menuAnalyze.addAction(self.actionPoint_Polygon_2)
        self.menuAnalyze.addAction(self.actionRay_Algorithm)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDraw.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.toolBar_2.addAction(self.actionOpen)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionPoint_Polygon_2)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionClear)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionExit)

        # Connect menu item in QT and function
        self.actionPoint_Polygon.triggered.connect(self.switchSourceClick)
        self.actionPoint_Polygon_2.triggered.connect(self.analyzeClick)
        # Point_Polygon_2 mean Point and polygon POSITION

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)
        # Hugo radek
        self.actionOpen.triggered.connect(self.input)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Point and polygon position"))
        self.menuFile.setTitle(_translate("MainForm", "File"))
        self.menuDraw.setTitle(_translate("MainForm", "Draw"))
        self.menuAnalyze.setTitle(_translate("MainForm", "Analyze"))
        self.toolBar_2.setWindowTitle(_translate("MainForm", "toolBar_2"))
        self.actionOpen.setText(_translate("MainForm", "Open"))
        self.actionExit.setText(_translate("MainForm", "Exit"))
        self.actionPoint_Polygon.setText(_translate("MainForm", "Point/Polygon"))
        self.actionClear.setText(_translate("MainForm", "Clear"))
        self.actionPoint_Polygon_2.setText(_translate("MainForm", "Point and Polygon position"))
        self.actionPoint_Polygon_2.setShortcut(_translate("MainForm", "Ctrl+P"))
        self.actionRay_Algorithm.setText(_translate("MainForm", "Ray Algorithm"))

    #Hugo time
    def input(self):
        # Store Canvas parameters for later rescale
        width = self.Canvas.frameGeometry().width()
        height = self.Canvas.frameGeometry().height()

        # Call setPath with specific Canvas parameters
        self.Canvas.setPath(width, height)
    # Hugo konec

    #Change source
    def switchSourceClick(self):
        self.Canvas.switchsource()


    def analyzeClick(self):
        #Analyze point and position

        #Get point and polygon
        q = self.Canvas.getPoint()
        pol = self.Canvas.getPolygon()
        self.Canvas.clearResPol()

        #Analyze position
        a = Algorithms()
        info = 0

        for polygons in pol:

            if self.actionRay_Algorithm.isChecked():
                res = a.getRayCrossing(q, polygons)
                if res == 1:
                    # If point is inside polygon
                    self.Canvas.getResPol(polygons)
                    print("Ray Crossing aktivován")
                    info = 1
                    
            else:
                res = a.getWindingNumber(q,polygons)
                if res == 1:
                    #If point is inside polygon
                    self.Canvas.getResPol(polygons)
                    info = 1

        self.Canvas.repaint()

        #Print results
        dialog = QtWidgets.QMessageBox()
        dialog.setWindowTitle("Results of analysis")
        if info == 1:
            dialog.setText("Inside")
        else:
            dialog.setText("Outside")
        dialog.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec())
