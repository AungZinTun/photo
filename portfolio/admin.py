from django.contrib import admin
from .models import Album, Photo

# Register your models 

class PhotoInline(admin.TabularInline):
    model = Photo
class AlbumAdmin(admin.ModelAdmin):
    inlines=[PhotoInline,]

class ImageAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    # fields = ( 'image_tag','album', 'lighting', 'situation', 'mood', 'fov' )
    readonly_fields = ('image_tag',)

# admin.site.register(Photo, ImageAdmin)
admin.site.register(Album, AlbumAdmin)

