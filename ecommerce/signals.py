from django.db.models.signals import pre_delete, post_delete, post_save
from django.dispatch import receiver
from users.models import CustomUser
from .models import Product
from .resources import ProductResource
import json
from django.core.mail import send_mail


@receiver(pre_delete, sender=Product)
def product_pre_delete(sender, instance, **kwargs):
    resource = ProductResource()
    dataset = resource.export([instance])
    deleted_product = json.loads(dataset.json)[0]

    with open('ecommerce/backups/deleted_products.json', 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    data.append(deleted_product)

    with open('ecommerce/backups/deleted_products.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@receiver(post_delete, sender=Product)
def product_post_delete(sender, instance, **kwargs):
    receivers = ["djodio2023@gmail.com"] #put your receiver here
    send_mail(
        "Deleted product",
        "Backup made successfully",
        'heyj0435@gmail.com',
        receivers,
        fail_silently=False,
    )


@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "Product added",
            f"{instance.name.title()} was added to the stock",
            'heyj0435@gmail.com',
            [user for user in CustomUser.objects.all()],
        )

