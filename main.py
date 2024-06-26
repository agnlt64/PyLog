from logger import Logger, LogLevel

if __name__ == '__main__':
    logger = Logger()
    logger.enable_file_logging()
    logger.log('default log level with logger.log')
    logger.info('info with logger.info')

    logger.set_level(LogLevel.Warning)
    logger.log('this is a warning using logger.set_level')
    logger.warning('this is a warning using logger.warning')

    logger.reset()
    logger.log('this has been reset')

    logger.set_level(LogLevel.Error)
    logger.log('this is an error using logger.set_level')
    
    logger.error('this is an error with logger.error')
    logger.clean_logs() # removes the file logs.txt

    logger.set_level(LogLevel.Info)
    logger.log('hello world') # saved to logs.txt even if it has been deleted
    logger.disable_file_logging()
    logger.log('not saved to a file')
