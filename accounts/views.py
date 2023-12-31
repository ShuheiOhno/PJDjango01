from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser
from accounts.forms import ProfileForm, SignupUserForm
from allauth.account import views

#ログイン用
class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')
    
class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'
    form_class = SignupUserForm


#プロフィール
class ProfileView( LoginRequiredMixin ,View):
    def get(self, request, *args, **kwargs):
        #ログイン中ユーザーの取得
        user_data = CustomUser.objects.get(id=request.user.id)

        return render(request, 'accounts/profile.html', {
            'user_data': user_data,
        })
    
class ProfileEditView( LoginRequiredMixin ,View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        form_data = ProfileForm(
            request.POST or None,
            initial= { #初期値
                'first_name': user_data.first_name,
                'last_name': user_data.last_name,
                'department': user_data.department,
                'image': user_data.image,
            }
        )

        return render(request, 'accounts/profile_edit.html', {
            'form': form_data,
            'user_data': user_data,
        })
    
    def post(self, request, *args, **kwargs):
        form_data = ProfileForm(request.POST or None)
        if form_data.is_valid():
            user_data = CustomUser.objects.get(id=request.user.id)
            user_data.first_name = form_data.cleaned_data['first_name']
            user_data.last_name = form_data.cleaned_data['last_name']
            user_data.department = form_data.cleaned_data['department']
            if request.FILES.get('image'):
                user_data.image = request.FILES.get('image')
            user_data.save()
            return redirect('profile')
        
        return render(request, 'accounts/profile.html', {
            'form': form_data
        })
   