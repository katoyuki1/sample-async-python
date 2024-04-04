import logging


class CustomLogger:
  def __init__(self, name):
    log_level = logging.INFO
    log_format = "%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s"
    self.logger = logging.getLogger(name)
    self.logger.setLevel(log_level)
    formatter = logging.Formatter(log_format)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    self.logger.addHandler(console_handler)

  def get_logger(self):
    return self.logger