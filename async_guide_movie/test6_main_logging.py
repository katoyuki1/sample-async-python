from test6_logging_ad import CustomLogger

def main():
  logger = CustomLogger(__name__).get_logger()
  logger.info("This is an INFO message")
  logger.debug("This is an DEBUG message")
  logger.error("This is an ERROR message")

if __name__ == '__main__':
  main()