from django.contrib import admin

from .models import Todo, Category
# Register your models here.





class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'is_active' , 'crated_at', 'updated_at', 'category')
    list_display_links = [
        'title',
        'content',
        "category",
    ]
    


admin.site.register(Todo, TodoAdmin)

admin.site.register(Category)

