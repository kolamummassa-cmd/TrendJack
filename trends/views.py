from django.shortcuts import render, get_object_or_404
from django.db.models import Count

from trends.models import Trend
from core.models import WalletAccess


def dashboard(request):
    """
    Main dashboard: lists all detected trends as cards, with sorting and
    filtering controls. This is the "startup intelligence" home screen —
    designed to answer "what should we make content about right now?"
    at a glance.

    Query params:
        sort: 'trend_score' (default), 'relevance_score', or 'created_at'
        status: filter by Trend.STATUS_CHOICES value, or 'all' (default)
        min_relevance: integer, only show trends >= this relevance score
    """
    sort = request.GET.get("sort", "trend_score")
    status = request.GET.get("status", "all")
    min_relevance = request.GET.get("min_relevance", "")

    sort_field_map = {
        "trend_score": "-trend_score",
        "relevance_score": "-relevance_score",
        "created_at": "-created_at",
    }
    order_by = sort_field_map.get(sort, "-trend_score")

    trends = Trend.objects.all().select_related("brief")

    if status in dict(Trend.STATUS_CHOICES):
        trends = trends.filter(status=status)

    if min_relevance.isdigit():
        trends = trends.filter(relevance_score__gte=int(min_relevance))

    trends = trends.order_by(order_by)

    context = {
        "trends": trends,
        "current_sort": sort,
        "current_status": status,
        "current_min_relevance": min_relevance,
        "status_choices": Trend.STATUS_CHOICES,
        "total_count": trends.count(),
        "briefed_count": trends.filter(status=Trend.STATUS_BRIEFED).count(),
    }
    return render(request, "trends/dashboard.html", context)


# In trends/views.py — update the trend_detail view




def trend_detail(request, pk):
    trend = get_object_or_404(Trend, pk=pk)
    brief = getattr(trend, 'brief', None)

    # Check wallet access
    wallet_address = request.GET.get('wallet', '').strip()
    has_access = False

    if wallet_address:
        has_access = WalletAccess.objects.filter(
            wallet_address__iexact=wallet_address,
            is_active=True
        ).exists()

    return render(request, "trends/trend_detail.html", {
        "trend": trend,
        "brief": brief,
        "has_access": has_access,
    })
