from rest_framework.serializers import HyperlinkedModelSerializer
from api.models import Manufacturer, ShoeColor, ShoeType, Shoe


class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('website', 'name')


class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('color_name',)


class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('style',)


class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type',
        ]