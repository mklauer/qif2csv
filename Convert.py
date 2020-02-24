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
import os, fnmatch
import glob
import logging

class Convert:
    '''
    '''
    logger = logging.getLogger(__name__)
    FILE_EXTENSION = "*.qif"
    # {'^', 'S', '!Type:Invst\n', 'E', '$', '!Type:Cash\n', 'L', '!Type:Bank\n', 'C', 'P', 'M', '!Type:CCard\n', '!Type:Oth A\n', 'N', 'Q', 'Y', 'I', 'D', 'T'}
    DETAIL_CODES_DICT = {"I": "Price.",
                        "C": "Cleared status. Values are blank (unreconciled/not cleared), '*' or 'c' (cleared) and 'X' or 'R' (reconciled).",
                        "P": "Payee. Or a description for deposits, transfers, etc.",
                        "S": "Split category. Same format as L (Categorization) field. (40 characters maximum).",
                        "$": "Amount transferred, if cash is moved between accounts.",
                        "Y": "Security name.",
                        "D": "Date. Leading zeroes on month and day can be skipped. Year can be either 4 digits or 2 digits or 6 (=2006).",
                        "E": "Split memo—any text to go with this split item.",
                        "Q": "Quantity of shares (or split ratio, if Action is StkSplit).",
                        "T": "Amount of the item. For payments, a leading minus sign is required. For deposits, either no sign or a leading plus sign is accepted. Do not include currency symbols ($, £, ¥, etc.). Comma separators between thousands are allowed.",
                        "N": "Number of the check. Can also be 'Deposit', 'Transfer', 'Print', 'ATM', 'EFT'.",
                        "L": "Category or Transfer and (optionally) Class. The literal values are those defined in the Quicken Category list. SubCategories can be indicated by a colon (':') followed by the subcategory literal. If the Quicken file uses Classes, this can be indicated by a slash ('/') followed by the class literal. For Investments, MiscIncX or MiscExpX actions, Category/class or transfer/class. (40 characters maximum).",
                        "M": "Memo—any text you want to record about the item."}

    HEADER_DICT = {"!Type:Invst": "Investing: Investment Account.",
                    "!Type:Cash": "Cash Flow: Cash Account.",
                    "!Type:Bank": "Cash Flow: Checking & Savings Account.",
                    "!Type:CCard": "Cash Flow: Credit Card Account.",
                    "!Type:Oth A": "Property & Debt: Asset."}


    def __init__(self):
        '''
        Constructor
        '''
        self.detail_codes = set()
        # self.words = []
        # self._load_file()

    def convert_to_csv(self, files_location):
        '''Convert the files to CSV format.
        '''
        print("Converting...")
        self.files_list = self._get_files(files_location)
        print(self.files_list)
        for f in self.files_list:
            self._read_file(files_location, f)

        print(self.detail_codes)

    def _get_files(self, files_location):
        '''Get a list of the files.
        '''
        return fnmatch.filter(os.listdir(files_location), Convert.FILE_EXTENSION)

    def _read_file(self, files_location, f):
        '''Read the files.
        '''
        contents = open(os.path.join(files_location, f), "r")
        for line in contents:
            self._parse_line(line)
            # print(line)

    def _parse_line(self, line):
        '''...
        '''
        first_char = line[0]
        self._switch(first_char, line)
        # if first_char == "!":
        #     self.detail_codes.add(line)
        # else:
        #     self.detail_codes.add(first_char)
        
    def _switch(self, first_char, line):
        '''...
        '''
        if first_char == "!":
            pass
        elif first_char == "I":
            pass
        elif first_char == "C":
            pass
        elif first_char == "P":
            pass
        elif first_char == "S":
            pass
        elif first_char == "$":
            pass
        elif first_char == "Y":
            pass
        elif first_char == "D":
            pass
        elif first_char == "E":
            pass
        elif first_char == "Q":
            pass
        elif first_char == "T":
            pass
        elif first_char == "N":
            pass
        elif first_char == "L":
            pass
        elif first_char == "M":
            pass
        elif first_char == "^":
            # Throw exception.
            pass
        else:
            print(line)

    # def save_m3u(self):
    #     '''Save the class play list.
    #     '''
    #     playlist_file = open("./new lists/" + self.playlist_name.rstrip(".wpl") + self.FILE_EXTENSION, "w")  #, encoding="utf-8")
    #     playlist_file.write(self.new_playlist)
    #     playlist_file.close()

    # def contains_letter(self, letter):
    #     '''Get a list of words containing the letter.
    #     '''
    #     matcher = [letter]
    #     words_containing_letter = [word for word in self.words if any(match in word for match in matcher)]
    #     # (item for item in iterable if function(item))

    #     # print (words_containing_letter)
    #     print (len(words_containing_letter))