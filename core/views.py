

import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import WalletAccess


def home(request):
    return render(request, "core/home.html")


@csrf_exempt
@require_POST
def check_wallet(request):
    """
    Receives a wallet address from the frontend,
    checks if it's on the whitelist,
    and returns access status as JSON.
    """
    try:
        data = json.loads(request.body)
        address = data.get("address", "").strip().lower()

        if not address:
            return JsonResponse({"access": False, "message": "No wallet address provided."})

        has_access = WalletAccess.objects.filter(
            wallet_address__iexact=address,
            is_active=True
        ).exists()

        if has_access:
            return JsonResponse({"access": True, "message": "Access granted."})
        else:
            return JsonResponse({"access": False, "message": "Wallet not on access list."})

    except Exception as e:
        return JsonResponse({"access": False, "message": str(e)})