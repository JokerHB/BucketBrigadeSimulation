# -*- coding: utf-8 -*-


class BBEvent(object):
    def __init__(self, workerID, title, startTime, duraTime, level):
        self._workerID = workerID
        self._title = title
        self._level = level
        self._startTime = startTime
        self._duraTime = duraTime
        self._endTime = self._startTime + self._duraTime