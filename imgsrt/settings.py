import os
import json


class Settings():

    def __init__(self, appname, default_settings):
        self.appname = appname
        self.home_directory = os.path.expanduser('~')
        self.settings_filename = os.path.join(self.home_directory, f"{self.appname}.txt")
        self.default_settings = default_settings
        self.setup()

    def setup(self):
        if os.path.exists(self.settings_filename):
            self.load_settings()
        else:
            self.create_default_settings()
            self.load_settings()

    def load_settings(self):
        try:
            with open(self.settings_filename, "r") as f:
                data = json.load(f)
            self.settings = data
            print(f"Loaded settings file from {self.settings_filename}")
        except Exception as e:
            print(e)

    def create_default_settings(self):
        try:
            data = json.dumps(self.default_settings, indent=4)
            with open(self.settings_filename, "w") as outfile:
                outfile.write(data)
            print(f"Saved default settings file to {self.settings_filename}")
        except Exception as e:
            print(e)

    def save_settings(self):
        try:
            data = json.dumps(self.settings, indent=4)
            with open(self.settings_filename, "w") as outfile:
                outfile.write(data)
            print(f"Saved settings file to {self.settings_filename}")
        except Exception as e:
            print(e)
