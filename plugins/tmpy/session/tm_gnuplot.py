#!/usr/bin/env python
###############################################################################
##
## MODULE      : tm_gnuplot.py
## DESCRIPTION : Launcher for the Gnuplot plugin
## COPYRIGHT   : (C) 2019  Darcy Shen
##
## This software falls under the GNU general public license version 3 or later.
## It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
## in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.

import os
import sys
sys.path.append(os.environ.get("TEXMACS_PATH") + "/plugins/")

from tmpy.protocol        import *
from tmpy.graph.gnuplot   import Gnuplot
from tmpy.capture         import CaptureStdout
from tmpy.compat          import *

my_globals   = {}

if py_ver == 3:
    text = 'import builtins as __builtins__'
else:
    text = 'import __builtin__ as __builtins__'
CaptureStdout.capture (text, my_globals, "tm_gnuplot")

current = Gnuplot()
current.greet()

# Main session loop.
while True:
    line = tm_input()
    if not line:
        continue
    if line[0] == DATA_COMMAND:
        # TODO: Handle completions
        continue
    else:
        lines = []
        for x in line.split('~'):
            lines.append(x)
        while line != "<EOF>":
            line = tm_input()
            if line == '': 
                continue
            for x in line.split('~'):
                lines.append(x)

        text='\n'.join(lines[:-1])

        current.eval(text)