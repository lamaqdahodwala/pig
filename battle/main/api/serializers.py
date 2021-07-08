from ..models import Submission
from rest_framework.serializers import ModelSerializer


class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = ["name", "total", "r1", "r2", "r3", "r4", "r5"]
