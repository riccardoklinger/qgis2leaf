# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_qgis2leaf.ui'
#
# Created: Mon Jun  9 13:10:50 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_qgis2leaf(object):
    def setupUi(self, qgis2leaf):
        qgis2leaf.setObjectName(_fromUtf8("qgis2leaf"))
        qgis2leaf.resize(480, 547)
        self.label = QtGui.QLabel(qgis2leaf)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(qgis2leaf)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 461, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_3 = QtGui.QFrame(qgis2leaf)
        self.line_3.setGeometry(QtCore.QRect(10, 50, 461, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.tab_2 = QtGui.QTabWidget(qgis2leaf)
        self.tab_2.setGeometry(QtCore.QRect(10, 60, 461, 481))
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tab_app = QtGui.QWidget()
        self.tab_app.setObjectName(_fromUtf8("tab_app"))
        self.listWidget = QtGui.QListWidget(self.tab_app)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 341, 151))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_app)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 190, 443, 250))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radioButton = QtGui.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout.addWidget(self.radioButton, 1, 2, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.width_box = QtGui.QLineEdit(self.gridLayoutWidget)
        self.width_box.setObjectName(_fromUtf8("width_box"))
        self.horizontalLayout_2.addWidget(self.width_box)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.height_box = QtGui.QLineEdit(self.gridLayoutWidget)
        self.height_box.setObjectName(_fromUtf8("height_box"))
        self.horizontalLayout_2.addWidget(self.height_box)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.gridLayout.addWidget(self.comboBox_3, 3, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.cancelButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_4.addWidget(self.cancelButton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 7, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 6, 1, 1, 1)
        self.okButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.gridLayout.addWidget(self.okButton, 7, 2, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 6, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans"))
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 5, 1, 1, 1)
        self.line_2 = QtGui.QFrame(self.tab_app)
        self.line_2.setGeometry(QtCore.QRect(10, 170, 441, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.getSizeButton = QtGui.QPushButton(self.tab_app)
        self.getSizeButton.setGeometry(QtCore.QRect(360, 90, 81, 31))
        self.getSizeButton.setObjectName(_fromUtf8("getSizeButton"))
        self.getButton = QtGui.QPushButton(self.tab_app)
        self.getButton.setGeometry(QtCore.QRect(360, 130, 81, 31))
        self.getButton.setObjectName(_fromUtf8("getButton"))
        self.tab_2.addTab(self.tab_app, _fromUtf8(""))
        self.tab_help = QtGui.QWidget()
        self.tab_help.setObjectName(_fromUtf8("tab_help"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_help)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 441, 431))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tab_2.addTab(self.tab_help, _fromUtf8(""))
        self.actionLoadList = QtGui.QAction(qgis2leaf)
        self.actionLoadList.setObjectName(_fromUtf8("actionLoadList"))

        self.retranslateUi(qgis2leaf)
        self.tab_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(qgis2leaf)

    def retranslateUi(self, qgis2leaf):
        qgis2leaf.setWindowTitle(QtGui.QApplication.translate("qgis2leaf", "qgis2leaf", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("qgis2leaf", "QGIS 2 Leaflet", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("qgis2leaf", "Export your vector and raster to a leaflet based webmap", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("qgis2leaf", "Full Screen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("qgis2leaf", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("qgis2leaf", "Visible layers:", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("qgis2leaf", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("qgis2leaf", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("qgis2leaf", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("qgis2leaf", "Output project folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("qgis2leaf", "Basemap:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("qgis2leaf", "Extent:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("qgis2leaf", "Frame width / height:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("qgis2leaf", "Opacity control:", None, QtGui.QApplication.UnicodeUTF8))
        self.getSizeButton.setText(QtGui.QApplication.translate("qgis2leaf", "Get Map Size", None, QtGui.QApplication.UnicodeUTF8))
        self.getButton.setText(QtGui.QApplication.translate("qgis2leaf", "Get Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_2.setTabText(self.tab_2.indexOf(self.tab_app), QtGui.QApplication.translate("qgis2leaf", "qgis2leaf", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("qgis2leaf", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:9pt; font-weight:600; text-decoration: underline;\">General help:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:9pt;\">QGIS 2 Leaflet creates a webmap from your current QGIS vector features and rasters. Therefore it tries to copy the current vector styles to styles, leaflet will understand. If your data has an attribute called </span><span style=\" font-family:\'Sans\'; font-size:9pt; font-weight:600; font-style:italic;\">html_exp</span><span style=\" font-family:\'Sans\'; font-size:9pt; font-weight:600;\"> </span><span style=\" font-family:\'Sans\'; font-size:9pt;\">it will use this for the</span><span style=\" font-family:\'Sans\'; font-size:9pt; font-weight:600;\"> popup content. </span><span style=\" font-family:\'Sans\'; font-size:9pt;\">Otherwise it will create a </span><span style=\" font-family:\'Sans\'; font-size:9pt; font-weight:600;\">simple table</span><span style=\" font-family:\'Sans\'; font-size:9pt;\"> from all of your attributes and values. Furthermore you can define an </span><span style=\" font-family:\'Sans\'; font-size:9pt; font-weight:600;\">icon for your point</span><span style=\" font-family:\'Sans\'; font-size:9pt;\"> layers using an attribute called </span><span style=\" font-family:\'Sans\'; font-size:9pt; font-weight:600; font-style:italic;\">icon_exp</span><span style=\" font-family:\'Sans\'; font-size:9pt; font-weight:600;\">.</span><span style=\" font-family:\'Sans\'; font-size:9pt;\"> Each feature should have an </span><span style=\" font-family:\'Sans\'; font-size:9pt; font-weight:600;\">absolute path</span><span style=\" font-family:\'Sans\'; font-size:9pt;\"> on your current system or provide a </span><span style=\" font-family:\'Sans\'; font-size:9pt; font-weight:600;\">link to the image</span><span style=\" font-family:\'Sans\'; font-size:9pt;\"> (preferable *.svg or *.png). You may find suitable examples in the test_data folder.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:9pt;\">Raster images will be tranlated to EPSG:4326/jpg using GDAL. Make sure you\'ve installed GDAL.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:9pt; font-weight:600; text-decoration: underline;\">GUI help:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Sans\'; font-size:9pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press &quot;<span style=\" font-weight:600;\">get layers</span>&quot; to add/reload your vector layers to the plugin. You can select the layers to export.</li>\n"
"<li style=\" font-family:\'Sans\'; font-size:9pt;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Frame width</span> defines the map dimension in the html page. Toggle between given pixel values or full screen which corresponds to 100% width of your browser.</li>\n"
"<li style=\" font-family:\'Sans\'; font-size:9pt;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Extent: <span style=\" font-weight:600;\">canvas extent - </span>QGIS canvas will influence initial leaflet view / choose <span style=\" font-weight:600;\">layer extent</span> to set the leaflet webmap extent to the extent of all vector layers.</li>\n"
"<li style=\" font-family:\'Sans\'; font-size:9pt;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For large datasets set the <span style=\" font-weight:600;\">visible layers</span> to &quot;show none&quot;. Visibility can be toggled in the webmap afterwards as you have a nice layer switcher.</li>\n"
"<li style=\" font-family:\'Sans\'; font-size:9pt;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose one of the available <span style=\" font-weight:600;\">basemaps</span>. </li>\n"
"<li style=\" font-family:\'Sans\'; font-size:9pt;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Opacity of raster images in your map can be changed using the <span style=\" font-weight:600;\">Opacity control</span> which is a slider below your map.</li>\n"
"<li style=\" font-family:\'Sans\'; font-size:9pt;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">As <span style=\" font-weight:600;\">output project folder</span> you should choose a separate folder. There will be a designated folder in it with your current export files and folders.</li></ul></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_2.setTabText(self.tab_2.indexOf(self.tab_help), QtGui.QApplication.translate("qgis2leaf", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoadList.setText(QtGui.QApplication.translate("qgis2leaf", "loadList", None, QtGui.QApplication.UnicodeUTF8))

