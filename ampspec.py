# -*- coding: utf-8 -*-

"""
Created on Tue Dec  1 08:19:50 2015

@author: AhrensJH
"""

"""
function [mag, freq] = ampspec(X, Ts)

for k = 1:1:size(X, 2)
    x = detrend(X{k});
    Fs = 1/Ts;
    xdft = fft(x, 1e4);
    xdft = xdft(1:length(xdft)/2+1);
    xdft = 1/length(x).*xdft;
    xdft(2:end-1) = 2*xdft(2:end-1);
    freq = 0:Fs/(2*length(xdft)-1):Fs/2;
    mag(:, k) = abs(xdft);
    freqhrs(:, k) = 3600*freq';
end
"""

import matplotlib.pyplot as plt
import numpy as np

def ampspec(x, Ts, title=None):       
    # Single Sided Amplitude Specturm
    x = x - np.mean(x)
    Fs = 1/Ts
    xdft = np.fft.fft(x)
    xdft = xdft[0:int(len(xdft)/2+2)]
    xdft = xdft/len(x)
    xdft[1:-1] = 2*xdft[1:-1]
    freq = np.linspace(0, Fs/2, len(xdft))
    mag = np.abs(xdft)
    freqhrs = 3600*freq
    
    plt.plot(freqhrs, mag)
    title = 'Amplitude Specturm - ' + title
    plt.title(title)
    plt.xlabel('Hours^-1')
    plt.ylabel('|Y(t)|')
