

from django.contrib import admin
from .models import WalletAccess

@admin.register(WalletAccess)
class WalletAccessAdmin(admin.ModelAdmin):
    list_display = ["wallet_address", "label", "is_active", "created_at"]
    search_fields = ["wallet_address", "label"]
    list_filter = ["is_active"]