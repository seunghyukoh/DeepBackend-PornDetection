# Import module
from nudenet import NudeClassifier

# initialize classifier (downloads the checkpoint file automatically the first time)
classifier = NudeClassifier()

# Classify single image
# dic = classifier.classify('test.jpg')
# print(dic)
# Returns {'path_to_image_1': {'safe': PROBABILITY, 'unsafe': PROBABILITY}}
# Classify multiple images (batch prediction)
# batch_size is optional; defaults to 4

# classifier.classify(['path_to_image_1', 'path_to_image_2'], batch_size=BATCH_SIZE)
# # Returns {'path_to_image_1': {'safe': PROBABILITY, 'unsafe': PROBABILITY},
# #          'path_to_image_2': {'safe': PROBABILITY, 'unsafe': PROBABILITY}}

# # Classify video
# # batch_size is optional; defaults to 4
dic = classifier.classify_video('porn.mp4')
# print("\n\n\n")
# for key, value in dic['preds'].items():
#     print('프레임 {}의 결과 값은 {} 입니다'.format(key, value))

count = 0
num_frames = 0

for key, value in dic['preds'].items():
    if float(value['unsafe']) > 0.6:
        count += 1
    num_frames += 1

# print("count:{} num_frames:{}".format(count, num_frames))

prop = count / num_frames

print("\n", "Porn" if prop >= 0.5 else "Safe")

# # Returns {"metadata": {"fps": FPS, "video_length": TOTAL_N_FRAMES, "video_path": 'path_to_video'},
# #          "preds": {frame_i: {'safe': PROBABILITY, 'unsafe': PROBABILITY}, ....}}