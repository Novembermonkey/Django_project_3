from django.db import models
from decimal import Decimal
from django.db.models import Avg
from django.db.models.functions import Round
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Category(BaseModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories/')
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')


    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        price = self.price * Decimal(f'{1-(self.discount/100)}')
        return price.quantize(Decimal('1.00'))

    @property
    def primary_image_url(self):
        try:
            return self.images.get(is_primary=True).image.url
        except ObjectDoesNotExist:
            return self.images.first().image.url

    @property
    def avg_rating(self):
        avg = self.comments.aggregate(avg=Round(Avg('rating'), precision=2))['avg']
        return avg

class ProductImage(BaseModel):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product} - {self.image.url}'


class AttributeKey(BaseModel):
    key = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.key

class AttributeValue(BaseModel):
    value = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.value

class ProductAttribute(BaseModel):
    attribute_key = models.ForeignKey(AttributeKey, on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')

    def __str__(self):
        return f'{self.product.name} - {self.attribute_key.key} - {self.attribute_value.value}'

class Comment(BaseModel):
    class RatingChoices(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.THREE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name





