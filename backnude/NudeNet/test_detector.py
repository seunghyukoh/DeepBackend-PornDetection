# Import module
from nudenet import NudeDetector

# initialize detector (downloads the checkpoint file automatically the first time)
detector = NudeDetector() # detector = NudeDetector('base') for the "base" version of detector.
dic = detector.detect('test.jpg')

score = 0
count = 0
for part in dic:
    if part['score'] < 0.6:
        print(part['label'], "Porn")
        break
    else:
        print(part['label'], ':', part['score'])
