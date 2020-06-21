from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from PIL import Image
import io


# Create your views here.
def index(request):
    return HttpResponse(request, "hi there")


class SendImage(APIView):
    @staticmethod
    def check_validity(req):
        ret = True
        message = ""
        keys = [w for w in req.keys()]
        if "image" not in keys:
            ret = False
            message += "image is not appended, " \
                       "try appending the image in header files with key 'image', please refer to " \
                       "https://github.com/santhtadi/rest_api_in_django " \
                       "for more details ; "
        return ret, message

    # post is responsible for receiving files
    # develop det put and delete according to your need
    def post(self, request):
        # print the data in request to dashboard
        print(request.data)
        # convert the request data to a dictionary object in python
        req = dict(request.data)
        # check if all the required files are appended or not
        valid, error_message = self.check_validity(req)
        if not valid:
            return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)
        # read the image as bytes
        by = req['image'][0].read()
        # convert bytes as image using pillow library
        img = Image.open(io.BytesIO(by)).convert('RGB')
        # create an array using numpy
        image_in_rgb_format = np.array(img)
        # change RGB to BGR format for using with opencv library
        image_in_opencv_format = image_in_rgb_format[:, :, ::-1].copy()
        # returning size of image as output
        return Response({"image_size": image_in_opencv_format.shape}, status=status.HTTP_200_OK)
