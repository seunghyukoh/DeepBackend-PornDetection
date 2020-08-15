import os
import sys

from .nudenet import NudeClassifier

def classifier(path):
    
    assert(path != None)
    
    if os.path.isfile(path) == False:
        return None

    nude_classifier = NudeClassifier()

    dic_result = nude_classifier.classify_video(path)

    count = 0
    num_frames = 0
    print(path, "got result")
    for key, value in dic_result['preds'].items():
        if float(value['unsafe']) > 0.6:
            count += 1
        num_frames += 1
        # print(count)

    pred = count / num_frames
    
    return True if pred > 0.5 else False