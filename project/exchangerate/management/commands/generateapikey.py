from django.core.management.base import BaseCommand, CommandError
from rest_framework_api_key.models import APIKey

class Command(BaseCommand):
    help = 'Creates an API Key using terminal'

    def add_arguments(self, parser):
        parser.add_argument('key_names', nargs='+', type=str)

    def handle(self, *args, **options):
        for key_name in options['key_names']:
            api_key, key = APIKey.objects.create_key(name=str(key_name))

            self.stdout.write(self.style.SUCCESS(key))
