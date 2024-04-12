from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        """
        Devuelve la URL absoluta de la categoría.
        """
        return reverse('products_by_category', args=[self.slug])

    def __repr__(self):
        """
        Devuelve una representación de cadena de la categoría.
        """
        return self.category_name
