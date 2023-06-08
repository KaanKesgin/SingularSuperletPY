import numpy as np
import matplotlib.pyplot as plt

import generateData  # for generating data
import sst # for wavelet functions - will be replaced after development since direct import is not necessary in this script
import cwt # for wavelet functions - will be replaced after development since direct import is not necessary in this script

if __name__ == "__main__":

    # parameters for generating complex bursts
    numPackets = 50                       # generate numPackets amount of randomly positioned random bursts
    duration   = 0.05                     # for the total duration of duration (in seconds)
    freqs      = np.arange(1,1500,1)      # with frequencies sampled from freqs (in Hz)
    cLen       = np.arange(1,5,1)         # number of cycles sampled from cLen
    amp        = np.arange(1,5,1)         # amplitudes sampled from amp
    Fs         = 30000.0                  # sampling rate of the input data (Hz)

    #generate the data based on parameters above or load your own data
    y = generateData.generateComplexBursts(duration, numPackets, freqs, cLen, amp, Fs)


    # parameters for time frequency analysis
    frange    = np.arange(1,2000,1)       # frequency range of interest for performing the time frequency decomposition
    norm      = "frequency-sqrt"          # normalization to be used
    step      = 250.0                     # adaptive parameter for number of cycles increment per frequency band
    baseCycle = 3.0                       # number of baseline cycles to build the adaptive increments on 


    sstRez = sst.sst(y, frange, Fs, baseCycle, norm, step)
    cwtRez = cwt.cwt(y, frange, Fs, baseCycle, norm, step)


    #plotting
    t = np.arange(0,len(y)/Fs,1/Fs) # time variable for plotting the time data (in seconds)


    fig, axs = plt.subplots(3,1, sharex=True, figsize=(12, 8))
    # plot time data
    axs[0].plot(np.arange(len(y)), y)
    axs[0].set_title("time")

    ###########################################

    # plot time frequency decomposition heatmaps
    showEveryX = int(len(t)//10)
    showEveryY = int(len(frange)//5)

    axs[1].imshow(sstRez, cmap='jet', interpolation='nearest')
    axs[1].set_xticks(np.arange(0, len(t), showEveryX), labels= np.round(1000*t[::showEveryX]).astype(int))
    axs[1].set_yticks(np.arange(0, len(frange), showEveryY), labels=frange[::showEveryY])
    axs[1].set_aspect('auto')
    axs[1].set_ylabel("freq (Hz)")
    axs[1].set_title("sst")

    ##########################################

    axs[2].imshow(cwtRez, cmap='jet', interpolation='nearest')
    axs[2].set_xticks(np.arange(0, len(t), showEveryX), labels= np.round(1000*t[::showEveryX]).astype(int))
    axs[2].set_yticks(np.arange(0, len(frange), showEveryY), labels=frange[::showEveryY])
    axs[2].set_aspect('auto')
    axs[2].set_xlabel("time (ms)")
    axs[2].set_ylabel("freq (Hz)")
    axs[2].set_title("cwt")

    plt.show()
    # plt.savefig("C:\\Users\\kesgi\\Desktop\\githubThings\\SingularSuperletTransform\\code\\Python\\my_plot2.png", dpi=300)
