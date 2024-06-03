
import os
from django.conf import settings
from django.shortcuts import render

def gallery(request):
    photos_dir = os.path.join(settings.BASE_DIR, 'photos/static/photos/gallery')
    photos = [f'photos/gallery/{filename}' for filename in os.listdir(photos_dir) if filename.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    return render(request, 'photos/gallery.html', {'photos': photos})