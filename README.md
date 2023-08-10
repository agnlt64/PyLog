# PyLog, a simple logger in Python

## Installation
You do not need to install PyLog, you can just copy and paste the `logger.py` file into your project and it will work. See `main.py` for more datails.

## Methods
`__init__(log_to_file)`: `log_to_file` is a boolean parameter indicating that the printed logs will be saved in a file called `logs.txt`.  
`reset()`: reset the log level to `LogLevel.Info`, which is the default.  
`log(format: str)`: call the appropriate method (aka `self.info()`, `self.warning()`, or `self.error()`) following the value of `self.log_level`. 
`info(format: str)`: print the `format` in blue using `self.__get_format()` as a default formatter.  
`warning(format: str)`: print the `format` in yellow using `self.__get_format()` as a default formatter.  
`error(format: str)`: print the `format` in red using `self.__get_format()` as a default formatter.  
`set_level(log_level: LogLevel)`: set the logger log level to `log_level`. Raises a `ValueError` if the `log_level` is incorrect.  
`log_assert(condition: bool, message='')`: custom assert method. Raises an `AssertionError` if the `condition` is `False` and prints the `message` in bold red.  
`enable_file_logging()`: enable file logging if it was not already enabled.  
`disable_file_logging()`: disable file logging if it was not already disabled.  
__NOTE THAT `enable_file_logging` and `disable_file_logging` can be called anywhere in the program and you can therefore have logs saved to a file and logs only printed to the console.__  
`clean_logs()`: remove the `logs.txt` file if it exists.  

Internal methods are not documented here because you should not call them directly, but you can look at the code to understand what they do.

## Usage
```py
# see main.py
from logger import Logger, LogLevel

logger = Logger()
logger.enable_file_logging() # you can also enable file logging via the constructor
logger.log('default log level with logger.log') # blue
logger.info('info with logger.info') # blue

logger.set_level(LogLevel.Warning)
logger.log('this is a warning using logger.set_level') # yellow
logger.warning('this is a warning using logger.warning') # the current log level does not matter, yellow anyway

logger.reset() # self.log_level = LogLevel.Info
logger.log('this has been reset') # blue
logger.set_level(LogLevel.Error)
logger.log('this is an error using logger.set_level') # red

logger.error('this is an error with logger.error') # red anyway
logger.clean_logs() # removes the file logs.txt

logger.set_level(LogLevel.Info)
logger.log('hello world') # saved to logs.txt even if the file has been deleted
logger.disable_file_logging() # the next message will not be saved to logs.txt unless you call enable_file_logging()
logger.log('not saved to a file') # blue because the las call to set_level set logger.log_level to LogLevel.Info
```