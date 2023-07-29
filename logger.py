"""
PyLog is a very simple logger written in Python.

Copyright © Antonin GENELOT, 30/07/2023
"""

from enum import Enum
from datetime import datetime
import os
import re


class LogLevel(Enum):
    Info = 0,
    Warning = 1,
    Error = 2

class Logger:
    def __init__(self, log_level: LogLevel = LogLevel.Info, log_to_file: bool = False) -> None:
        self.log_level = log_level
        self.log_to_file = log_to_file
        
        self.date = datetime.now()
        self.filename = 'logs.txt'
        self.RESET = '\033[0m'
        self.RED = "\033[0;31m"
        self.BLUE = "\033[0;36m"
        self.YELLOW = "\033[1;33m"
        self.BOLD = "\033[1m"


    #######################
    # Private methods
    ######################

    def _log_level_to_string(self) -> str:
        """
        Returns the stringified version of the current log level.
        """
        match self.log_level:
            case LogLevel.Info:
                return 'info'
            case LogLevel.Warning:
                return 'warning'
            case LogLevel.Error:
                return 'error'
        return 'info'

    def _format_date(self) -> str:
        """
        Returns
        """
        day = str(self.date.day)
        month = str(self.date.month)
        if int(day) < 10:
            day = '0' + day
        if int(month) < 10:
            month = '0' + month
        return f'{day}/{month}/{self.date.year}'
    
    def _strip_format(self, input_string: str) -> str:
        """
        Removes all the ANSI escape codes from the given string.
        """
        escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return escape.sub('', input_string)

    def _format(self, color: str) -> str:
        """
        Default string format for the logger.
        """
        return f"{self.RESET}{self.BOLD}{color}[{self._log_level_to_string().upper()}]{self.RESET}{color}"

    def _log_to_file(self, format: str) -> None:
        with open(self.filename, 'a+') as logs:
            logs.write(self._strip_format(format) + '\n')


    ##########################
    # Public methods
    #########################

    def reset(self) -> None:
        """
        Resets the log level to LogLevel.Info.
        """
        self.log_level = LogLevel.Info

    def log(self, message: str):
        """
        Logs a message with the current log level.
        """
        date = f'[{self._format_date()}]'
        match self.log_level:
            case LogLevel.Info:
                formatted_message = f'{self._format(self.BLUE)} {message} {date}'
                if self.log_to_file:
                    self._log_to_file(formatted_message)
                print(formatted_message)
            case LogLevel.Warning:
                formatted_message = f'{self._format(self.YELLOW)} {message} {date}'
                if self.log_to_file:
                    self._log_to_file(formatted_message)
                print(formatted_message)
            case LogLevel.Error:
                formatted_message = f'{self._format(self.RED)} {message} {date}'
                if self.log_to_file:
                    self._log_to_file(formatted_message)
                print(formatted_message)
            case _:
                pass
    
    def set_level(self, log_level: LogLevel) -> None | ValueError:
        """
        Sets the current log level. An ValueError is raised if the log level provided is incorrect.
        """
        print(self.RESET)
        if log_level not in [LogLevel.Info, LogLevel.Warning, LogLevel.Error]:
            raise ValueError('log_level must be LogLevel.{Info, Warning, Error}')
        self.log_level = log_level

    def enable_file_logging(self) -> None:
        """
        Enables logging to a file.
        """
        self.log_to_file = True
        
    def disable_file_logging(self) -> None:
        """
        Disables logging to a file.
        """
        self.log_to_file = False

    def clean_logs(self) -> None:
        """
        Removes the file `logs.txt` if it existed.
        """
        if os.path.exists(self.filename):
            os.remove(self.filename)
