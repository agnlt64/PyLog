"""
The MIT License (MIT)

Copyright (c) 2023 Antonin GENELOT.                                       

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
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

        self._log_to_file = log_to_file
        self._date = datetime.now()
        self._filename = 'logs.txt'
        self.RESET  = '\033[0m'
        self.RED    = '\033[0;31m'
        self.BLUE   = '\033[0;36m'
        self.YELLOW = '\033[0;33m'
        self.BOLD   = '\033[1m'


    #######################
    # Private methods
    ######################

    def __log_level_to_string(self, log_level: LogLevel=None) -> str:
        """
        Returns the stringified version of the log level parameter if it is not None,
        else returns the stringified versoin of the current log level.
        """
        if log_level is None: level = self.log_level
        else: level = log_level
        match level:
            case LogLevel.Info:
                return 'info'
            case LogLevel.Warning:
                return 'warning'
            case LogLevel.Error:
                return 'error'
        return 'info'


    def __global_time_format(self, time: str) -> str:
        if int(time) < 10:
            time = '0' + time
        return time

    def __format_date(self) -> str:
        """
        Returns the date using `dd/mm/yyyy` format.
        """
        day = self.__global_time_format(str(self._date.day))
        month = self.__global_time_format(str(self._date.month))
        return f'{day}/{month}/{self._date.year}'
    

    def __format_hour(self) -> str:
        """
        Returns the current hour using `hour:minute:second`.
        """
        hour = self.__global_time_format(str(self._date.hour))
        minute = self.__global_time_format(str(self._date.minute))
        second = self.__global_time_format(str(self._date.second))
        return f'{hour}:{minute}:{second}'


    def __strip_format(self, input_string: str) -> str:
        """
        Removes all the ANSI escape codes from the given string.
        """
        escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return escape.sub('', input_string)


    def __get_format(self, color: str, log_level: LogLevel) -> str:
        """
        Default string format for the logger, aka `(bold + color)[date at hour] severity:(no bold + color)`.
        """
        return f'{color}{self.BOLD}[{self.__format_date()} at {self.__format_hour()}] {self.__log_level_to_string(log_level).upper()}:{self.RESET}{color}'


    def __write_to_file(self, format: str) -> None:
        """
        Writes the `format` to a file called `logs.txt` and removes the ANSI escapes code from the format.
        """
        with open(self._filename, 'a+') as logs:
            logs.write(self.__strip_format(format) + '\n')


    ##########################
    # Public methods
    #########################

    def reset(self) -> None:
        """
        Resets the log level to LogLevel.Info.
        """
        self.log_level = LogLevel.Info


    def log(self, format: str):
        """
        Logs a message with the current log level.
        """
        match self.log_level:
            case LogLevel.Info:
                self.info(format)
            case LogLevel.Warning:
                self.warning(format)
            case LogLevel.Error:
                self.error(format)
            case other:
                pass


    def info(self, format: str) -> None:
        """
        Logs the message in blue using `self.__get_format()`.
        """
        if self._log_to_file:
            self.__write_to_file(format)
        print(f'{self.__get_format(self.BLUE, LogLevel.Info)} {format}')
        print(self.RESET)


    def warning(self, format: str) -> None:
        """
        Logs the message in yellow using `self.__get_format()`.
        """
        if self._log_to_file:
            self.__write_to_file(format)
        print(f'{self.__get_format(self.YELLOW, LogLevel.Warning)} {format}')
        print(self.RESET)


    def error(self, format: str) -> None:
        """
        Logs the message in red using `self.__get_format()`.
        """
        if self._log_to_file:
            self.__write_to_file(format)
        print(f'{self.__get_format(self.RED, LogLevel.Error)} {format}')
        print(self.RESET)


    def set_level(self, log_level: LogLevel) -> None | ValueError:
        """
        Sets the current log level. An ValueError is raised if the log level provided is incorrect.
        """
        if log_level not in [LogLevel.Info, LogLevel.Warning, LogLevel.Error]:
            raise ValueError('log_level must be LogLevel.{Info, Warning, Error}')
        self.log_level = log_level


    def enable_file_logging(self) -> None:
        """
        Enables logging to a file.
        """
        self._log_to_file = True


    def disable_file_logging(self) -> None:
        """
        Disables logging to a file.
        """
        self._log_to_file = False


    def clean_logs(self) -> None:
        """
        Removes the file `logs.txt` if it existed.
        """
        if os.path.exists(self._filename):
            os.remove(self._filename)
