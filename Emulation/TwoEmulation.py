# -*- coding:UTF-8 -*-
# AUTHOR: Joker
# FILE: BucketBrigadeSimulation/Emulation/TwoEmulation.py
# DATE: 2020/12/01 Tue
# TIME: 14:17:23

# DESCRIPTION:

from math import ceil
from decimal import Decimal


class TwoEmulation(object):
    def __init__(self, m, v1, v2, p, q):
        """Init the two emulation

        Parameters
        ----------
        m : int
            the number of station
        v1 : positive real number
            speed of worker 1
        v2 : positive real number
            speed of worker 2
        p : int
            initial position of worker 1
        q : int
            initial position of worker 2
        """
        self._m = Decimal(m)
        self._v1 = Decimal(v1)
        self._v2 = Decimal(v2)
        self._p = Decimal(p)
        self._q = Decimal(q)
        self._rou = self._v1 / self._v2
        self._handOffPointList = []
        self._maximumIteration = 100

    def IsCatchUp(self, currentPosition, initPosition=None):
        """Judge worker 1 can catch up worker 1

        Parameters
        ----------
        currentPosition : int
            current position of worker 2
        initPosition : int, none
            current position of worker 1, by default None

        Returns
        -------
        bool
            true, if worke 1 can catch up worker 2, else false
        """
        if initPosition is None:
            initPosition = self._p
        t = (self._m - currentPosition) / self._v2
        position = initPosition + t * self._v1
        return position > self._m - 1

    def GetFirstHandOffPoint(self):
        if self.IsCatchUp(currentPosition=self._q, initPosition=self._p):
            handOffPoint = self._m - Decimal(1)
        else:
            t = (self._m - self._q) / self._v2
            handOffPoint = Decimal(ceil(t * self._v1 + self._p))
        return handOffPoint

    def GetNextHandOffPoint(self, currentPosition):
        if self.IsCatchUp(currentPosition=currentPosition, initPosition=0):
            handOffPoint = self._m - 1
        else:
            t = (self._m - currentPosition) / self._v2
            handOffPoint = Decimal(ceil(t * self._v1))
        return handOffPoint

    def GetThroughput(self):
        indexA = self._maximumIteration - 1
        indexB = indexA - 1
        indexC = indexB - 1
        t1 = (self._m - self._handOffPointList[indexB]) / self._v2
        t2 = (self._m - self._handOffPointList[indexA]) / self._v2
        # idel time
        t3 = (self._handOffPointList[indexB] -
              (self._m - self._handOffPointList[indexC]) *
              (self._v1 / self._v2)) / self._v1
        t4 = (self._handOffPointList[indexA] -
              (self._m - self._handOffPointList[indexB]) *
              (self._v1 / self._v2)) / self._v1
        t1, t2, t3, t4 = max(0, t1), max(0, t2), max(0, t3), max(0, t4)
        return Decimal(2) / (t1 + t2 + t3 + t4)

    def GetMaximumThroughput(self):
        # return self._v2 / (self._m - (self._m * (self._v1 /
        #                                          (self._v1 + self._v2))))
        return (self._v1 + self._v2) / self._m

    def GetPerformanceRatio(self):
        return self.GetThroughput() / self.GetMaximumThroughput()

    def GetFixedPoint(self):
        indexA = self._maximumIteration - 1
        indexB = indexA - 1
        if self._handOffPointList[indexA] != self._handOffPointList[indexB]:
            return (self._handOffPointList[indexA],
                    self._handOffPointList[indexB])
        else:
            return (self._handOffPointList[indexA])

    def GetTheoreticFixedPoint(self):
        fp1 = Decimal(ceil(self._m * (self._rou) / (self._rou + 1)))
        condition = (self._m * self._rou - self._m + 1) / self._rou
        if fp1 > condition:
            return fp1
        elif self._rou >= self._m - 1:
            return self._m - 1
        return None

    def TheoreticFixedPointRegion(self):
        fp1 = Decimal((self._m * (self._rou) / (self._rou + Decimal(1))))
        condition = (self._m * self._rou - self._m + Decimal(1)) / self._rou
        if fp1 > condition:
            return (self._m * self._rou / (self._rou + Decimal(1)),
                    (self._m * self._rou + Decimal(1)) /
                    (self._rou + Decimal(1)))
        return (Decimal(0), self._m)

    def IsTheoreticFixedPointExisted(self):
        a, b = self.TheoreticFixedPointRegion()
        fp = self.GetTheoreticFixedPoint()
        if fp is None or (fp < a or fp >= b) or (fp <= Decimal(0)
                                                 or fp >= self._m):
            return False
        return True

    def Emulation(self):
        self._handOffPointList.append(self.GetFirstHandOffPoint())
        for i in range(self._maximumIteration):
            currentPosition = self._handOffPointList[i]
            self._handOffPointList.append(
                self.GetNextHandOffPoint(currentPosition=currentPosition))


if __name__ == "__main__":
    twoEmulation = TwoEmulation(m=3, v1=1, v2=1 / 0.8, p=1, q=2)
    twoEmulation.Emulation()
    print(twoEmulation._handOffPointList)
    print(twoEmulation.GetThroughput())
    print(twoEmulation.GetMaximumThroughput())
    print(twoEmulation.GetFixedPoint())
    print(twoEmulation.GetTheoreticFixedPoint())
    print(twoEmulation.IsTheoreticFixedPointExisted())
