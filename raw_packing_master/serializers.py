from rest_framework import serializers
from . models import raw
from mode_master.models import mode



class rawlistSerializer(serializers.ModelSerializer):
    mode_name = serializers.CharField(max_length=100)
    

    class Meta:
    	model = raw
    	fields = ('id',
        'material_type',
        'material_name', 
        'purchase_name', 
        'purchase_date', 
        'factory_wise_bifercation', 
        'ex_factory_price', 
        'supplier_name', 
        'hsn_code',
        'gst',
        'price_after_gst',
        'transpoter',
        'freight',
        'cost_price',
        'mode_name',

       )


class rawSerializer(serializers.ModelSerializer):

    class Meta:
        model = raw
        fields = '__all__'



