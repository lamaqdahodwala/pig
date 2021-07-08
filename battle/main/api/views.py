from .serializers import SubmissionSerializer
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response

class SubmitGameView(APIView):
    def post(self, req):
        ser = SubmissionSerializer(data=req.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=HTTP_201_CREATED)