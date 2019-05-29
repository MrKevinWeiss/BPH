#! /usr/bin/env python3
# Copyright (c) 2019 Kevin Weiss, for HAW Hamburg  <kevin.weiss@haw-hamburg.de>
#
# This file is subject to the terms and conditions of the MIT License. See the
# file LICENSE in the top level directory for more details.
# SPDX-License-Identifier:    MIT

"""
This script handles interfacing to the BPG and PHiLIP device.  It parses data
and exposes from the PhilipExtIf class to be run in a shell.  It also adds
specific functions used by the BPH such as power monitoring and gpio toggling.

The purpose of this script is allow easy setup and manual usage of the BPH.

Usage
-----

```
usage: bph_shell.py  [-h]
                        [--loglevel {debug,info,warning,error,fatal,critical}]
                        [--port PORT]
                        [--filter-data]

optional arguments:
  -h, --help            show this help message and exit
  --loglevel {debug,info,warning,error,fatal,critical}
                        Python logger log level (default: warning)
  --port, -p
                        Specify the serial port
  --data_only, -do
                        Filters data from philip responses to only display
                        what is needed (default: False)
```
"""
import cmd
from json import dumps
import logging
import argparse
import serial.tools.list_ports
try:
    import readline
except ImportError:
    readline = None
from philip_pal.philip_shell import PhilipShell
try:
    from .bph_if import BphIf
except (ImportError, SystemError):
    from bph_if import BphIf

class BphShell(PhilipShell):

    prompt = 'BPT: '
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



PARSER = argparse.ArgumentParser()

LOG_LEVELS = ('debug', 'info', 'warning', 'error', 'fatal', 'critical')
PARSER.add_argument('--loglevel', choices=LOG_LEVELS, default='info',
                    help='Python logger log level')
PARSER.add_argument('--port', '-p', help='Specifies the serial port',
                    default=None)
PARSER.add_argument('--data_filter_off', '-do', default=True,
                    action='store_false',
                    help='Filters data from philip responses')
PARSER.add_argument('--use_dev_map', '-dm', default=False,
                    action='store_true',
                    help='Uses the memory map from device')

def main():
    """Main program"""
    pargs = PARSER.parse_args()

    if pargs.loglevel:
        loglevel = logging.getLevelName(pargs.loglevel.upper())
        logging.basicConfig(level=loglevel)
    BphShell(port=pargs.port, data_only=pargs.data_filter_off,
                use_dev_map=pargs.use_dev_map).cmdloop()


if __name__ == '__main__':
    main()
