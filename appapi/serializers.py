from appapi.models import *
from rest_framework import serializers

class dataserializer(serializers.ModelSerializer):
	class Meta:
		model = SurveyData
 		fields = '__all__'