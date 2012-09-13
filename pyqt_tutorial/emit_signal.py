#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore


class Emit(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle('emit signal example')
        self.resize(250, 150)
        self.connect(self, QtCore.SIGNAL('closeEmitApp()'), 
                     QtCore.SLOT('close()'))

    def mousePressEvent(self, event):
        self.emit(QtCore.SIGNAL('closeEmitApp()'))


app = QtGui.QApplication(sys.argv)
qb = Emit()
qb.show()
sys.exit(app.exec_())
