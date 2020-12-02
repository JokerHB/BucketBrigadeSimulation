# -*- coding:UTF-8 -*-
# AUTHOR: Joker
# FILE: TwoWorker.py
# DATE: 2020/12/02 Wed
# TIME: 22:26:23

# DESCRIPTION:

from Emulation.TwoEmulation import TwoEmulation

if __name__ == "__main__":
    for rou in range(1, 10):
        twoEmulation = TwoEmulation(m=5, v2=1, v1=1 / (rou / 10.), p=1, q=2)
        twoEmulation.Emulation()
        # print('rou is %f' % (rou / 10.))
        # print('Throughput is %f' % twoEmulation.GetThroughput())
        # print('Maximum throughput is %f' % twoEmulation.GetMaximumThroughput())
        print('Performance is %f%%' % (100. *
                                       (twoEmulation.GetThroughput() /
                                        twoEmulation.GetMaximumThroughput())))
        # print('Fixed point is %s' % str(twoEmulation.GetFixedPoint()))
        # print('Fixed point in Theoretic is %s' %
        #       str(twoEmulation.GetTheoreticFixedPoint()))
        # print('Fixed point in Theoretic exist: %s' %
        #       str(twoEmulation.IsTheoreticFixedPointExisted()))
        # print('-' * 12)
