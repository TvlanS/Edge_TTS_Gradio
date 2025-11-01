import yaml
import pyprojroot
import os

root = pyprojroot.here()

class Config():
    def __init__(self):
        with open(os.path.join(root, "config/config.yaml")) as f:
            config = yaml.safe_load(f)

        self.voices = config["voices"]

    