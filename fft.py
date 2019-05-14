#!/usr/bin/env python3
#
# Rigol DS1054Z Fast Fourier Transform
#
# This script downloads the samples from the oscilloscopes via LAN 
# and calulates the FFT
#
# This source file is part of the follwoing repository:
# http://www.github.com/microfarad-de/oscilloscope
#
# Please visit:
#   http://www.microfarad.de
#   http://www.github.com/microfarad-de
#
# Copyright (C) 2019 Karim Hraibi (khraibi at gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from ds1054z import DS1054Z
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.signal import hann


# Scope IP address
IP_ADDRESS = '192.168.2.4'


# Connect to scope
scope = DS1054Z(IP_ADDRESS)
print(scope.idn)


# Query the sample rate
sRate = float( scope.query(':ACQuire:SRATe?') )     # Sample rate

# Get the samples 
chan1 = scope.get_waveform_samples('CHAN1', 'RAW')  # Samples

n   = len(chan1)  # Number of samples = FFT size
w   = hann(n)     # Hanning window function
scs = sRate/n     # Sub-carrier spacing

#chan1 = np.linspace(1, 1, n)
#chan1 = np.random.normal(0.0001, 0.00005, size=n)

print('sRate = ' + str(sRate))
print('n     = ' + str(n) )
print('scs   = ' + str(scs) )

# Generate the values for the x-axis
x = np.linspace (0, n//2*scs, n//2)


# Calculate the FFT without the hanning window
#chan1F = fft(chan1)

# Calculate the FFT after applying the hanning window
chan1WF = fft(chan1*w)




# Plot using logarithmic scale
#plt.plot(chan1)
plt.semilogy( x, 2.0/n * np.abs(chan1WF[0:n//2]), '-b' )
#plt.semilogy( x, 2.0/n * np.abs(chan1F[0:n//2]), '-r' )
plt.grid()
plt.show()



