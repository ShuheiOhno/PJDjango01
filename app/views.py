from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import Staff, Store

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

class StaffView(View):
    def get(self, request, *args, **kwargs):
        store_data = get_object_or_404(Store, id=self.kwargs['pk'])
        staff_data = Staff.objects.filter(store=store_data).select_related('user')

        return render(request, 'app/staff.html', {
            'store_data': store_data,
            'staff_data': staff_data,
        })