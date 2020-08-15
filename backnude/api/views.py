from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import secrets
import json

import os
import sys
from keras import backend as K

from ..NudeNet.nudenet import NudeClassifier

# from ..NudeNet.porn_detection import classifier

class CheckPornView(APIView):
    def post(self, request):
        raw_data = request.body.decode('utf-8')
        data = json.loads(raw_data)
        print(data)
        path = data['path']
        os.chdir("/home/ubuntu/Server/DeepBackend/")

        if os.path.isfile(path) == False:
            return Response({"status":'Fail'}, status=400)
        
        
        K.clear_session()

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

        pred = "Porn" if pred > 0.5 else "Safe"

        response = Response({"status":pred}, status=200)

        return  response