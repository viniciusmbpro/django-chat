from django.shortcuts import render

# Create your views here.

def accounts_list(request):
    return render(request, 'accounts_list.html')

def accounts_detail(request):
    return render(request, 'accounts_detail.html')