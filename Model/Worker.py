# -*- coding: utf-8 -*-


class Worker(object):
    def __init__(self, ID, initPosition, forwardVelocity, backwardVelocity,
                 handoffTime, operatingZone):
        self._workerID = ID
        self._initPosition = initPosition
        self._currentPosition = self._initPosition
        self._forwardVelocity = forwardVelocity
        # backwardVelocity = -1 \
        # backward velocity is not take into consideration
        self._backwardVelocity = backwardVelocity
        # handoffTime = -1 \
        # handoffTime is not take into consideration
        self._handoffTime = handoffTime
        self._operatingZone = operatingZone

    def GetCurrentPosition(self):
        return self._currentPosition

    def SetCurrentPosition(self, newPosition):
        self._currentPosition = newPosition

    def SetInitPosition(self, newPosition):
        self._initPosition = newPosition
        self._currentPosition = self._initPosition
