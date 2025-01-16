from django.contrib import admin

from .models import Review, Tag

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['comment', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('slug', 'created', 'updated')

        return ()

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['tag', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('slug', 'created', 'updated')
        return ()