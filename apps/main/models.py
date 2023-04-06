from django.db import models
from django.utils.text import slugify
# Create your models here.
class Tag(models.Model):
    name =models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    headline =models.CharField(max_length=200, verbose_name="Название")
    sud_headline = models.CharField(max_length=200, null=True, blank=True, verbose_name="Описание")
    body = models.TextField(null=True, blank=True, verbose_name="Текст")
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, verbose_name="Избранные")
    tags = models.ManyToManyField(Tag, verbose_name="Направление")
    image = models.ImageField(null=True, blank=True, upload_to='images', default='1.jpg', verbose_name="Изображение")
    # slug = models.SlugField(null=True, blank=True)

    def __str__(self) -> str:
        return self.headline
    # # slug 
    # def save(self, *args, **kwargs):
    #     if self.slug == None:
    #         slug = slugify(self.headline)
    #         has_slug = Post.objects.filter(slug=slug).exists()
    #         count = 1
    #         while has_slug:
    #             count += 1
    #             slug = slugify(self.headline) + '-' + str(count)
    #             has_slug = Post.objects.filter(slug=slug).exists()
    #         self.slug = slug
    #     super().save(*args, **kwargs)



