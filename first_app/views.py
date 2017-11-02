from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccassRecord

def index(request):
    webpages_list = AccassRecord.objects.order_by('date')
    date_dict = {'acces_records': webpages_list}
    return render(request, 'first_app/index.html', context = date_dict)
