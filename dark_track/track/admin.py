from django.contrib import admin
from .models import TractorTrack


class TractorTrackInline(admin.TabularInline):
    model = TractorTrack


class TractorTrackAdmin(admin.ModelAdmin):
    inlines = [
        TractorTrackInline,
    ]


admin.site.register(TractorTrack, TractorTrackAdmin)