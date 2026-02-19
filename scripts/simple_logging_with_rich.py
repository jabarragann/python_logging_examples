import logging
from pathlib import Path
from rich.logging import RichHandler
import numpy as np
import time
from pyprojroot.here import here # type: ignore

## Numpy print options
np.set_printoptions(precision=4, suppress=True, sign=" ")

FORMAT = "%(message)s"

logger = logging.getLogger("application")

def setup_logger(filename: Path):
    root_logger = logging.getLogger()

    # File handler
    filename.parent.mkdir(parents=True, exist_ok=True)
    f_format = "%(asctime)s | %(levelname)-8s | %(message)s"
    f_handler = logging.FileHandler(filename, mode="w")
    f_handler.setLevel("INFO")
    f_handler.setFormatter(logging.Formatter(fmt=f_format, datefmt="[%Y-%m-%d %H:%M:%S]"))

    root_logger.addHandler(f_handler)

    # Simple Stream handler
    # s_format = "%(asctime)s | %(levelname)-8s | %(message)s"
    # s_handler = logging.StreamHandler()
    # s_handler.setLevel("DEBUG")
    # s_handler.setFormatter(logging.Formatter(fmt=s_format, datefmt="[%Y-%m-%d %H:%M:%S]"))
    # root_logger.addHandler(s_handler)

    # Rich stream handler
    r_format = "%(asctime)s | %(message)s"
    r_handler = RichHandler(rich_tracebacks=True, show_time=True, show_level=True, show_path=False, omit_repeated_times=False)
    r_handler.setFormatter(logging.Formatter(fmt=r_format, datefmt="[%Y-%m-%d %H:%M:%S]"))
    root_logger.addHandler(r_handler)


if __name__ == "__main__":
    here = here()
    output_log_file = here /"output/sample1.log"
    setup_logger(output_log_file)

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