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


from collections import namedtuple


ValueTuple = namedtuple('ValueTuple', 'header unit range zero value')
Unit = namedtuple('Unit', 'physEntity factor unit')

UnitTable = {
    1:  Unit(u"Electrical current",  0.1,    u"A"),
    2:  Unit(u"Electrical current",  5,      u"A"),
    3:  Unit(u"Voltage",             0.1,    u"V"),
    4:  Unit(u"Voltage",             1,      u"V"),
    5:  Unit(u"Voltage",             5,      u"V"),
    6:  Unit(u"Elec. resistance",    1,      u"Ω"),
    7:  Unit(u"Power (active)",      1,      u"W"),
    8:  Unit(u"Power (active)",      10,     u"W"),
    9:  Unit(u"Power (active)",      100,    u"W"),

    10: Unit(u"Power (apparent)",    1,      u"VA"),
    11: Unit(u"Power (apparent)",    10,     u"VA"),
    12: Unit(u"Power (apparent)",    100,    u"VA"),
    13: Unit(u"Power (reactive)",    1,      u"VAr"),
    14: Unit(u"Power (reactive)",    10,     u"Var"),
    15: Unit(u"Power (reactive)",    100,    u"VAr"),
    16: Unit(u"Frequency",           1,      u"Hz"),
    17: Unit(u"Frequency",           2.5,    u"Hz"),
    18: Unit(u"Rot. velocity",       12,     u"rpm"),
    19: Unit(u"Rot. velocity",       100,    u"rpm"),

    20: Unit(u"Temperature",         0.1,    u"°C"),
    21: Unit(u"Temperature",         1,      u"°C"),
    22: Unit(u"Flow",                0.1,    u"m³/h"),
    23: Unit(u"Flow",                1,      u"m³/h"),
    24: Unit(u"Head",                0.1,    u"m"),
    25: Unit(u"Head",                1,      u"m"),
    26: Unit(u"Head",                10,     u"m"),
    27: Unit(u"Pressure",            0.01,   u"bar"),
    28: Unit(u"Pressure",            0.1,    u"bar"),
    29: Unit(u"Pressure",            1,      u"bar"),

    30: Unit(u"Percentage",          1,      u"%"),
    31: Unit(u"Energy",              1,      u"kWh"),
    32: Unit(u"Energy",              10,     u"kWh"),
    33: Unit(u"Energy",              100,    u"kWh"),
    34: Unit(u"Ang. velocity",       2,      u"rad/s"),
    35: Unit(u"Time",                1,      u"h"),
    36: Unit(u"Time",                2,      u"min"),
    37: Unit(u"Time",                1,      u"s"),
    38: Unit(u"Frequency",           2,      u"Hz"),
    39: Unit(u"Time",                1024,   u"h"),

    40: Unit(u"Energy",              512,    u"kWh"),
    41: Unit(u"Flow",                5,      u"m³/h"),
    42: Unit(u"Electrical current",  0.2,    u"A"),
    43: Unit(u"Elec. resistance",    10,     u"kΩ"),
    44: Unit(u"Power (active)",      1,      u"kW"),
    45: Unit(u"Power (active)",      10,     u"kW"),
    46: Unit(u"Energy",              1,      u"MWh"),
    47: Unit(u"Energy",              10,     u"MWh"),
    48: Unit(u"Energy",              100,    u"MWh"),
    49: Unit(u"Ang. degrees",        1,      u"°"),

    50: Unit(u"Gain",                1,      u""),
    51: Unit(u"Pressure",            0.001,  u"bar"),
    52: Unit(u"Flow",                1,      u"l/s"),
    53: Unit(u"Flow",                1,      u"m³/s"),
    54: Unit(u"Flow",                1,      u"gpm"),
    55: Unit(u"Pressure",            1,      u"psi"),
    56: Unit(u"Head",                1,      u"ft"),
    57: Unit(u"Temperature",         1,      u"°F"),
    58: Unit(u"Flow",                10,     u"gpm"),
    59: Unit(u"Head",                10,     u"ft"),

    60: Unit(u"Pressure",            10,     u"psi"),
    61: Unit(u"Pressure",            1,      u"kPa"),
    62: Unit(u"Electrical current",  0.5,    u"A"),
    63: Unit(u"Flow",                0.1,    u"l/s"),
    64: Unit(u"Volume",              0.1,    u"m³"),
    65: Unit(u"Volume",              1000,   u"m³"),
    66: Unit(u"Energy pr vol.",      10,     u"kWh/m³"),
    67: Unit(u"Volume",              256,    u"m³"),
    68: Unit(u"Area",                1,      u"m²"),
    69: Unit(u"Flow",                0.1,    u"ml/h"),

    70: Unit(u"Volume",              0.1,    u"ml"),
    71: Unit(u"Volume",              1,      u"nl"),
    72: Unit(u"Time",                1024,   u"min"),
    73: Unit(u"Flow",                0.5,    u"l/h"),
    74: Unit(u"Energy pr vol.",      1,      u"Wh/m³")
}

