from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/profile.html')
    
    
