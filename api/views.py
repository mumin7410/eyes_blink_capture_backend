from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import base64
from . import face_recognition

# Create your views here.

@api_view(['POST'])
def receive_image(request):
    if request.method == 'POST':
        # Get the Base64 image data from the request
        base64_image = request.data.get('image')
        fr = face_recognition.FaceRecognition()
        result = fr.run_Facerecognition(base64_image)

        return Response({'message': result}, status=200)
    else:
        return Response({'error': 'Unsupported method'}, status=405)