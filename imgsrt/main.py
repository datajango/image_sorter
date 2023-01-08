import sys
import logging
from PySide6.QtWidgets import (
    QApplication,
)

from main_app import MainApp
from settings import Settings
from default_settings import default_app_settings

# default logging output
log = logging.getLogger('main')


def main():

    app_settings = Settings("imgsrt", default_app_settings)

    # Optionally add an additional root log handler to stream messages to the console.
    if False:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(logging.Formatter('%(levelname)s:%(name)s: %(message)s'))
        logging.getLogger().addHandler(console_handler)

    # initialize the Qt system itself
    app = QApplication(sys.argv)

    # create the main application controller
    MainApp(app_settings)

    # run the event loop until the user is done
    log.info("Starting event loop.")
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
