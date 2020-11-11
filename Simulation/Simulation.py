# -*- coding: utf-8 -*-
import sys
import os

bp = os.path.dirname(os.path.realpath('.')).split(os.sep)
modpath = os.sep.join(bp)
sys.path.insert(0, modpath)

from Model.BBEvent import BBEvent
from Model.BBTimer import BBTimer
from Model.Station import Station
from Model.Worker import Worker


class TwoSimulation(object):
    def __init__(self, workers, stations):
        self._workers = workers
        self._stations = stations
        self._idleWorkers = []
        self._timer = BBTimer.Instance()

    def IsPeriodic(self):
        periodic = list(map(lambda x: x.IsPeriodic(), self._workers))
        return periodic

    def GetStation(self, stationID):
        result = list(
            filter(lambda x: x._stationID == stationID, self._stations))
        if result is None or result == []:
            return None
        return result[0]

    def GetWorker(self, workerID):
        result = list(filter(lambda x: x._workerID == workerID, self._workers))
        if result is None or result == []:
            return None
        return result[0]

    def ReleaseStations(self, workerIDs):
        for workerID in workerIDs:
            worker = self.GetWorker(workerID=workerID)
            station = self.GetStation(stationID=worker.GetCurrentPositio())
            station.ReleaseStation()

    def MoveToNextStation(self, workerID):
        worker = self.GetWorker(workerID=workerID)
        nextStationID = worker.GetNextPosition()
        nextStation = self.GetStation(stationID=nextStationID)
        # MARK: Forward
        if nextStationID <= len(
                self._stations) - 1 and nextStation.IsBusy() is False:
            title = 'worker %d work at station %d, current time is %f' % (
                worker._workerID, nextStation,
                float(self._timer.GetCurrentTime()))
            startTime = self._timer.GetCurrentTime()
            duraTime = nextStation._workcontent / worker._forwardVelocity
            level = 0
            event = BBEvent(workerID=worker._workerID,
                            title=title,
                            startTime=startTime,
                            duraTime=duraTime,
                            level=level)
            nextStation.OccupyStation()
            worker.SetCurrentPosition(newPosition=worker.GetNextPosition())
            self._timer.AddEvent(event=event)
        # MARK: Backward
        # TODO: Backward part

    def InitSimulation(self):
        for worker in self._workers:
            title = 'worker %d start at station %d, current time is %f' % (
                worker._workerID, worker._initPosition,
                float(self._timer.GetCurrentTime()))
            startTime = 0
            station = self.GetStation(stationID=worker._stationID)
            station.OccupyStation()
            duraTime = station._workcontent / worker._forwardVelocity
            level = 0
            event = BBEvent(workerID=worker._workerID,
                            title=title,
                            startTime=startTime,
                            duraTime=duraTime,
                            level=level)
            self._timer.AddEvent(event=event)

    def Simulate(self):
        self.InitSimulation()
        while False in self.IsPeriodic():
            events = self._timer.RunNextEvent()
            workerIDs = [x._workerID for x in events]
            self.ReleaseStations(workerIDs=workerIDs)
            self._idleWorkers += workerIDs
            self._idleWorkers.sort()[::-1]
            for workerID in self._idleWorkers:
                self.MoveToNextStation(workerID=workerID)


if __name__ == "__main__":
    timer = BBTimer.Instance()
    # event = BBEvent()
    # station = Station()
    # Worker = Worker()
