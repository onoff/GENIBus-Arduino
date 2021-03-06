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

import abc
import logging
import threading
from wx.lib.pubsub import Publisher as Publisher

DATA_NOT_AVAILABLE = None

class IController(object):
    __metaclass__ = abc.ABCMeta
    logger = logging.getLogger("genicontrol")
    quitViewEvent = threading.Event()
    quitModelEvent = threading.Event()

    def __init__(self, modelCls, viewClass):
        self._pub = Publisher()
        self._view = viewClass  # (self, model)
        self._model = modelCls()
        self._viewThread = self._view.initialize(self._model, IController.quitViewEvent)
        # TODO: Create and disable controls.
        self._modelThread = self._model.initialize(IController.quitModelEvent)


