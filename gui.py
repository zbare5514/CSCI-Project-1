# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_television_window(object):
    def setupUi(self, television_window):
        television_window.setObjectName("television_window")
        television_window.setEnabled(True)
        television_window.resize(1124, 715)
        television_window.setMinimumSize(QtCore.QSize(1124, 715))
        television_window.setMaximumSize(QtCore.QSize(1124, 715))
        font = QtGui.QFont()
        font.setPointSize(11)
        television_window.setFont(font)
        television_window.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=television_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label_television_display = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_television_display.setGeometry(QtCore.QRect(220, 10, 681, 441))
        self.label_television_display.setText("")
        self.label_television_display.setPixmap(QtGui.QPixmap("gui images/power_off.jpg"))
        self.label_television_display.setObjectName("label_television_display")
        self.button_channel_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_up.setGeometry(QtCore.QRect(50, 420, 121, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setKerning(True)
        self.button_channel_up.setFont(font)
        self.button_channel_up.setAutoFillBackground(False)
        self.button_channel_up.setIconSize(QtCore.QSize(30, 30))
        self.button_channel_up.setObjectName("button_channel_up")
        self.button_channel_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_channel_down.setGeometry(QtCore.QRect(50, 540, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.button_channel_down.setFont(font)
        self.button_channel_down.setIconSize(QtCore.QSize(30, 30))
        self.button_channel_down.setObjectName("button_channel_down")
        self.button_volume_down = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_volume_down.setGeometry(QtCore.QRect(960, 540, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.button_volume_down.setFont(font)
        self.button_volume_down.setObjectName("button_volume_down")
        self.button_volume_up = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_volume_up.setEnabled(True)
        self.button_volume_up.setGeometry(QtCore.QRect(960, 420, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.button_volume_up.setFont(font)
        self.button_volume_up.setObjectName("button_volume_up")
        self.button_power = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_power.setGeometry(QtCore.QRect(460, 500, 221, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_power.setFont(font)
        self.button_power.setObjectName("button_power")
        self.button_mute = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_mute.setGeometry(QtCore.QRect(880, 500, 61, 61))
        self.button_mute.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui images/mute.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_mute.setIcon(icon)
        self.button_mute.setIconSize(QtCore.QSize(56, 56))
        self.button_mute.setObjectName("button_mute")
        self.slider_channel = QtWidgets.QSlider(parent=self.centralwidget)
        self.slider_channel.setEnabled(True)
        self.slider_channel.setGeometry(QtCore.QRect(80, 80, 51, 271))
        self.slider_channel.setMaximum(3)
        self.slider_channel.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.slider_channel.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.slider_channel.setObjectName("slider_channel")
        self.slider_volume = QtWidgets.QSlider(parent=self.centralwidget)
        self.slider_volume.setEnabled(True)
        self.slider_volume.setGeometry(QtCore.QRect(1000, 80, 51, 271))
        self.slider_volume.setMaximum(2)
        self.slider_volume.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.slider_volume.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.slider_volume.setObjectName("slider_volume")
        television_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=television_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 26))
        self.menubar.setObjectName("menubar")
        television_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=television_window)
        self.statusbar.setObjectName("statusbar")
        television_window.setStatusBar(self.statusbar)

        self.retranslateUi(television_window)
        QtCore.QMetaObject.connectSlotsByName(television_window)

    def retranslateUi(self, television_window):
        _translate = QtCore.QCoreApplication.translate
        television_window.setWindowTitle(_translate("television_window", "MainWindow"))
        self.button_channel_up.setText(_translate("television_window", "Channel Up"))
        self.button_channel_down.setText(_translate("television_window", "Channel Down"))
        self.button_volume_down.setText(_translate("television_window", "Volume Down"))
        self.button_volume_up.setText(_translate("television_window", "Volume Up"))
        self.button_power.setText(_translate("television_window", "Power"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    television_window = QtWidgets.QMainWindow()
    ui = Ui_television_window()
    ui.setupUi(television_window)
    television_window.show()
    sys.exit(app.exec())
