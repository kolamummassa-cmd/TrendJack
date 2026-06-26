from django.db import models


class Article(models.Model):
    """
    A single news/blog article pulled in from an RSS feed.

    This is the raw evidence layer of the pipeline. Nothing here is AI
    generated — it's just what the source published. Trend detection later
    reads across many Articles to find recurring topics.
    """

    title = models.CharField(
        max_length=500,
        help_text="Article headline, as published by the source.",
    )
    source = models.CharField(
        max_length=150,
        help_text="Human-readable source name, e.g. 'TechCrunch', 'Google News'.",
    )
    url = models.URLField(
        max_length=1000,
        unique=True,
        help_text="Canonical article URL. Unique — used as the dedupe key on ingestion.",
    )
    summary = models.TextField(
        blank=True,
        help_text="RSS description/snippet. Short summary, not full article text.",
    )
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When the source published this article (from RSS feed metadata).",
    )
    raw_content = models.TextField(
        blank=True,
        help_text="Optional fuller text content, if the feed provides more than a snippet.",
    )
    matched_keywords = models.CharField(
        max_length=500,
        blank=True,
        help_text=(
            "Comma-separated keywords/phrases this article was matched to during "
            "trend detection. Filled in by the detect_trends command, not on ingestion."
        ),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="When this article was ingested into our database (not published date).",
    )

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return f"{self.title[:60]} ({self.source})"
