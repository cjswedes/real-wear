from django.shortcuts import render

from ledger.models import Product
# Create your views here.
from django.views import generic
from django.core.serializers.json import DjangoJSONEncoder
import json

class GlobeListView(generic.ListView):
    model       = Product
    template_name = 'globe.html'

    def get(self, request, *args, **kwargs):
        pquery = Product.objects.all().values_list('production_longitude', 'production_latitude')
        mquery = Product.objects.all().values_list('materials_latitude', 'materials_longitude')
      
        pjson = json.dumps(list(pquery), cls=DjangoJSONEncoder)
        mjson = json.dumps(list(mquery), cls=DjangoJSONEncoder)
        return render(request, self.template_name, {'pjson': pjson, 'mjson': mjson})