from django.core.management.base import BaseCommand
from ledger.models import Ledger, Citation, Product, Customer, Category
import pandas

from django.core.files import File
import os
import random




class Command(BaseCommand):
    #args = '<foo bar ...>'
    #help = 'our help string comes here'
    def add_arguments(self, parser):
        parser.add_argument( 
            '--debug', 
            action='store_true',
            help='Run command without saving items. Used for testing.',)
    def handle(self, *args, **options):
        ledger_df = pandas.read_csv('ledger/data/example_ledger.csv', encoding='latin1')
        fake = options['debug']

        customer_choices = ['chef', 'landowner', 'slave', 'merchant', 'blacksmith', 'farmer', 'tailor']

        for index, entry in ledger_df.iterrows():
            if fake:
                print("row: %d" % index)
            category = Category(name=entry['department'],
                                name_slug=entry['department'])
            citation = Citation(author=entry['author'],
                                book=entry['book'],
                                publisher=entry['publisher'])
            # TODO: there could possibly be more citations, but this script isnt checking them
            # fields: book2 author2, publisher2




            customer = Customer(first_name=entry['customer'].split(' ')[0],
                                last_name=entry['customer'].split(' ')[1],
                                occupation=random.choice(customer_choices))
            pcoord = str(entry['ProductionCoordinates'])
            mcoord = str(entry['MaterialsCoordinates'])
            if pcoord == 'nan':
                pcoord = ','
            elif mcoord == 'nan':
                mcoord = ','
            ptokens = pcoord.split(',')
            mtokens = pcoord.split(',')
            def coordinate_clean(token):
                if token == '':
                    return 0.0
                token = token.replace(u'\N{DEGREE SIGN}', '')
                cleaned = float(token.strip('NSEW'))
                if 'S' in token:
                    cleaned = -1.0*cleaned
                elif 'W' in token:
                    cleaned = -1.0*cleaned
                return cleaned

            pclean = list(map(coordinate_clean, ptokens))
            mclean = list(map(coordinate_clean, mtokens))

            if fake:
                print("\t" + str(pclean))
                print("\t" + str(mclean))
                print("\t" + str(os.path.join('ledger/data/', entry['image'])))

            product = Product(title=entry['title'],
                    title_slug=entry['self'],
                    artifact=entry['artifact'],
                    image=File(open(os.path.join('ledger/data/', entry['image']), 'rb')),
                    materials=entry['materials'],
                    dimensions=entry['dimensions'],
                    #origin=entry['origin'],
                    collection=entry['collection'],
                    link=entry['link'],
                    origin_description=entry['origin2'],
                    production_country=entry['production1'],
                    production_city=entry['production2'],
                    production_latitude=pclean[0],
                    production_longitude=pclean[1],
                    materials_latitude=mclean[0],
                    materials_longitude=mclean[1],
                    #materials_location=entry['materials2'],
                    description=entry['description'],
                    license=entry['license'],
                    license_link=entry['link2'],
                    original_price=entry['pounds'],
                    modern_pounds=entry['pounds2'],
                    modern_dollars=entry['dollars'],
                    page=entry['page'],
                    quantity=entry['unit'],
                    category=category)

            try:
                if not fake:
                    category.save()
                    customer.save()
                    citation.save()
            except Exception as exc:
                 # if the're a problem anywhere, you wanna know about it
                 print('Error saving customer: %s' % exc)
            try:
                if not fake:
                    product.save()
            except Exception as exc:
                # if the're a problem anywhere, you wanna know about it
                print('Error saving citation: %s' % exc)

            ledger_entry = Ledger(date=entry['date'],
                                  analytics=entry['analytics'],
                                  customer=customer,
                                  product=product,
                                  citation=citation

                                                  # distance=entry['distance'],
                                                  # department=entry['department']
                                  )

            try:
                if not fake:
                    ledger_entry.save()
            except Exception as exc:
                 # if the're a problem anywhere, you wanna know about it
                 print('Error saving ledger entry: %s' % exc)


