from django.shortcuts import render


def home(request):
    """
    Landing page for Trendjack Hunter.

    Lightweight marketing/intro page that links into the trends dashboard.
    Kept separate from the dashboard itself so the dashboard can stay
    focused purely on data once we build it.
    """
    return render(request, 'core/home.html')
