from rest_framework import serializers
from . models import cost, costpack
from raw_packing_master.models import raw


class manuSerializer(serializers.ModelSerializer):
	
	totalcost = serializers.CharField(max_length=100)
	dealerprice = serializers.CharField(max_length=100)

	class Meta:
		model = cost
		fields = ('id','product_name', 'product_code', 'factory_name','totalcost','dealerprice', 'pack_size', 'margin_per', 'margin_amount', 'mrp_per', 'mrp_price')


class rawSerializers(serializers.ModelSerializer):
	class Meta:
		mode = raw
		fields = ('cost_price')

class manu2Serializer(serializers.ModelSerializer):
	#k = manuSerializer(many=True, read_only=False)
	#l = rawSerializers(many=True, read_only=False)
	
	class Meta:
		model = cost
		fields='__all__'
	class Meta:
		model = cost
		fields='__all__'	

class ManuSerializer(serializers.ModelSerializer):

    class Meta:
        model = cost
        fields = '__all__'