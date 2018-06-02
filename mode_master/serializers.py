from rest_framework import serializers
from . models import mode

class modeSerializer(serializers.ModelSerializer):

	class Meta:
		model = mode
		fields = ('id','mode_name', 'created_date', 'modify_date')

class modeFileSerializer(serializers.ModelSerializer):

	class Meta:
		model = mode
		fields = ('mode_name')




