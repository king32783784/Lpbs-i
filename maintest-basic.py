#!/usr/bin/env python
# *-* coding=utf-8 *-*
import sys
from PyQt4 import QtGui, QtCore
from iozoneset import *
from mainset import *

class Mainwindow(QtGui.QWidget):

    def __init__(self):
        super(QtGui.QWidget, self).__init__()
        self.setWindowTitle("Lpb_i")
        self.resize(400, 600)
        palette1 = QtGui.QPalette()
        palette1.setColor(self.backgroundRole(), QColor("#cccddc"))  # 设置背景色
        self.setPalette(palette1)
        self.setAutoFillBackground(True)

        self.gridlayout = QtGui.QGridLayout()   # 创建布局组件
        self.createbutton()
        # 添加设置按钮到布局组件
        self.gridlayout.addWidget(self.button1, 1, 2) 
        self.gridlayout.addWidget(self.button2, 2, 2)
        self.gridlayout.addWidget(self.button3, 3, 2)
        self.gridlayout.addWidget(self.button4, 4, 2)
        self.gridlayout.addWidget(self.button5, 5, 2)
        self.gridlayout.addWidget(self.button6, 6, 2)
        self.gridlayout.addWidget(self.button7, 7, 2)
        self.gridlayout.addWidget(self.button8, 8, 2)
        self.gridlayout.addWidget(self.button9, 9, 2)
        self.gridlayout.addWidget(self.button10, 10, 2)
        

        # 创建测试列表复选框
        self.radio1 = QtGui.QCheckBox("Perf_cpu") 
        self.radio2 = QtGui.QCheckBox("Perf_mem")
        self.radio3 = QtGui.QCheckBox("Perf_io")
        self.radio4 = QtGui.QCheckBox("Perf_thread")
        self.radio5 = QtGui.QCheckBox("Perf_system")
        self.radio6 = QtGui.QCheckBox("Perf_kernel")
        self.radio7 = QtGui.QCheckBox("Perf_stream")
        self.radio8 = QtGui.QCheckBox("Perf_browser")
        self.radio9 = QtGui.QCheckBox("Perf_java")
        self.radio10 = QtGui.QCheckBox("Perf_graphics")
        self.radio1.setChecked(True)    #将Radio1默认选中
       
        # 添加复选框到布局组件
        self.gridlayout.addWidget(self.radio1, 1, 1)  
        self.gridlayout.addWidget(self.radio2, 2, 1)
        self.gridlayout.addWidget(self.radio3, 3, 1)
        self.gridlayout.addWidget(self.radio4, 4, 1)
        self.gridlayout.addWidget(self.radio5, 5, 1)
        self.gridlayout.addWidget(self.radio6, 6, 1)
        self.gridlayout.addWidget(self.radio7, 7, 1)
        self.gridlayout.addWidget(self.radio8, 8, 1)
        self.gridlayout.addWidget(self.radio9, 9, 1)
        self.gridlayout.addWidget(self.radio10, 10, 1)
        
        spacer1 = QtGui.QSpacerItem(20,40)
        self.gridlayout.addItem(spacer1, 11, 1)
        self.allradio = QtGui.QRadioButton(u'全部')  # 创建All选课
        self.allradio.setChecked(False)                  # 将复选框默认未选中
        self.gridlayout.addWidget(self.allradio, 13,1,2,1) # 添加复选框到布局组件
        
   
        self.startbutton = QtGui.QPushButton(u'启动测试') # 创建按钮
        self.gridlayout.addWidget(self.startbutton, 13,2,2,1)# 添加按钮到布局组件
        self.setLayout(self.gridlayout)    # 添加布局组件到窗口
        
        self.createbuttondo()
       # 按钮事件
    def createbuttondo(self):
        self.connect(self.startbutton,   
            QtCore.SIGNAL('clicked()'),
            self.Onstartbutton)
        self.connect(self.button1,
            QtCore.SIGNAL('clicked()'),
            self.Onbutton1)
        self.connect(self.button2,
            QtCore.SIGNAL('clicked()'),
            self.Onbutton2)
        self.connect(self.button3,
            QtCore.SIGNAL('clicked()'),
            self.Onbutton3)
        self.connect(self.button4,
            QtCore.SIGNAL('clicked()'),
            self.Onbutton4)
        self.connect(self.button5,
            QtCore.SIGNAL('clicked()'),
            self.Onbutton5)
        self.connect(self.button6,
            QtCore.SIGNAL('clicked()'),
            self.Onbutton6)
        self.connect(self.button7,
            QtCore.SIGNAL('clicked()'),
            self.Onbutton7)
        self.connect(self.button8,
            QtCore.SIGNAL('clicked()'),
            self.Onbutton8)
        self.connect(self.button9,
            QtCore.SIGNAL('clicked()'),
            self.Onbutton9)
        self.connect(self.button10,
            QtCore.SIGNAL('clicked()'),
            self.Onbutton10)

    # 创建设置按钮
    def createbutton(self):
        self.button1 = QtGui.QPushButton(u'参数设置')
        self.button2 = QtGui.QPushButton(u'参数设置')
        self.button3 = QtGui.QPushButton(u'参数设置')
        self.button4 = QtGui.QPushButton(u'参数设置')
        self.button5 = QtGui.QPushButton(u'参数设置')
        self.button6 = QtGui.QPushButton(u'参数设置')
        self.button7 = QtGui.QPushButton(u'参数设置')
        self.button8 = QtGui.QPushButton(u'参数设置')
        self.button9 = QtGui.QPushButton(u'参数设置')
        self.button10 = QtGui.QPushButton(u'参数设置')


    def Onstartbutton(self):   # 按钮信号槽函数
        if self.allradio.isChecked():
            print("test all start")
        else:
            print("start test")
  
    def Onbutton1(self):
        print("set sysbench")

    def Onbutton2(self):
        print("set sysbench")

    def Onbutton3(self):
      #  win.hide()
        print("set iozone")
        form = Iozoneset()
        form.show()
        form.exec_()

    def Onbutton4(self):
        print("set ")

    def Onbutton5(self):
        print("set")

    def Onbutton6(self):
        print("set")

    def Onbutton7(self):
        print("set")

    def Onbutton8(self):
        print("set")

    def Onbutton9(self):
        print("set")

    def Onbutton10(self):
        print("set")


class Window(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle("Lpb-i")
        self.resize(450,550)

        self.main_widget = Mainwindow()
        self.setCentralWidget(self.main_widget)
        self.setFixedSize(self.width(), self.height()); #　禁用窗口大小调整
  
        self.menubar = self.menuBar() # 获得窗口的菜单条
        self.addmenu()
   
    def addmenu(self):
        self.filemenu = self.menubar.addMenu(u'文件') # 添加文件菜单
        self.filemenuexit = self.filemenu.addAction(u'退出') # 添加退出命令

        self.settingmenu = self.menubar.addMenu(u'&设置')
        self.settingrun = self.settingmenu.addAction(u'运行项目')
        self.settingmenu.addSeparator()  # 添加分隔符
        self.settingbasic = self.settingmenu.addAction(u'基础配置')

        self.testitemmenu = self.menubar.addMenu(u'&测试项')
        self.testiteminfo = self.testitemmenu.addAction(u'测试项说明')

        self.helpmenu = self.menubar.addMenu(u'&帮助')
        self.helpuse = self.helpmenu.addAction(u'&使用说明')
        self.helpabout = self.helpmenu.addAction(u'关于')
        self.creatmenuaction()

    def creatmenuaction(self):
        self.connect(self.filemenuexit, QtCore.SIGNAL('triggered()'), self.Onmenuexit)
        self.connect(self.settingrun, QtCore.SIGNAL('triggered()'), self.Onsettingrun)
        self.connect(self.settingbasic, QtCore.SIGNAL('triggered()'), self.Onsettingbasic)
        self.connect(self.testiteminfo, QtCore.SIGNAL('triggered()'), self.Ontestiteminfo)
        self.connect(self.helpabout, QtCore.SIGNAL('triggered()'), self.Onhelpabout)
        self.connect(self.helpuse, QtCore.SIGNAL('triggered()'), self.Onhelpuse)

    def Onmenuexit(self):
        self.close()

    def Onsettingrun(self):
        print("setting run")

    def Onsettingbasic(self):
        basicset = StackDialog()
        basicset.show()
        basicset.exec_()

    def Ontestiteminfo(self):
        print("testitem info")

    def Onhelpabout(self):
        print("test help")

    def Onhelpuse(self):
        print("test use")

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win =Window()
    win.show()
    app.exec_()
