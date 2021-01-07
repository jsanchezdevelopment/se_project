from django.shortcuts import render
from home_get_data import home_get_data

def index(request):

  if 'step' in request.GET:
    sr = request.GET['step']
  else:
    sr = "StepResult"

  print(sr)
  data1,data2,header = home_get_data(sr)
  data1.sort()

  return render(request, 'main_template.html', {'data1':data1,'data2':data2,'header':header})
