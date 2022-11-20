from django.db import models
from django.core.files import File

# Create your models here.


# class ProductImage(models.Model):
#     image_file = models.ImageField(upload_to='images')
#     image_url = models.URLField()

#     def save(self, *args, **kwargs):
#         if self.image_url:
#             r = requests.get(self.image_url)
#             self.image_file.save(
#                 os.path.basename(self.image_url),
#                 io.BytesIO(r.content)
#             )
#             super(ProductImage, self).save(args, kwargs)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    retail_price = models.IntegerField(default=0)
    discounted_price = models.IntegerField(default=0)
    brand = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    image_url = models.URLField()