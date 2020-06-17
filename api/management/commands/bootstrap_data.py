from django.core.management.base import BaseCommand, CommandError
from api.models import ShoeColor, ShoeType


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        shoechoices = ['sneaker', 'boot', 'sandal', 'dress', 'other']
        colorchoices = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'White', 'Black']
        for shoetype in shoechoices:
            ShoeType.objects.create(style=shoetype)

        for shoecolor in colorchoices:
            ShoeColor.objects.create(color_name=shoecolor)

