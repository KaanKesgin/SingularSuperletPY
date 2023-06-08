import numpy as np

def getWaveletTimeRange(Fc, Nc, Fs):
    resolution = int(np.abs(np.floor(np.log10(1/Fs))))-2
    t_edge = round(Nc/(2*Fc), resolution)*2.0
    return np.arange(-t_edge,t_edge,1/Fs) + (45e-2)/Fs


def normalize(wavelet, envelope, norm, Fc):
    if norm=="modulus-integral":
        return wavelet / np.sum( np.abs(envelope) )
    elif norm=="unit":
        return wavelet / np.max( np.abs(envelope) )
    elif norm=="frequency-sqrt":
        return wavelet * np.sqrt(Fc) / np.sum( np.abs(envelope) ) 
    elif norm=="frequency-square":
        return wavelet * Fc / np.sum( np.abs(envelope) ) 
    elif norm=="energy":
        return wavelet / np.sum( np.abs(envelope)**2 ) 
    else: #if norm is given none of the options above, still return modulus integral
        return wavelet / np.sum( np.abs(envelope) )
    
