# core/models.py

from django.db import models

class WalletAccess(models.Model):
    wallet_address = models.CharField(max_length=42, unique=True)
    label = models.CharField(max_length=100, blank=True, help_text="e.g. 'Judge 1', 'Demo user'")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.label or self.wallet_address} ({'active' if self.is_active else 'inactive'})"

    class Meta:
        verbose_name = "Wallet Access"
        verbose_name_plural = "Wallet Access List"