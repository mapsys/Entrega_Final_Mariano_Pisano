from django.contrib import admin
from . import models
# Register your models here.
app_name = "posteos"
admin.site.site_title = "Posteos"




class PosteoAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "subtitulo",
        "contenido",
        "autor",
        "fecha_creacion",
        "imagen",
    )
    list_display_links = ("titulo",)
    search_fields = ("titulo",)
    ordering = ("titulo", "autor", "fecha_creacion")
    list_filter = ("autor",)
    date_hierarchy = "fecha_creacion"


admin.site.register(models.Posteo, PosteoAdmin)
