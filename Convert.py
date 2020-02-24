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
import logging

class Convert:
    '''
    '''
    logger = logging.getLogger(__name__)


    def __init__(self):
        '''
        Constructor
        '''
        # self.words = []
        # self._load_file()

    def convert_to_csv(self):
        '''Convert the files to CSV format.
        '''
        print("Converting...")

    # def contains_letter(self, letter):
    #     '''Get a list of words containing the letter.
    #     '''
    #     matcher = [letter]
    #     words_containing_letter = [word for word in self.words if any(match in word for match in matcher)]
    #     # (item for item in iterable if function(item))

    #     # print (words_containing_letter)
    #     print (len(words_containing_letter))