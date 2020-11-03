# -*- coding: utf-8 -*-


class BBTimer(object):
    def __init__(self):
        self._currentTime = 0
        self._eventList = []

    def GetCurrentTime(self):
        return self._currentTime

    def ReSetCurrentTime(self):
        self._currentTime = 0.0

    def SetCurrentTime(self, newTime):
        self._currentTime = newTime

    def ReSetEventList(self):
        self._eventList = []

    def AddEvent(self, event):
        self._eventList.append(event)

    def AddEvents(self, eventList):
        self._eventList += eventList

    def GetNextEvent(self):
        if len(self._eventList) == 0 or self._eventList == []:
            return None
        eventEndTime = list(map(lambda x: x._endTime, self._eventList))
        minEventEndTime = min(eventEndTime)
        event = [
            eve for eve in self._eventList if eve._endTime == minEventEndTime
        ]
        self._eventList = [eve for eve in self._eventList if eve not in event]
        return event
