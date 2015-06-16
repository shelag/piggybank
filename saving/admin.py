from django.contrib import admin
from .models import Movement, Tag


class MovementAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text', 'amount', 'currency', 'owner']}),
        ('', {'fields': ['tag']}),
        ('Date information', {'fields': ['date_pub'], 'classes': ['collapse']}),
    ]
    list_display = ('text', 'amount', 'date_pub')
    list_filter = ['date_pub', 'text']
    date_hierarchy = 'date_pub'
    search_fields = ['text']
    filter_horizontal = ['tag']


class TagAdmin(admin.ModelAdmin):
    """docstring for TagAdmin"""
    model = Tag
    list_display = ['slug']


admin.site.register(Movement, MovementAdmin)
admin.site.register(Tag, TagAdmin)
