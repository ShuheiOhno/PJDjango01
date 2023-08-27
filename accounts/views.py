from django.shortcuts import render, redirect
from django.views import View
from accounts.models import CustomUser

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        #ログイン中ユーザーの取得
        user_data = CustomUser.objects.get(id=request.user.id)

        return render(request, 'accounts/profile.html', {
            'user_data': user_data,
        })