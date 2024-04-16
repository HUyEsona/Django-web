from django.shortcuts import render

def homepage(request):
    # Xử lý logic cho trang chủ ở đây
    return render(request, 'home.html')

def trang_chu_page(request):
    return render(request, 'trang_chu.html')

def san_pham_page(request): 
    return render(request, 'san_pham.html')

def gio_hang_page(request):
    return render(request, 'gio_hang.html')

def about_page(request):
    
    return render(request, 'about.html')

def lien_he_page(request):
    #
    return render(request, 'lien_he.html')