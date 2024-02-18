from django.contrib import admin
from .models import Producto, Categoria


# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre", "precio")
    search_fields = ("nombre",)


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
