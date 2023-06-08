import numpy as np
import SingularSuperletPY.waveletHelper # for wavelet functions

def singularSuperlet(Fc, Nc, Fs, norm):
    t = waveletHelper.getWaveletTimeRange(Fc, Nc, Fs) # get the time range where the wavelet is defined
    timeCancelFactor = (1/(Nc/(2*Fc)))**2

    envelope =  ( -np.log( timeCancelFactor * t**2 ) ) * np.exp( -(timeCancelFactor * t**2 )**( 2*np.log(Nc) )  )
    wavelet = envelope * np.exp(1j * 2*np.pi*Fc * t)

    return waveletHelper.normalize(wavelet, envelope, norm, Fc)


# perform SST on the input data (y), at frequencies (frange), sampling frequency (Fs) and normalisation
def sst(y, frange, Fs, baseCycle, norm, step):
    N, M = len(y), len(frange) # get N points from the input data and M frequency points for correct number of points operations    
    scalogram = np.zeros((M, N), dtype=float) # N points in time, M points in frequency

    for i in range(M):
        o = 1.0 + frange[i]/step # number of cycles increase factor per frequency
        w = singularSuperlet(frange[i], baseCycle*o, Fs, norm) # generate the wavelet
        lenW = len(w)
        scalogram[i,:] =  2 * np.abs( np.convolve(y, w, 'full')[lenW//2 -1 : -lenW//2] )**2 #apply convolution operation and correct for the resultant size
    
    return scalogram #rotate from time*frequency to frequency*time (helps heatmap plotting)
