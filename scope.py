#!/usr/bin/env python3

import sys

from ds1054z import DS1054Z

IP_ADDRESS = '192.168.2.4'


scope = DS1054Z(IP_ADDRESS)

print(scope.idn)

chan1 = scope.get_waveform_samples('CHAN1')

print(chan1)