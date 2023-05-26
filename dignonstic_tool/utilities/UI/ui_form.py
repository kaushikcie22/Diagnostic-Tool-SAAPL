# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)
import asset_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(3)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.frame_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.GPIO_TAB = QWidget()
        self.GPIO_TAB.setObjectName(u"GPIO_TAB")
        self.horizontalLayout = QHBoxLayout(self.GPIO_TAB)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.GPIO_TAB)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(5)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_14 = QFrame(self.frame_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.frame_17)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.label_5 = QLabel(self.frame_17)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/new/prefix1/red.png"))

        self.horizontalLayout_6.addWidget(self.label_5)


        self.verticalLayout_12.addWidget(self.frame_17, 0, Qt.AlignLeft)

        self.frame_9 = QFrame(self.frame_14)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame_9)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.pin_set_line_1 = QLineEdit(self.frame_5)
        self.pin_set_line_1.setObjectName(u"pin_set_line_1")

        self.verticalLayout_5.addWidget(self.pin_set_line_1)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.set_low_btn = QPushButton(self.frame_9)
        self.set_low_btn.setObjectName(u"set_low_btn")

        self.horizontalLayout_2.addWidget(self.set_low_btn)

        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.set_high_btn = QPushButton(self.frame_8)
        self.set_high_btn.setObjectName(u"set_high_btn")

        self.verticalLayout_9.addWidget(self.set_high_btn)


        self.horizontalLayout_2.addWidget(self.frame_8)


        self.verticalLayout_12.addWidget(self.frame_9, 0, Qt.AlignLeft)


        self.verticalLayout_8.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.frame_16)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.label_11 = QLabel(self.frame_16)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u":/new/prefix1/red.png"))

        self.horizontalLayout_5.addWidget(self.label_11)


        self.verticalLayout_13.addWidget(self.frame_16, 0, Qt.AlignLeft)

        self.frame_10 = QFrame(self.frame_15)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_6 = QFrame(self.frame_10)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.pin_set_line_2 = QLineEdit(self.frame_6)
        self.pin_set_line_2.setObjectName(u"pin_set_line_2")

        self.verticalLayout_6.addWidget(self.pin_set_line_2)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.contious_tick_box = QCheckBox(self.frame_10)
        self.contious_tick_box.setObjectName(u"contious_tick_box")

        self.horizontalLayout_3.addWidget(self.contious_tick_box)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.read_btn = QPushButton(self.frame_11)
        self.read_btn.setObjectName(u"read_btn")

        self.verticalLayout_10.addWidget(self.read_btn)


        self.horizontalLayout_3.addWidget(self.frame_11)


        self.verticalLayout_13.addWidget(self.frame_10, 0, Qt.AlignLeft)


        self.verticalLayout_8.addWidget(self.frame_15)


        self.horizontalLayout.addWidget(self.frame_4)

        self.tabWidget.addTab(self.GPIO_TAB, "")
        self.cam_test = QWidget()
        self.cam_test.setObjectName(u"cam_test")
        self.verticalLayout_14 = QVBoxLayout(self.cam_test)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_7 = QFrame(self.cam_test)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_7)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_18)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Plain)
        self.verticalLayout_17 = QVBoxLayout(self.frame_19)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.comboBox_3 = QComboBox(self.frame_19)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_17.addWidget(self.comboBox_3, 0, Qt.AlignLeft)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setMinimumSize(QSize(0, 0))
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setFrameShape(QFrame.Box)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_21)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.cam_test_display = QLabel(self.frame_21)
        self.cam_test_display.setObjectName(u"cam_test_display")
        sizePolicy.setHeightForWidth(self.cam_test_display.sizePolicy().hasHeightForWidth())
        self.cam_test_display.setSizePolicy(sizePolicy)

        self.verticalLayout_18.addWidget(self.cam_test_display)


        self.verticalLayout_17.addWidget(self.frame_21)


        self.verticalLayout_16.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.snap_btn = QPushButton(self.frame_20)
        self.snap_btn.setObjectName(u"snap_btn")

        self.horizontalLayout_4.addWidget(self.snap_btn)

        self.video_btn = QPushButton(self.frame_20)
        self.video_btn.setObjectName(u"video_btn")

        self.horizontalLayout_4.addWidget(self.video_btn)

        self.stop_btn = QPushButton(self.frame_20)
        self.stop_btn.setObjectName(u"stop_btn")

        self.horizontalLayout_4.addWidget(self.stop_btn)


        self.verticalLayout_16.addWidget(self.frame_20, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frame_18)


        self.verticalLayout_14.addWidget(self.frame_7)

        self.tabWidget.addTab(self.cam_test, "")
        self.program_test = QWidget()
        self.program_test.setObjectName(u"program_test")
        self.verticalLayout_19 = QVBoxLayout(self.program_test)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_22 = QFrame(self.program_test)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_22)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_26 = QFrame(self.frame_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_25 = QFrame(self.frame_26)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Box)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_25)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.pro_test_normal = QLabel(self.frame_25)
        self.pro_test_normal.setObjectName(u"pro_test_normal")
        sizePolicy.setHeightForWidth(self.pro_test_normal.sizePolicy().hasHeightForWidth())
        self.pro_test_normal.setSizePolicy(sizePolicy)

        self.verticalLayout_23.addWidget(self.pro_test_normal)


        self.horizontalLayout_8.addWidget(self.frame_25)

        self.frame_24 = QFrame(self.frame_26)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Box)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_24)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.prog_test_process_display = QLabel(self.frame_24)
        self.prog_test_process_display.setObjectName(u"prog_test_process_display")
        sizePolicy.setHeightForWidth(self.prog_test_process_display.sizePolicy().hasHeightForWidth())
        self.prog_test_process_display.setSizePolicy(sizePolicy)

        self.verticalLayout_21.addWidget(self.prog_test_process_display)


        self.horizontalLayout_8.addWidget(self.frame_24)


        self.verticalLayout_20.addWidget(self.frame_26)

        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.acquisition_btn = QPushButton(self.frame_23)
        self.acquisition_btn.setObjectName(u"acquisition_btn")

        self.horizontalLayout_7.addWidget(self.acquisition_btn)

        self.stop_acquisition = QPushButton(self.frame_23)
        self.stop_acquisition.setObjectName(u"stop_acquisition")

        self.horizontalLayout_7.addWidget(self.stop_acquisition)


        self.verticalLayout_20.addWidget(self.frame_23, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.frame_22)

        self.tabWidget.addTab(self.program_test, "")
        self.refrence_tab = QWidget()
        self.refrence_tab.setObjectName(u"refrence_tab")
        self.verticalLayout_22 = QVBoxLayout(self.refrence_tab)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_12 = QFrame(self.refrence_tab)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_11.addWidget(self.label_6)

        self.referimage = QLabel(self.frame_13)
        self.referimage.setObjectName(u"referimage")
        sizePolicy.setHeightForWidth(self.referimage.sizePolicy().hasHeightForWidth())
        self.referimage.setSizePolicy(sizePolicy)
        self.referimage.setPixmap(QPixmap(u":/new/prefix1/Downloads/MicrosoftTeams-image.png"))
        self.referimage.setScaledContents(True)
        self.referimage.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.referimage, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_13)


        self.verticalLayout_22.addWidget(self.frame_12)

        self.tabWidget.addTab(self.refrence_tab, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dignostic app", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SAAPL Dignostic Tool", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Output  Control", None))
        self.label_5.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GPIO Pin", None))
        self.set_low_btn.setText(QCoreApplication.translate("MainWindow", u"Set Low", None))
        self.set_high_btn.setText(QCoreApplication.translate("MainWindow", u"Set High", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Input control", None))
        self.label_11.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"GPIO Pin", None))
        self.contious_tick_box.setText(QCoreApplication.translate("MainWindow", u"Continous", None))
        self.read_btn.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GPIO_TAB), QCoreApplication.translate("MainWindow", u"GPIO TEST", None))
        self.cam_test_display.setText("")
        self.snap_btn.setText(QCoreApplication.translate("MainWindow", u"Snap", None))
        self.video_btn.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cam_test), QCoreApplication.translate("MainWindow", u"Camera Test", None))
        self.pro_test_normal.setText("")
        self.prog_test_process_display.setText("")
        self.acquisition_btn.setText(QCoreApplication.translate("MainWindow", u"Acquisition", None))
        self.stop_acquisition.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.program_test), QCoreApplication.translate("MainWindow", u"Program Test", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Refer GPIO Pin", None))
        self.referimage.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.refrence_tab), QCoreApplication.translate("MainWindow", u"BOARD LAYOUT", None))
    # retranslateUi

