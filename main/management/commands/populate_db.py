from django.core.management.base import BaseCommand, CommandError
from main.models import Student, Grievance, Category
import pandas as pd

class Command(BaseCommand):
    help = 'Adds data in mentioned excel file to database'

    def handle(self, *args, **options):
        file_loc= '/home/vishesh/Downloads/Pycharm-master/nlp/sentdex_tutorial/grievances.xlsx'
        df = pd.read_excel(file_loc, sheetname="Sheet1", header=0, skiprows=0, index_col=None, parse_cols="A:B", converters={'Category':str})
        if(df is None) :
            print("Couldn't find file")
            return
        descriptions= list(df['Description'])
        categories= list(df['Category'])
        tatia= Student.objects.get_queryset().filter(name="Yash Tatia").first()
        if(tatia is None) :
            print("Couldn't find student")
            return
        for (desc,categ) in zip(descriptions, categories): 
            ctgs= categ.split(", ")
            grievance= Grievance.objects.create(student= tatia,description= desc)
            for ctg in ctgs:
                category= Category.objects.get_category_for(ctg)
                # print(category.first()) 
                grievance.categories.add(category.first())
            for ctg in grievance.categories.all() :
                grievance.actions.add(ctg.action)
            grievance.save()
            print(grievance)

        self.stdout.write(self.style.SUCCESS('Successfully added rows'))

