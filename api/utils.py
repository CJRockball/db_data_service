import logging.config
import yaml
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
config_file = ROOT_DIR / 'configs/logging_config.yaml'
