#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
##
## Grundfos GENIBus Library for Arduino.
##
## (C) 2007-2013 by Christoph Schueler <github.com/Christoph2,
##                                      cpu12.gems@googlemail.com>
##
##  All Rights Reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program; if not, write to the Free Software Foundation, Inc.,
## 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
##
##
##
## GENIBus device database.
##

import csv
import logging
import os
from genicontrol.utils import absConfigurationFilename

logger = logging.getLogger("genicontrol")

def getDeviceFileName(family, type_, version):
    return "GeniBus-%s.%s.%s.info" % (family, type_, version)

def deviceInfoExists(family, type_, version):
    return os.access(absConfigurationFilename(getDeviceFileName(family, type_, version)), os.F_OK)

def loadDeviceInfo(family, type_, version):
    pass

def saveDeviceInfo(family, type_, version, info):
    pass

def main():
    print deviceInfoExists(0x03, 0x01, 0x42)

if __name__ == '__main__':
    main()

