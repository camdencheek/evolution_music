import numpy as np


def tone(frequency, duration, sampRate=44100, amplitude=1, phi_0=0):

    """ frequency   - frequency of tone in Hertz
        duration    - duration of tone in seconds
        sampRate    - sample rate of tone in Hertz
        phi_0       - initial phase angle of sine wave """

    time = np.linspace(0,duration,num=duration*sampRate)
    phi_t = time*frequency*2*np.pi + phi_0
    phi_t = phi_t[1:]
    wave = np.sin(phi_t,dtype='float32') * amplitude
    phi_final = phi_t[-1] % 2*np.pi

    return wave, phi_final

def sweep(f_start,f_end,duration,sampRate=44100,amplitude=1,phi_0=0):
    time = np.linspace(0,duration,num=sampRate*duration)
    phi_t = phi_0 + 2*np.pi*f_start*duration*np.log(f_end/f_start)*\
        ((f_end/f_start)**(time/duration) - 1)
    phi_t = phi_t[1:]
    wave = np.sin(phi_t,dtype='float32') * amplitude
    phi_final = phi_t[-1] % (2*np.pi)

    return wave, phi_final
