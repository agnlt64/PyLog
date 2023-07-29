from logger import Logger, LogLevel

if __name__ == '__main__':
    logger = Logger(log_to_file=True)
    logger.clean_logs()
    logger.log('default log level')
    logger.set_level(LogLevel.Warning)
    logger.log('this is a warning')
    logger.reset()
    logger.log('this has been reset')
    logger.set_level(LogLevel.Error)
    logger.log('this is an error')