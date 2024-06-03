from django.shortcuts import render

def index(request):
    return render(request, 'things_to_do/index.html')

def activity_detail(request, activity):
    context = {'activity': activity}
    return render(request, f'things_to_do/{activity}.html', context)
