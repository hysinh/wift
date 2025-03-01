from django.shortcuts import render


def display_404(request, exception):
    """
    Displays a custom 404 error page
    """
    return render(request, "errors/404.html", status=404)


def display_500(request):
    """
    Displays a custom 500 error page
    """
    return render(request, "errors/500.html", status=500)
