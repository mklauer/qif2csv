# Word Search

This is a Python application that is used to convert QIF files to CSV format. The main file of the application is `Main.py`.

## Copyright

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

There is a copy of this license at <http://www.gnu.org/licenses/>.

## Installation

To install this application, you need to have Python installed on your machine. You can download the code from this repository and run it on your local machine.

## Configuration

The application uses a logging system to keep track of the application's activities. The log file is named `qif2csv.log` and its location depends on the platform. For Windows, it is located in the current directory, and for other platforms, it is located in `/var/log/`.

The application also requires a directory named `qif-data` in the same directory as `Main.py` where it will look for files to convert.

## Usage

To use the application, navigate to the directory containing `Main.py` and run the following command:

```
python Main.py
```

The application will then convert all files in the `qif-data` directory to CSV format.

## Development

The conversion process is done by the class [Convert](Convert.py). 
It uses parts of the [QIF Specification](https://en.wikipedia.org/wiki/Quicken_Interchange_Format)
