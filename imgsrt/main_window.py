from __future__ import print_function
import logging
import queue
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QMainWindow,
    QVBoxLayout,
)

# default logging output
log = logging.getLogger('main')


class MainWindow(QMainWindow):
    """A custom main window which provides all GUI controls.
    Requires a delegate main application object to handle user requests."""

    def __init__(self, main, *args, **kwargs):
        super(MainWindow, self).__init__()

        # save the main object for delegating GUI events
        self.main = main

        # create the GUI elements
        self.console_queue = queue.Queue()
        self.setupUi()

        self._handler = None
        self.enable_console_logging()

        # finish initialization
        self.show()

        return

    def setupUi(self):

        self.setWindowTitle("Image Sorter")

        self.resize(600, 600)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.horizontalLayout = QHBoxLayout()
        self.centralwidget.setLayout(self.horizontalLayout)

        self.leftWidget = QWidget(self)
        self.leftVerticalLayout = QVBoxLayout()
        self.leftVerticalLayout.setContentsMargins(-1, -1, -1, 9)  # left, top, right, bottom
        self.leftWidget.setLayout(self.leftVerticalLayout)

        self.rightWidget = QWidget(self)
        self.rightHorizontalLayout = QHBoxLayout()
        self.rightWidget.setLayout(self.rightHorizontalLayout)

        return

    def write(self, string):
        """Write output to the console text area in a thread-safe way.  Qt only allows
        calls from the main thread, but the service routines run on separate threads."""
        self.console_queue.put(string)
        return

    def enable_console_logging(self):
        # get the root logger to receive all logging traffic
        logger = logging.getLogger()
        # create a logging handler which writes to the console window via self.write
        handler = logging.StreamHandler(self)
        handler.setFormatter(logging.Formatter('%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)
        # logger.setLevel(logging.NOTSET)
        logger.setLevel(logging.DEBUG)
        handler.setLevel(logging.NOTSET)
        self._handler = handler
        log.info("Enabled logging in console window.")
        return

    def disable_console_logging(self):
        if self._handler is not None:
            logging.getLogger().removeHandler(self._handler)
            self._handler = None
