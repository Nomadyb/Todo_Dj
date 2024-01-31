from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title",unique=True) # aynı isimde slug oluşturulmasını engeller. slug: urldeki isimlerin arasındaki tireli kısım.
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'categoryView',
            kwargs={
                'catSlug': self.slug
            }

        )


class Todo(models.Model):
    #category = models.ForeignKey(Category, on_delete=models.CASCADE) # bir kategori silindiğinde o kategoriye ait tüm todolar silinir.
    #category = models.ManyToManyField(Category, blank=True) # bir todo birden fazla kategoriye ait olabilir.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # bir kategori silindiğinde o kategoriye ait tüm todolar silinir. null=True: kategori silindiğinde todo nun kategorisi null olur.

    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    crated_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) # yeni bir kayıt oluşturulduğunda otomatik olarak tarih ve saat bilgisi ekler.

    def __str__(self):
        return self.title


