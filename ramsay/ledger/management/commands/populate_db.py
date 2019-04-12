from django.core.management.base import BaseCommand
from ledger.models import Ledger, Citation, Product, Customer, Category
import pandas

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        ledger_df = pandas.read_csv('ledger/data/example_ledger.csv')
        for index, entry in ledger_df.iterrows():
            category = Category(name=entry['department'],
                                name_slug=entry['department'])
            citation = Citation(author=entry['author'],
                                book=entry['book'],
                                publisher=entry['publisher'])
            # TODO: there could possibly be more citations, but this script isnt checking them
            # fields: book2 author2, publisher2

            customer = Customer(first_name=entry['customer'].split(' ')[0],
                                last_name=entry['customer'].split(' ')[1],
                                occupation='baker')
            product = Product(title=entry['title'],
                    title_slug=entry['self'],
                    artifact=entry['artifact'],
                    image=None,  # TODO: actually load the image
                    materials=entry['materials'],
                    dimensions=entry['dimensions'],
                    origin=entry['origin'],
                    collection=entry['collection'],
                    link=entry['link'],
                    origin_description=entry['origin2'],
                    production_country=entry['production1'],
                    production_detail=entry['production2'],
                    materials_location=entry['materials2'],
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
                category.save()
                customer.save()
                citation.save()
            except Exception as exc:
                 # if the're a problem anywhere, you wanna know about it
                 print('Error saving customer: %s' % exc)
            try:
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
                ledger_entry.save()
            except Exception as exc:
                 # if the're a problem anywhere, you wanna know about it
                 print('Error saving ledger entry: %s' % exc)


