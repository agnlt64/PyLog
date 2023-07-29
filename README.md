# PyLog, a simple logger in Python

## Installation
You do not need to install PyLog, you can just copy and paste the `logger.py` file into your project and it will work. See `main.py` for more datails.

## Methods
`__init__(log_to_file)`: `log_to_file` is a boolean parameter indicating that the printed logs will be saved in a file called `logs.txt`.  
`reset()`: reset the log level to `LogLevel.Info`, which is the default.  
`log(message: str)`: print the `message` to the console using the `Logger._format()` format.  
`set_level(log_level: LogLevel)`: set the logger log level to `log_level`. Raise a `ValueError` if the `log_level` is incorrect.  
`enable_file_logging()`: enable file logging if it was not already enabled.  
`disable_file_logging()`: disable file logging if it was not already disabled.  
__NOTE THAT `enable_file_logging` and `disable_file_logging` can be called anywhere in the program and you can therefore have logs saved to a file and logs only printed to the console.__  
`clean_logs()`: remove the `logs.txt` file if it exists.  

Internal methods are not documented here because you should not call them directly, but you can look at the code to understand what they do.

## Usage
```py
from logger import Logger, LogLevel

logger = Logger(log_to_file=True)
logger.log('default logging level') # this will be printed in blue and saved to a file
logger.disable_file_logging()
logger.log('not saved') # this will only be printed but not saved
logger.enable_file_logging()
logger.set_level(LogLevel.Warning)
logger.log('warning') # this will be saved to a file and be printed in yellow
logger.set_level(LogLevel.Error)
logger.log('error') # this will be saved to a file and br printed in red
logger.clean_logs() # this line removes the logs.txt file
```