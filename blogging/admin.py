from django.contrib import admin
from blogging.models import Post, Category

# If happy with the default admin interface, then all you need is the below code:
# admin.site.register(Post)
# admin.site.register(Category)


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
