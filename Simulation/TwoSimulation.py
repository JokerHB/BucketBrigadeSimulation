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
from Tools.WorkerState import WorkerState
from Tools.Direction import Direction


class TwoSimulation(object):
    def __init__(self, workers, stations):
        self._workers = workers
        self._stations = stations
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
            station = self.GetStation(stationID=worker.GetCurrentPosition())
            station.ReleaseStation()

    def ReleaseWorkers(self, workerIDs):
        for workerID in workerIDs:
            worker = self.GetWorker(workerID=workerID)
            worker.SetWorkerState(state=WorkerState.Idle)

    def MoveToNextStation(self, workerID):
        worker = self.GetWorker(workerID=workerID)
        nextStationID = worker.GetNextPosition()
        if nextStationID == len(self._stations) + 1:
            worker.SetWorkerState(state=WorkerState.Idle)
            self.ResetWorkers()
            return None
        nextStation = self.GetStation(stationID=nextStationID)
        if nextStation.IsBusy() is False:
            title = 'worker %d work at station %d, current time is %f' % (
                worker._workerID, nextStation._stationID,
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
            worker.SetWorkerState(state=WorkerState.Busy)
            worker.SetCurrentPosition(newPosition=worker.GetNextPosition())
            self._timer.AddEvent(event=event)

    def ResetWorkers(self):
        workerIDs = list(map(lambda x: x._workerID, self._workers))[::-1]
        for i in range(len(workerIDs) - 1):
            worker = self.GetWorker(workerID=workerIDs[i])
            preWorker = self.GetWorker(workerID=workerIDs[i + 1])
            if preWorker.GetWorkerState() == WorkerState.Idle:
                worker.SetNextPosition(
                    nextPosition=preWorker.GetNextPosition())
            elif preWorker.GetWorkerState() == WorkerState.Busy:
                worker.SetNextPosition(
                    nextPosition=preWorker.GetNextPosition())
                events = self._timer.RunNextEvent()
                workerIDs = [x._workerID for x in events]
                self.ReleaseStations(workerIDs=workerIDs)
                self.ReleaseWorkers(workerIDs=workerIDs)
            worker.AddHandOffPoint(handOffPoint=worker.GetNextPosition())
            preWorker.AddHandOffPoint(handOffPoint=worker.GetNextPosition())
        worker = self.GetWorker(workerID=workerIDs[-1])
        worker.SetNextPosition(nextPosition=1)

    def InitSimulation(self):
        for worker in self._workers:
            title = 'worker %d start at station %d, current time is %f' % (
                worker._workerID, worker._initPosition,
                float(self._timer.GetCurrentTime()))
            startTime = 0.0
            station = self.GetStation(stationID=worker.GetCurrentPosition())
            station.OccupyStation()
            worker.SetWorkerState(state=WorkerState.Busy)
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
            if events != None:
                workerIDs = [x._workerID for x in events]
                self.ReleaseStations(workerIDs=workerIDs)
                self.ReleaseWorkers(workerIDs=workerIDs)
            idleWorkers = list(
                filter(lambda x: x.GetWorkerState() == WorkerState.Idle,
                       self._workers))
            idleWorkerIDs = list(map(lambda x: x._workerID, idleWorkers))
            idleWorkerIDs.sort(reverse=True)
            for workerID in idleWorkerIDs:
                self.MoveToNextStation(workerID=workerID)
        for worker in self._workers:
            print(worker.GetHandOffPoint())
        for worker in self._workers:
            print(worker.GetPath())


if __name__ == "__main__":
    worker1 = Worker(ID=1,
                     initPosition=2,
                     forwardVelocity=1.5,
                     backwardVelocity=-1,
                     handoffTime=-1,
                     operatingZone=None)
    worker2 = Worker(ID=2,
                     initPosition=3,
                     forwardVelocity=1,
                     backwardVelocity=-1,
                     handoffTime=-1,
                     operatingZone=None)

    station1 = Station(ID=1, workcontent=1)
    station2 = Station(ID=2, workcontent=1)
    station3 = Station(ID=3, workcontent=1)
    station4 = Station(ID=4, workcontent=1)
    station5 = Station(ID=5, workcontent=1)

    simulation = TwoSimulation(
        workers=[worker1, worker2],
        stations=[station1, station2, station3, station4, station5])

    simulation.Simulate()
