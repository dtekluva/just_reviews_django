from django.contrib import admin
from reviews.models import Product, Category, Comment
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'comments','slug',)
    

class CommentAdmin(admin.ModelAdmin):

    list_display = ('title', 'product', 'backs', 'pub_date')

# class UserAdmin(admin.ModelAdmin):

#     list_display = ('title', 'product', 'backs', 'pub_date')



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)