from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from main.final import retrain_multilabelbinarizer_model, make_query_post
from main.models import grievances

class Command(BaseCommand):
    help = 'Adds data in mentioned excel file to database'

    def handle(self, *args, **options):
        file_loc= '/home/vishesh/Downloads/Pycharm-master/nlp/sentdex_tutorial/grievances.xlsx'
        
        

        self.stdout.write(self.style.SUCCESS('Successfully added rows'))
