import numpy as np
from jenks import jenks
import sinegen

class Notelet():
    def __init__(self,frequency):
        self.frequency = frequency
        self.note = None

    def parent(self):
        return self.note


class Note():
    def __init__(self,notelets):
        self.notelets = notelets

    def num_notelets(self):
        return len(self.notelets)

    def frequency(self):
        return np.exp(np.mean([np.log(x.frequency) for x in self.notelets]))

    def amplitude(self):
        return 1 - np.exp(-self.notelets.__len__)


class Chord():
    def __init__(self,notelets):
        self.notelets = notelets
        self.notes = []
        gvf = 0.0
        nclasses = 2
        while gvf < .8:
            gvf, zone_indices = self.goodness_of_variance_fit(nclasses)
            nclasses += 1

        for zone in zone_indices:
            self.notes.append(Note([self.notelets[idx] for idx in zone]))

    def goodness_of_variance_fit(self, nclasses):
        array = [x.frequency for x in self.notelets]

        # get the break points
        classes = jenks(array, nclasses)

        # do the actual classification
        classified = np.array([self.classify(i, classes) for i in array])

        # max value of zones
        maxz = max(classified)

        # nested list of zone indices
        zone_indices = [[idx for idx, val in enumerate(classified) if zone + 1 == val] for zone in range(maxz)]

        # sum of squared deviations from array mean
        sdam = np.sum((array - np.mean(array)) ** 2)

        # sorted polygon stats
        array_sort = [np.array([array[index] for index in zone]) for zone in zone_indices]

        # sum of squared deviations of class means
        sdcm = sum([np.sum((classed - classed.mean()) ** 2) for classed in array_sort])

        # goodness of variance fit
        gvf = (sdam - sdcm) / sdam

        return gvf, zone_indices

    def classify(self,value,breaks):
        for i in range(1,len(breaks)):
            if value <= breaks[i]:
                return i
        return len(breaks)

    def sinWav(self):
        waves = []

        for note in self.notes:
            waves.append(sinegen.tone(note.frequency(), 5))

        return np.sum([wave/waves.__len__ for wave,phi in waves])
