# SingularSuperletPY
 Python repo for [Singular Superlet Transform](https://github.com/KaanKesgin/SingularSuperletTransform) (SST)

The Singular Superlet Transform (SST) is a time-frequency decomposition method based on wavelet transform that can generate highly localised spectra.

_Please cite our research paper using when using SST in your research project._
> Jorntell, Henrik, and Kaan Kesgin. "Singular superlet transform achieves markedly improved time-frequency super-resolution for separating complex neural signals." bioRxiv (2023): 2023-02


Quickstart 
============
You can git clone or download this repository, then add execute run.py for a quick start and a comparison with CWT using randomly generated data.

Or simply Install the Python package using pip:
```
$ pip install SingularSuperletPY
```
Once the installation is successful you can test it on your own data as following:

```Python
#import required packages
import numpy as np
import matplotlib.pyplot as plt

#import the functions
from SingularSuperletPY import sst
# from SingularSuperletPY import cwt #uncomment if you want to compare the method (SST) with continuous wavelet transform (CWT)

filename = "\path\to\your\data"   # define the path to your data
y        = np.load(filename)	  # load your data
Fs       = 1000.0                 # define sampling rate in Hz, replace with the sampling rate of your file

# define parameters for singular superlet transform, consult the research paper above for further details
frange    = np.arange(1,2000,1)   # frequency range of interest for performing the time frequency decomposition
norm      = "frequency-sqrt"      # normalization to be used, options are: "modulus-integral", "unit", "frequency-sqrt" and "energy". Check the function normalize in waveletHelper.py for further details
step      = 250                   # adaptive parameter for number of cycles increment per frequency band
baseCycle = 3                     # number of baseline cycles to build the adaptive increments on 

# perform time frequency decomposition
sstRez = sst.sst(y, frange, Fs, baseCycle, norm, step) # perform sst,  returns the scalogram output that is frequencyPoints x timePoints
# cwtRez = cwt.cwt(y, frange, Fs, baseCycle, norm, step) # perform cwt,  uncomment if you wish to make comparisons with cwt, returns the scalogram output that is frequencyPoints x timePoints

```
![](https://github.com/KaanKesgin/SingularSuperletPY/blob/main/SingularSuperletPY/my_plot.png)

- High performance Julia implementation [under development](https://github.com/KaanKesgin/SingularSuperletJL.jl)
- MATLAB version [available](https://github.com/KaanKesgin/SingularSuperletMAT)
