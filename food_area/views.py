from django.shortcuts import render, HttpResponse
from food_area.models import Area
# Create your views here.
def food_area_name(request):
    area_name = Area.objects.all()
    template = 'food_area/food_area_name.html'
    context = {'area_name':area_name}
    return render(request, template,context)
