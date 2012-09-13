#!/usr/bin/env python

import sys
from PyQt4 import QtGui

class Absolute(QtGui.QWidget):

    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)

        label = QtGui.QLabel('Yo', self)
        label.move(15, 10)

        label = QtGui.QLabel('Hello', self)
        label.move(115, 10)

        label = QtGui.QLabel('Hi', self)
        label.move(145, 40)

        self.resize(250, 150)

app = QtGui.QApplication(sys.argv)
qb  = Absolute()
qb.show()
sys.exit(app.exec_())
