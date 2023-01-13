from django.core.management.base import BaseCommand, CommandError
from ._helpers import get_forecast

class Command(BaseCommand):
    help = 'Obtain the latest conditions from the UBC Weather Station'

    def handle(self, *args, **options):
        get_forecast()