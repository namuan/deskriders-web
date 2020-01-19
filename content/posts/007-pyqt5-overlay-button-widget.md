+++ 
date = 2020-01-02T11:51:10Z
title = "Overlay button on a PyQt5 widget"
description = ""
slug = "" 
tags = ["python", "pyqt5", "tutorial"]
categories = ["tutorial"]
externalLink = ""
series = []
+++

This is a short post on how to add a floating button on top of a widget in PyQt5.

![pyqt5_floating_widget](/images/007/6tpq07fmmwo1rt4gadry.gif)

First, we'll define the button and the relative positioning.

```python
class FloatingButtonWidget(QtWidgets.QPushButton): #1

    def __init__(self, parent):
        super().__init__(parent)
        self.paddingLeft = 5
        self.paddingTop = 5

    def update_position(self): 
        if hasattr(self.parent(), 'viewport'):
            parent_rect = self.parent().viewport().rect()
        else:
            parent_rect = self.parent().rect()

        if not parent_rect:
            return

        x = parent_rect.width() - self.width() - self.paddingLeft
        y = self.paddingTop #3
        self.setGeometry(x, y, self.width(), self.height())

    def resizeEvent(self, event): #2
        super().resizeEvent(event)
        self.update_position()

    def mousePressEvent(self, event): #4
        self.parent().floatingButtonClicked.emit()

```
1. Inheriting from QPushButton.
2. Overriding `resizeEvent` and updating position of the this button based on the parent position.
3. This will add the button to the top. If you need to place it at the button then use something like `parent_rect.height() - self.paddingLeft`.
4. Catching the mouse pressed event and calling an signal on the parent widget.

With the button defined, we'll embed it in a custom `QPlainTextEdit` and define appropriate interfaces for the caller to work with the floating button.

```python
class OverlayedPlainTextEdit(QtWidgets.QPlainTextEdit): #1
    floatingButtonClicked = QtCore.pyqtSignal() #2

    def __init__(self, parent=None):
        super().__init__(parent)
        self.floating_button = FloatingButtonWidget(parent=self)

    def update_floating_button_text(self, txt):
        self.floating_button.setText(txt) #3

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.floating_button.update_position() #4
```

1. Inheriting from QPlainTextEdit although this could be any widget.
2. Defining a custom signal which is triggered when a mouse pressed event is captured in the floating button as we saw earlier.
3. Updating the text of the button which we'll see later.
4. Overriding `resizeEvent` so that we can update the position of the floating button.

Now we can use this class instead of `QPlainTextEdit` and update the floating button.

```python
self.plainTextEdit.floatingButtonClicked.connect(self.on_test)
self.plainTextEdit.update_floating_button_text("Edit")`
```

That is it. Here is the full source code. [Github Gist](https://gist.github.com/namuan/e34387e53e62b52c6aea2146108a92c7)

```python
import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets


class FloatingButtonWidget(QtWidgets.QPushButton):

    def __init__(self, parent):
        super().__init__(parent)
        self.paddingLeft = 5
        self.paddingTop = 5

    def update_position(self):
        if hasattr(self.parent(), 'viewport'):
            parent_rect = self.parent().viewport().rect()
        else:
            parent_rect = self.parent().rect()

        if not parent_rect:
            return

        x = parent_rect.width() - self.width() - self.paddingLeft
        y = self.paddingTop
        self.setGeometry(x, y, self.width(), self.height())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_position()

    def mousePressEvent(self, event):
        self.parent().floatingButtonClicked.emit()


class OverlayedPlainTextEdit(QtWidgets.QPlainTextEdit):
    floatingButtonClicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.floating_button = FloatingButtonWidget(parent=self)

    def update_floating_button_text(self, txt):
        self.floating_button.setText(txt)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.floating_button.update_position()


# NOTE: This class is generated from QtDesigner
class Ui_DebugWindow(object):
    def setupUi(self, DebugWindow):
        DebugWindow.setObjectName("DebugWindow")
        DebugWindow.resize(622, 498)
        self.centralwidget = QtWidgets.QWidget(DebugWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = OverlayedPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        DebugWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DebugWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 22))
        self.menubar.setObjectName("menubar")
        DebugWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DebugWindow)
        self.statusbar.setObjectName("statusbar")
        DebugWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DebugWindow)
        QtCore.QMetaObject.connectSlotsByName(DebugWindow)

    def retranslateUi(self, DebugWindow):
        _translate = QtCore.QCoreApplication.translate
        DebugWindow.setWindowTitle(_translate("DebugWindow", "MainWindow"))


class DebugWindow(QtWidgets.QMainWindow, Ui_DebugWindow):
    edit_mode = True

    def __init__(self, parent=None):
        super(DebugWindow, self).__init__(parent)
        self.setupUi(self)
        # ui events
        self.plainTextEdit.floatingButtonClicked.connect(self.on_test)
        self.update_floating_button_text()

    def on_test(self):
        self.edit_mode = not self.edit_mode
        self.plainTextEdit.appendPlainText("Button Clicked - Mode: {}".format("Edit" if self.edit_mode else "Preview"))
        self.update_floating_button_text()

    def update_floating_button_text(self):
        if self.edit_mode:
            self.plainTextEdit.update_floating_button_text("Edit")
        else:
            self.plainTextEdit.update_floating_button_text("Preview")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = DebugWindow()
    window.show()
    sys.exit(app.exec_())
```