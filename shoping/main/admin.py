from django.contrib import admin
from main.models import Category, Color, Brand, Specifications, Product


admin.site.register(Product)

admin.site.register(Color)
admin.site.register(Specifications)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = (
        'name',
        'slug',
    )


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
