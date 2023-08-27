from django import forms
from allauth.account.forms import SignupForm

class SignupUserForm(SignupForm):
    #サインアップ時に必要なフォーム
    first_name = forms.CharField(max_length=50, label='姓')
    last_name = forms.CharField(max_length=50, label='名')
    print('aaa')

    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        print(user)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='姓')
    last_name = forms.CharField(max_length=50, label='名')
    department = forms.CharField(max_length=50, label='所属', required=False)