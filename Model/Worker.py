# -*- coding: utf-8 -*-
import sys
import os

bp = os.path.dirname(os.path.realpath('.')).split(os.sep)
modpath = os.sep.join(bp)
sys.path.insert(0, modpath)

from Tools.WorkerState import WorkerState
from Tools.Direction import Direction


class Worker(object):
    def __init__(self, ID, initPosition, forwardVelocity, backwardVelocity,
                 handoffTime, operatingZone):
        self._workerID = ID
        self._state = WorkerState.Idle
        self._direction = Direction.Forward
        self._initPosition = initPosition
        self._currentPosition = self._initPosition
        self._nextPosition = self._currentPosition + 1
        self._path = [self._initPosition]
        self._forwardVelocity = forwardVelocity
        # backwardVelocity = -1 \
        # backward velocity is not take into consideration
        self._backwardVelocity = backwardVelocity
        # handoffTime = -1 \
        # handoffTime is not take into consideration
        self._handoffTime = handoffTime
        self._operatingZone = operatingZone

    def IsPeriodic(self):
        flag = False
        if self._path == [] or len(self._path) == 1:
            return flag
        for i in range(1, len(self._path)):
            if self._path[i] in self._path[i + 1:]:
                flag = True
                break
        return flag

    def GetPath(self):
        return self._path

    def SetWorkerState(self, state):
        self._state = state

    def GetWorkerState(self):
        return self._state

    def SetWorkerDirection(self, direction):
        self._direction = direction

    def GetWorkerDirection(self):
        return self._direction

    def GetCurrentPosition(self):
        return self._currentPosition

    def GetNextPosition(self):
        return self._nextPosition

    def SetNextPosition(self, nextPosition):
        self._nextPosition = nextPosition

    def SetCurrentPosition(self, newPosition):
        self._currentPosition = newPosition
        self._nextPosition = self._currentPosition + 1
        self._path.append(self._currentPosition)

    def SetInitPosition(self, newPosition):
        self._initPosition = newPosition
        self._currentPosition = self._initPosition
        self._nextPosition = self._currentPosition + 1
        self._path = [self._initPosition]
