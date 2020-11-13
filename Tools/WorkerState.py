# -*- coding: utf-8 -*-

from enum import Enum


class WorkerState(Enum):
    Idle = 0
    Busy = 1
    Block = 2
    Starvation = 3
    Halt = 4
    