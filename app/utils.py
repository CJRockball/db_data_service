import logging.config
import yaml
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
config_file = ROOT_DIR / 'configs/logging_configs.yaml'

with open(config_file, 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    logging.captureWarnings(True)
    
def get_logger(name:str):
    """Logs a message

    Args:
        name (str): name of logger
    """
    logger = logging.getLogger(name)
    return logger