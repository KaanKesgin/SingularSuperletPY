import numpy as np

def generateComplexBursts(duration, numPackets, freqs, cLen, amp, Fs):
    t = np.arange(0,duration,1/Fs)
    y = np.zeros(len(t), dtype=float)
    for i in range(numPackets):
        burstFrequency = np.random.choice(freqs) #randomly sample from the given frequency range
        burstDuration = np.random.choice(cLen)*int(Fs//burstFrequency) #generate a random duration with respect to number of cycles
        while burstDuration>=len(t):
            burstFrequency = np.random.choice(freqs)
            burstDuration = np.random.choice(cLen)*int(Fs//burstFrequency)
        burstStart = np.random.choice(len(t)-burstDuration) #make sure the starting point for the burst does not cause exeeding the duration of the signal
        burst = np.random.choice(amp)*np.sin(2*np.pi*burstFrequency*t)[burstStart:burstStart+burstDuration-1] #create the burst
        y[burstStart:burstStart+burstDuration-1] += burst # sum the burst to the data
    return y
  
