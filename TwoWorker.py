# -*- coding:UTF-8 -*-
# AUTHOR: Joker
# FILE: TwoWorker.py
# DATE: 2020/12/02 Wed
# TIME: 22:26:23

# DESCRIPTION:

import itertools as it
from Emulation.TwoEmulation import TwoEmulation

if __name__ == "__main__":
    totalSpeed = 2
    for m in range(5, 23, 2):
        for rou in range(1, 1000):
            for speed in range(2):
                if speed == 0:
                    v1 = totalSpeed / (1 + rou / 1000.0)
                    v2 = v1 * (rou / 10.)
                else:
                    v1 = totalSpeed / (1 + rou / 1000.0)
                    v2 = v1 * (rou / 10.)
                positionList = list(
                    it.combinations([i for i in range(1, m)], 2))
                for p, q in positionList:
                    twoEmulation = TwoEmulation(m=m, v1=v1, v2=v2, p=p, q=q)
                    twoEmulation.Emulation()
                    if twoEmulation.IsTheoreticFixedPointExisted() is True:
                        print('%s %s %s %s %s %s 1' %
                              (str(m), str(p), str(q), str(
                                  v1 / v2), str(twoEmulation.GetThroughput()),
                               str(100. * twoEmulation.GetPerformanceRatio())))
                    else:
                        print('%s %s %s %s %s %s 2' %
                              (str(m), str(p), str(q), str(
                                  v1 / v2), str(twoEmulation.GetThroughput()),
                               str(100. * twoEmulation.GetPerformanceRatio())))
                    # print('rou is %f' % (v1 / v2))
                    # # print(twoEmulation._handOffPointList)
                    # print('Throughput is %f' % twoEmulation.GetThroughput())
                    # print('Maximum throughput is %f' %
                    #       twoEmulation.GetMaximumThroughput())
                    # print('Performance is %f%%' %
                    #       (100. * twoEmulation.GetPerformanceRatio()))
                    # print('Fixed point is %s' % str(twoEmulation.GetFixedPoint()))
                    # print('Fixed point in Theoretic is %s' %
                    #       str(twoEmulation.GetTheoreticFixedPoint()))
                    # print('Fixed point in Theoretic exist: %s' %
                    #       str(twoEmulation.IsTheoreticFixedPointExisted()))
                    # print('-' * 12)
