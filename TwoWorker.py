# -*- coding:UTF-8 -*-
# AUTHOR: Joker
# FILE: TwoWorker.py
# DATE: 2020/12/02 Wed
# TIME: 22:26:23

# DESCRIPTION:

# cython: language_level=3

import itertools as it
from decimal import Decimal
from Emulation.TwoEmulation import TwoEmulation


def TPofFixedPoint():
    totalSpeed = Decimal('2')
    for m in range(5, 23, 2):
        for rou in range(1, 100):
            v2 = totalSpeed / Decimal(
                Decimal('1') + Decimal(rou) / Decimal('100.0'))
            v1 = v2 * (rou / Decimal('100.'))
            positionList = list(it.combinations([i for i in range(1, m)], 2))
            for p, q in positionList:
                twoEmulation = TwoEmulation(m=m, v1=v1, v2=v2, p=p, q=q)
                twoEmulation.Emulation()
                emulationTwo = TwoEmulation(m=m, v1=v2, v2=v1, p=p, q=q)
                emulationTwo.Emulation()
                if isinstance(twoEmulation.GetFixedPoint(),
                              Decimal) and isinstance(
                                  emulationTwo.GetFixedPoint(), Decimal):
                    if abs(twoEmulation.GetThroughput() -
                           emulationTwo.GetThroughput()) > 1e-7:
                        print('%s %s %s %s %s %s %s %s' %
                              (str(m), str(p), str(q), str(
                                  v1 / v2), str(twoEmulation.GetThroughput()),
                               str(
                                   Decimal('100.') *
                                   twoEmulation.GetPerformanceRatio()),
                               str(twoEmulation.GetFixedPoint()),
                               str(twoEmulation.GetTheoreticFixedPoint())))
                        print('%s %s %s %s %s %s %s %s' %
                              (str(m), str(p), str(q), str(
                                  v2 / v1), str(emulationTwo.GetThroughput()),
                               str(
                                   Decimal('100.') *
                                   emulationTwo.GetPerformanceRatio()),
                               str(emulationTwo.GetFixedPoint()),
                               str(emulationTwo.GetTheoreticFixedPoint())))
                        print('*' * 12)


def FPTheoreticVSReal():
    totalSpeed = Decimal('2')
    for m in range(5, 23, 2):
        for rou in range(1, 100):
            v2 = totalSpeed / Decimal(
                Decimal('1') + Decimal(rou) / Decimal('100.0'))
            v1 = v2 * (rou / Decimal('100.'))
            positionList = list(it.combinations([i for i in range(1, m)], 2))
            for p, q in positionList:
                twoEmulation = TwoEmulation(m=m, v1=v1, v2=v2, p=p, q=q)
                twoEmulation.Emulation()
                emulationTwo = TwoEmulation(m=m, v1=v2, v2=v1, p=p, q=q)
                emulationTwo.Emulation()
                if twoEmulation.GetFixedPoint(
                ) != twoEmulation.GetTheoreticFixedPoint(
                ) and twoEmulation.IsTheoreticFixedPointExisted() is True:
                    print('%s %s %s %s %s %s %s %s' %
                          (str(m), str(p), str(q), str(
                              v1 / v2), str(twoEmulation.GetThroughput()),
                           str(
                               Decimal('100.') *
                               twoEmulation.GetPerformanceRatio()),
                           str(twoEmulation.GetFixedPoint()),
                           str(twoEmulation.GetTheoreticFixedPoint())))
                if emulationTwo.GetFixedPoint(
                ) != emulationTwo.GetTheoreticFixedPoint(
                ) and emulationTwo.IsTheoreticFixedPointExisted() is True:
                    print('%s %s %s %s %s %s %s %s' %
                          (str(m), str(p), str(q), str(
                              v2 / v1), str(emulationTwo.GetThroughput()),
                           str(
                               Decimal('100.') *
                               emulationTwo.GetPerformanceRatio()),
                           str(emulationTwo.GetFixedPoint()),
                           str(emulationTwo.GetTheoreticFixedPoint())))
                print('*' * 12)


if __name__ == "__main__":
    FPTheoreticVSReal()

    # print('rou is %f' % (v1 / v2))
    # print(twoEmulation._handOffPointList)
    # print('Throughput is %f' % twoEmulation.GetThroughput())
    # print('Maximum throughput is %f' %
    #       twoEmulation.GetMaximumThroughput())
    # print('Performance is %f%%' %
    #       (Decimal('100.0') * twoEmulation.GetPerformanceRatio()))
    # print('Fixed point is %s' % str(twoEmulation.GetFixedPoint()))
    # print('Fixed point in Theoretic is %s' %
    #       str(twoEmulation.GetTheoreticFixedPoint()))
    # print('Fixed point in Theoretic exist: %s' %
    #       str(twoEmulation.IsTheoreticFixedPointExisted()))
    # print('-' * 12)
