from django import forms 
from django.contrib.auth import (
	authenticate,
	get_user_model
)

User = get_user_model()


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
			user = User.objects.filter(username=username).first()
			if not user:
				raise forms.ValidationError('This user does not exist')
			if not user.check_password(password):
				raise forms.ValidationError('Incorrect password')
			user = authenticate(username=username, password=password)
			if not user or not user.is_active:
				raise forms.ValidationError('This user is not active')
		return super(UserLoginForm, self).clean(*args, **kwargs)		