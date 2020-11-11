# -*- coding: utf-8 -*-


class Station(object):
    def __init__(self, ID, workcontent):
        self._isBusy = False
        self._stationID = ID
        self._workcontent = workcontent

    def OccupyStation(self):
        self._isBusy = True

    def ReleaseStation(self):
        self._isBusy = False

    def IsBusy(self):
        return self._isBusy
