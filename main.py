import pyaudio
import sinegen
from notelets import *

a = Chord([Notelet(440),
           Notelet(441),
           Notelet(443),
           Notelet(885),
           Notelet(1280),
           Notelet(1370),
           Notelet(1290),
           Notelet(1302),
           Notelet(890),
           Notelet(880)])


sampRate = 44100

p = pyaudio.PyAudio()

stream = p.open(format = pyaudio.paFloat32,
                channels = 1,
                rate = sampRate,
                output = True)

stream.write(a.sinWav().tostring())

stream.close()
