'''
Word search.

Copyright (C) 2020 Francis J. Hammell <hammell.francis@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

There is a copy of this license at <http://www.gnu.org/licenses/>.

Created on 09 Feb 2020

@author: fjh
'''
import sys
import os
import platform
import logging
import logging.handlers
import time

from Convert import Convert

# pylint: disable=too-few-public-methods
class Main:
    '''Used to start the application. Call Main.main().

    From the command line:-

        python Main.py
    '''
    LOG_NAME = "qif2csv.log"
    logger = logging.getLogger(__name__)
    FILES_LOCATION = "qif-data"

    def __init__(self):
        '''Do not use.
        '''
        raise RuntimeError("This class should never be instantiated.")

    @classmethod
    def main(cls):
        '''Start here.

        Returns:
            0 on a successful exit, else -1.
        '''
        cls.__config_logging()
        # pylint: disable=logging-format-interpolation
        cls.logger.debug("Started.")

        try:
            print ("Started.")
            current_dir_name = os.path.dirname(__file__)
            dir_name = os.path.join(current_dir_name, Main.FILES_LOCATION)
            Con = Convert()
            Con.convert_to_csv(dir_name)
            time.sleep(1)

        except Exception as ex:
            # pylint: disable=logging-format-interpolation
            cls.logger.critical("Error while running {0}".format(ex))
            cls.logger.warning("Bad exit.")
            sys.exit(-1)

        finally:
            pass

        cls.logger.info("Good exit.")
        sys.exit(0)

    @classmethod
    def __config_logging(cls):
        '''Format the logging output.
        '''
        # Create file logger.
        if platform.system() == "Windows":
            file_name = "./" + Main.LOG_NAME
        else:
            file_name = "/var/log/" + Main.LOG_NAME

#         logging.basicConfig(format="%(asctime)s %(name)s:%(levelname)s - %(message)s",
#                             datefmt="%d/%m/%Y %H:%M:%S",
#                             filename="./basic.log",
#                             filemode="a",
#                             level=logging.DEBUG)

        # Set root logger level.
        logging.getLogger("").setLevel(logging.DEBUG)

        # Add rotating file logger.
        rotating = logging.handlers.RotatingFileHandler(filename=file_name,
                                                        mode="a",
                                                        maxBytes=1000000,
                                                        backupCount=5)
        #rotating.setLevel(logging.DEBUG)
        formatter = logging.Formatter(fmt="%(asctime)s %(name)s:%(levelname)s - %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
        rotating.setFormatter(formatter)
        logging.getLogger("").addHandler(rotating)

        # Add console logger.
        console = logging.StreamHandler()
        #console.setLevel(logging.DEBUG)
        #formatter = logging.Formatter(fmt="%(asctime)s %(name)s:%(levelname)s - %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
        console.setFormatter(formatter)
        logging.getLogger("").addHandler(console)

        cls.logger.debug("Configured logging.")

def command_line_invocation():
    '''Tell me if it's a command line invocation.
    '''
    # pylint: disable=logging-format-interpolation
    Main.logger.debug("Started from the command line.")

if __name__ == "__main__":
    command_line_invocation()
    Main.main()
