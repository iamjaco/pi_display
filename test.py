#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Example for seven segment displays.
"""

import sys
import time
from datetime import datetime

from demo_opts import get_device
from luma.core.virtual import viewport, sevensegment

def main():
    # create seven segment device
    device = get_device()

    if not hasattr(device, 'segment_mapper'):
        sys.exit('sevensegment is not supported on a {} device'.format(
            device.__class__.__name__))

    seg = sevensegment(device)

    print('Simple text...')
    for _ in range(8):
        seg.text = "HELLO"
        time.sleep(0.6)
        seg.text = " GOODBYE"
        time.sleep(0.6)

device.contrast(0x7F)

if __name__ == '__main__':
    main()
