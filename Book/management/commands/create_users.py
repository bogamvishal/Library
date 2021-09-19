from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = "Create randon users"

    def add_arguments(self, parser):
        parser.add_argument('total',type=int,help='No of users to be created')

    def handle(self, *args, **kwags):
        print(kwags)
        total = kwags['total']
        for i in range(total):
            s = get_random_string(6)
            User.objects.create_user(username = s,email = s+"@gmail.com",password='123')