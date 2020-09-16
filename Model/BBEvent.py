# -*- coding: utf-8 -*-

class BBEvent(object):
    def __init__(self, title, startTime, duraTime, level):
        self._title = title
        self._level = level
        self._startTime = startTime
        self._duraTime = duraTime
        self._endTime = self._startTime + self._duraTime