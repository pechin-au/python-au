#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import modules
import math
import numpy
import matplotlib.pyplot as mpp

if __name__=='__main__':
    arguments = numpy.r_[-math.pi:math.pi:0.01] # from -pi to pi
    mpp.plot(
        arguments,
        [abs(math.sin(a)) for a in arguments]   # plot y=|sin(a)|
    )
    mpp.show()                                  # show plot
