#!/usr/bin/python3
################################################################################
# status.py - python i3bar status line generator
#
# author: mutantmonkey <mutantmonkey@mutantmonkey.in>
################################################################################

import json
import sys
import time

from battery import *
from clock import *
# from mpdstatus import *
from weather import *
from wifi import *
from applesmc import *

RUN_INTERVAL = 1
widgets = [
    AppleSmcWidget(),
    WifiWidget('wlp4s0'),
    BatteryWidget('BAT0'), 
    #MpdStatusWidget('gigantea.mutantmonkey.in'),
    WeatherWidget('KBCB'),
    ClockWidget(),
]


print(json.dumps({'version': 1}) + '[[]')
while True:
    output = []
    for widget in widgets:
        output.append(widget.output())
    print(',' + json.dumps(output), flush=True)
    time.sleep(RUN_INTERVAL)
print(']')
