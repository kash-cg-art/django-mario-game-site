from django import forms
from app1.models import feedback,mail
from captcha.fields import CaptchaField

class feedbackform(forms.ModelForm):
    person = forms.CharField(label='Your Name')
    email = forms.EmailField(label='Your Email')
    comment = forms.CharField(widget=forms.Textarea,label='Review')
    captcha = CaptchaField()
    class Meta:
        model = feedback
        #fields = ('name','email','comment')
        fields = '__all__'

class mailform(forms.ModelForm):
    person = forms.CharField(label='Your Name')
    email = forms.EmailField(label='Your Email')
    captcha = CaptchaField()
    class Meta:
        model = mail
        #fields = ('name','email','comment')
        fields = '__all__'
