#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore


class SigSlot(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('Signal and Slot example')

        lcd    = QtGui.QLCDNumber(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'), lcd,
                     QtCore.SLOT('display(int)'))

        self.resize(250, 150)

app = QtGui.QApplication(sys.argv)
qb = SigSlot()
qb.show()
sys.exit(app.exec_())
