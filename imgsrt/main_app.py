import sys
import logging
import signal
from PySide6 import QtCore
from main_window import MainWindow


# default logging output
log = logging.getLogger('main')


class MainApp(object):
    """Main application object holding any non-GUI related state."""

    def __init__(self, app_settings):
        self.app_settings = app_settings

        # Attach a handler to the keyboard interrupt (control-C).
        signal.signal(signal.SIGINT, self._sigint_handler)

        # load any available persistent application settings
        QtCore.QCoreApplication.setOrganizationName("Image Sorter")

        QtCore.QCoreApplication.setApplicationName('imgsrt')
        self.settings = QtCore.QSettings()

        # create the interface window
        self.window = MainWindow(self)
        return

    def app_is_exiting(self):
        self.client.disconnect()

    def _sigint_handler(self, signal, frame):
        print("Keyboard interrupt caught, running close handlers...")
        self.app_is_exiting()
        sys.exit(0)


