from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

from yolov5.detectv3 import detect

@gzip.gzip_page
def detectme(request):
    try:
   
        return StreamingHttpResponse(detect(), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass