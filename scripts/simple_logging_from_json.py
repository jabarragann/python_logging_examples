import json
import logging.config
from pathlib import Path
import time
from pyprojroot.here import here # type: ignore
import numpy as np

## Numpy print options
np.set_printoptions(precision=4, suppress=True, sign=" ")
## Global logger
logger = logging.getLogger("application")


def setup_logging_from_json(config_file: Path, log_output_file: Path):

    log_output_file.parent.mkdir(parents=True, exist_ok=True)
    logger_config_dict = json.load(open(config_file))
    logger_config_dict["handlers"]["file_handler"]["filename"] = str(log_output_file)
    logging.config.dictConfig(logger_config_dict)


if __name__ == "__main__":
    root = here()
    
    log_output_file = root /"output/sample2.log"
    log_config_file = root /"configs/config1.json"
    setup_logging_from_json(log_config_file, log_output_file)

    ## Demo

    logger.setLevel("DEBUG")
    logger.info("Starting stereo calibration refinement...Long message to test the formatting of the Rich handler.")
    logger.debug("Debug message")
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
    a = np.array([1, 2, 3])
    b = np.array([[1.03, 2.03, 3.03], [4.03, 5.03, 6.03], [7.03, 8.03, 9.03453]])
    logger.info(f"a_matrix \n{a}\n")
    logger.info(f"b_matrix \n{b}\n")

    time.sleep(1)
    logger.info("Done")