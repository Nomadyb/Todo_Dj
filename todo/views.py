from django.shortcuts import render, get_object_or_404
import random
from todo.models import Todo , Category


def home_view(request):

    motivation_quotes = [
        "Motivation is what gets you started. Habit is what keeps you going.",
        "Don't watch the clock; do what it does. Keep going.",
        "Believe you can and you're halfway there.",
        
    ]
    random_motivation = random.choice(motivation_quotes)

    todos = Todo.objects.filter(is_active=True)

    
    context = {
        "todos": todos,
        "motivation_quote": random_motivation,
    }
    
    return render(request, "todo/todo_list.html", context)



def categoryView(request, catSlug):
    category = get_object_or_404(Category, slug=catSlug)
    todos = Todo.objects.filter(category=category, is_active=True, user=request.user,)

    context = {
        "todos": todos,
        "category": category,
    }
    return render(request, "todo/todo_list.html", context)





def todo_detail_view(request, id):
    todo = get_object_or_404(Todo, pk=id)
    

    image_urls = [
        "https://wallpapers.com/images/hd/minimalist-colorful-solar-system-y0v7avuayjl9gi74.webp",
        "https://wallpapers.com/images/hd/red-moon-minimalist-w02jclyyd7u1rbai.webp",
        "https://wallpapers.com/images/hd/colorful-cube-minimalist-2xuvdxq5ihi15f8n.webp",
        "https://img.freepik.com/free-photo/positivity-life-motivation-passion-inspiration-word-graphic_53876-124726.jpg",
        "https://www.thoughtco.com/thmb/ImHJQyy-rLI1UWElO7tmFnRI9u8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Anim1754_-_Flickr_-_NOAA_Photo_Library-57f289285f9b586c3561f25e.jpg",
        "https://c02.purpledshub.com/uploads/sites/62/2023/11/Whats-the-difference-between-whales-and-dolphins.jpg?w=1029&webp=1",
        "https://c02.purpledshub.com/uploads/sites/62/2023/11/Whats-the-difference-between-whales-and-dolphins.jpg?w=1029&webp=2"
    ]

    random_image_url = random.choice(image_urls)

    context = {
        "todo": todo,
        "random_image_url": random_image_url,
    }

    return render(request, "todo/todo_detail.html", context)
