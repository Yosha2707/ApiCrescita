from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework .response import Response
from rest_framework import status
from . models import cost, costpack
from raw_packing_master.models import raw 
from . serializers import manuSerializer, manu2Serializer, ManuSerializer
from django.db import connection
from rest_framework import viewsets, generics
import itertools 


  

class manuList(APIView):

	def get(self, request):
		cursor = connection.cursor()
		cursor.execute("SELECT mcp.id, mcp.product_name, mcp.product_code, mcp.factory_name, mcp.pack_size, mcp.mrp_per, mcp.mrp_price, mcp.margin_per, mcp.margin_amount, ROUND(((((mcp.rawmultiplier*rpm.cost_price)/(mcp.rawmultiplier-(mcp.wastage*mcp.rawmultiplier/100)))*mcp.rawmultiplier)+ table_pack.fpc) + (mode_master_head.factory*((((mcp.rawmultiplier*rpm.cost_price)/(mcp.rawmultiplier-(mcp.wastage*mcp.rawmultiplier/100)))*mcp.rawmultiplier)+ table_pack.fpc)/100) + (mcp.overall_wastage*((((mcp.rawmultiplier*rpm.cost_price)/(mcp.rawmultiplier-(mcp.wastage*mcp.rawmultiplier/100)))*mcp.rawmultiplier)+ table_pack.fpc)/100),4) as totalcost, ROUND((mcp.margin_amount + ((((mcp.rawmultiplier*rpm.cost_price)/(mcp.rawmultiplier-(mcp.wastage*mcp.rawmultiplier/100)))*mcp.rawmultiplier)+ table_pack.fpc) + (mode_master_head.factory*((((mcp.rawmultiplier*rpm.cost_price)/(mcp.rawmultiplier-(mcp.wastage*mcp.rawmultiplier/100)))*mcp.rawmultiplier)+ table_pack.fpc)/100) + (mcp.overall_wastage*((((mcp.rawmultiplier*rpm.cost_price)/(mcp.rawmultiplier-(mcp.wastage*mcp.rawmultiplier/100)))*mcp.rawmultiplier)+ table_pack.fpc)/100)), 4) as dealerprice fROM manufacturing_cost_master_cost as mcp inner join raw_packing_master_raw as rpm on mcp.raw_id = rpm.id inner join mode_master_head left join (SELECT cost_id , ifnull(SUM(rpm.cost_price*mccp.multipliar), 0) as fpc from manufacturing_cost_master_costpack as mccp left join raw_packing_master_raw as rpm on mccp.packing_id = rpm.id group by mccp.cost_id) as table_pack on table_pack.cost_id=mcp.id")
		columns = [column[0] for column in cursor.description]
		results = []
		roo = [ ]
		for row in cursor.fetchall():
			results.append(dict(zip(columns, row)))
		for r in results:
			tt = {}
			tt['totalcost'] = r['totalcost']
			tt['dealerprice'] = r['dealerprice']
			roo.append(tt)
	

		
		serializers = manuSerializer(roo, many=True)
		serializer = manuSerializer(results, many=True)
		return Response(serializer.data)
		return Response(serializers.data)


 
class ManuUp(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = ManuSerializer

	def get_queryset(self):
		return cost.objects.all() 
	

