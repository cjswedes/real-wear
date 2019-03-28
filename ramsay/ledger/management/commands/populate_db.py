from django.core.management.base import BaseCommand
from ramsay.ledger.models import Ledger, Citation
import pandas

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        ledger_df = pandas.read_csv('example_ledger.csv')
        for index, entry in ledger_df.iterrows():
            citation = Citation(author=entry['author'],
                                book=entry['book'],
                                publisher=entry['publisher'])
            # TODO: there could possibly be more citations, but this script isnt checking them
            # fields: book2 author2, publisher2
            entry = Ledger(slug=entry['self'],
                           title=entry['title'],
                           artifact=entry['artifact'],
                           image=None, # TODO: actually load the image
                           materials=entry['materials'],
                           dimensions=entry['dimensions'],
                           date=entry['date'],
                           origin=entry['origin'],
                           distance=entry['distance'],
                           collection=entry['collection'],
                           link=entry['link'],
                           license=entry['license'],
                           license_link=entry['link2'],
                           department=entry['department'],
                           customer_first=entry['customer'].split(' ')[0],
                           customer_last=entry['customer'].split(' ')[1:],
                           page=entry['page'],
                           origin_description=entry['origin2'],
                           production_country=entry['production1'],
                           production_detail=entry['production2'],
                           description=entry['description'],
                           citation=citation,
                           quantity=entry['unit'],
                           orginal_price=entry['pounds'],
                           modern_pounds=entry['pounds2'],
                           modern_dollars=entry['dollars'],
                           analytics=entry['analytics'])
            try:
             entry.save()
            except:
             # if the're a problem anywhere, you wanna know about it
             print("there was a problem with line")



