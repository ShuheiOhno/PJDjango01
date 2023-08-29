from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from app.models import Store

# Create your views here.
class IndexView(TemplateView):
    template_name = 'app/index.html'
    login_url = '/account/login/'

class StoreView(View):
    def get(self, request, *args, **kwargs):
        store_data = Store.objects.all()

        return render(request, 'app/store.html', {
            'store_data': store_data,
        })

