import config as cfg
import os
from src.Field import Field

os.chdir(cfg.config["working-directory"])

if __name__ == "__main__":
    field = Field()

