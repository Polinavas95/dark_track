from django.contrib import admin
from .models import Track, ProcessingArea, Route, Tractor, Aggregator


@admin.register(Track)
class TractorTrackAdmin(admin.ModelAdmin):
    pass


@admin.register(ProcessingArea, Route)
class ShapeAdmin(admin.ModelAdmin):
    pass


@admin.register(Tractor)
class TractorAdmin(admin.ModelAdmin):
    pass


@admin.register(Aggregator)
class AggregatorAdmin(admin.ModelAdmin):
    pass