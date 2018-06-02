from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework .response import Response
from . models import raw
from mode_master.models import mode
from . serializers import rawlistSerializer, rawSerializer
from rest_framework import viewsets, generics, status
from django.db import connection
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class rawList(APIView):
	def get(self, request):
		cursor = connection.cursor()
		cursor.execute("SELECT rpm.id,rpm.material_type,rpm.mode_id, rpm.material_name, rpm.purchase_name, rpm.factory_wise_bifercation, rpm.ex_factory_price, rpm.supplier_name, rpm.hsn_code,rpm.gst,rpm.purchase_date, rpm.price_after_gst,rpm.freight,rpm.cost_price,rpm.transpoter, mmm.mode_name from raw_packing_master_raw as rpm inner join mode_master_mode as mmm on rpm.mode_id = mmm.id ")
		columns = [column[0] for column in cursor.description]
		results = []
		roo = [ ]
		for row in cursor.fetchall():
			results.append(dict(zip(columns, row)))
		
		yo = []
		for r in results:
			t = {}
			members = { }
			t = r['mode_id']
			member = mode.objects.get(id=t)
			members['mode_name'] = member.mode_name
			yo.append(members)
		serializers = rawlistSerializer(yo, many=True)
		serializer = rawlistSerializer(results, many=True)
		return Response(serializer.data)
		return Response(serializers.data)

def delete(request, id):
    member = raw.objects.get(id=id)
    member.delete()		
		



class rawCreate(generics.CreateAPIView):
	lookup_field = 'pk'
	serializer_class = rawSerializer


	def get_queryset(self):
		return raw.objects.all()

class rawUp(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = rawSerializer


	def get_queryset(self):
		return raw.objects.all()

@method_decorator(csrf_exempt)
def get_place(request):
    
    if True:
        q = request.GET.get('q', '')
        places = raw.objects.filter(material_name__icontains=q)
        results = []
        for pl in places:
          place_json = { }  
          place_json ['id'] = pl.id
          place_json ['material_name'] = pl.material_name
          place_json ['cost_price'] = pl.cost_price
          place_json['material_type'] = pl.material_type
          results.append(place_json)
        content = json.dumps(results)
    else:
        content = 'fail'
    mimetype = 'application/json'
    return HttpResponse(content, mimetype)




