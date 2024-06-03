from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from products.models import Favorite
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.views.decorators.csrf import csrf_exempt
 

@login_required
def index(request):
    # Fetch the user's favorites if they are logged in
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'dashboard/index.html', {'favorites': favorites})

@csrf_exempt
@login_required
def print_pdf_with_selection(request): 
    if request.method == "POST":
        selected_items = request.POST.getlist('selected_items')
        favorites = Favorite.objects.filter(id__in=selected_items, user=request.user)

        # Generate PDF TO DO FIX THISSS!!
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        y = height - 40
        for favorite in favorites:
            text = ""
            if favorite.itinerary:
                text = f"Itinerary: {favorite.itinerary.name}\n Details: {favorite.itinerary.details}\n"
            elif favorite.place_to_stay:
                text = f"Place to Stay: {favorite.place_to_stay.name}\n Description: {favorite.place_to_stay.description}\n"
            elif favorite.cultural_activity:
                text = f"Cultural Activity: {favorite.cultural_activity.name}\n Description: {favorite.cultural_activity.description}\n"
            elif favorite.blog_post:
                text = f"Blog Post: {favorite.blog_post.title}\nContent: {favorite.blog_post.content}\n"

            p.drawString(40, y, text)
            y -= 20
            if y < 40:
                p.showPage()
                y = height - 40

        p.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='favorites.pdf')

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
@login_required
def delete_selected_favorites(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('selected_items[]')
        for item_id in selected_items:
            favorite = get_object_or_404(Favorite, id=item_id, user=request.user)
            favorite.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})