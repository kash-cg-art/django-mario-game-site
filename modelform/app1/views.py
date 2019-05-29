from django.shortcuts import render
from app1 import forms
from app1.models import feedback,mail
# Create your views here.

def index(request):
    formvar = forms.feedbackform()
    comment_list = feedback.objects.order_by('-date')
    count = comment_list.count()
    if request.method=='POST':
        formvar = forms.feedbackform(request.POST)
        if formvar.is_valid():
            human = True
            formvar.save(commit=True)
            return render(request,'app1/review.html',{'formvar':formvar,'comments':comment_list,'count':count})
    else:
        formvar = forms.feedbackform()
    return render(request,'app1/review.html',{'formvar':formvar,'comments':comment_list,'count':count})

def main(request):
    formvar = forms.mailform()
    if request.method=='POST':
        formvar = forms.mailform(request.POST)
        if formvar.is_valid():
            human = True
            formvar.save(commit=True)
            return render(request,'app1/home.html',{'formvar':formvar})
    else:
        formvar = forms.mailform()
    return render(request,'app1/home.html',{'formvar':formvar})

def contact(request):
    return render(request,'app1/contact.html')
