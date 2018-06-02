from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework .response import Response
from rest_framework import status
from . models import mode
from . serializers import modeSerializer, modeFileSerializer
from rest_framework import viewsets, generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from django.core.urlresolvers import reverse
from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.settings import api_settings
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
import csv
from rest_framework.parsers import FileUploadParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class modeList(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = modeSerializer


	def get_queryset(self):
		return mode.objects.all()
 
class modeCreate(generics.CreateAPIView):
	lookup_field = 'pk'
	serializer_class = modeSerializer


	def get_queryset(self):
		return mode.objects.all()


class modeUp(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = modeSerializer


	def get_queryset(self):
		return mode.objects.all()

class ModeFileUpload(APIView):
	queryset = mode.objects.all()
	serializer_class = modeSerializer
	parser_classes = (FormParser, MultiPartParser) # set parsers if not set in settings. Edited

	def perform_create(self, serializer):
		if request.method == 'POST':
			myfile = self.validated_data['file'] # access file
			print(myfile)
			fs = FileSystemStorage()
			BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.url(filename)
			reader = csv.reader(open(BASE_DIR + uploaded_file_url), dialect='excel', delimiter=",")
			count=0
			ro = []
			for row in reader:
				if count==0 :
					count=1
					continue
					r = mode()
				r.mode_name=row[0]
				ro.append(r)
				mode.objects.bulk_create(ro)   
			return Response(status=HTTP_200_OK)
		return Response(status=HTTP_400_BAD_REQUEST)

