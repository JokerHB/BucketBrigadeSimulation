# -*- coding: utf-8 -*-

import threading


class BBTimer(object):
    _instanceLock = threading.Lock()

    def __init__(self):
        self._currentTime = 0
        self._eventList = []

    @classmethod
    def Instance(cls, *args, **kwargs):
        with BBTimer._instanceLock:
            if not hasattr(BBTimer, '_instance'):
                BBTimer._instance = BBTimer(*args, **kwargs)
        return BBTimer._instance

    def GetCurrentTime(self):
        return self._currentTime

    def ReSetCurrentTime(self):
        self._currentTime = 0.0

    def SetCurrentTime(self, newTime):
        self._currentTime = newTime

    def ReSetEventList(self):
        self._eventList = []

    def ReSetTimer(self):
        self.ReSetCurrentTime()
        self.ReSetEventList()

    def AddEvent(self, event):
        self._eventList.append(event)

    def AddEvents(self, eventList):
        self._eventList += eventList

    def UpdateEvents(self):
        for event in self._eventList:
            event._endTime -= self._currentTime

    def RunNextEvent(self):
        if len(self._eventList) == 0 or self._eventList == []:
            return None
        eventEndTime = list(map(lambda x: x._endTime, self._eventList))
        minEventEndTime = min(eventEndTime)
        event = [
            eve for eve in self._eventList if eve._endTime == minEventEndTime
        ]
        self._currentTime += minEventEndTime
        self._eventList = [eve for eve in self._eventList if eve not in event]
        self.UpdateEvents()
        return event


if __name__ == "__main__":
    time1 = BBTimer.Instance()
    print(time1._currentTime, time1._eventList)

    time1._currentTime = 100
    print(time1._currentTime, time1._eventList)

    time2 = BBTimer.Instance()
    print(time2._currentTime, time2._eventList)

    time2._currentTime = 200
    print(time2._currentTime, time2._eventList)

    print(time1._currentTime, time1._eventList)
