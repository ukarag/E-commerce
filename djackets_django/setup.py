import os
import sys
import django

# Set the Django settings module to your project's settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djackets_django.settings")

# Initialize Django
django.setup()

# Import the necessary models
from product.models import Category, Product

# Create two categories: "summer" and "winter"
summer_category, created = Category.objects.get_or_create(name="Summer", slug="summer")
winter_category, created = Category.objects.get_or_create(name="Winter", slug="winter")

# Create products and associate them with the categories
Product.objects.get_or_create(
    category=summer_category,
    name="Summer Jacket",
    slug="summer-product-1",
    description="Very nice",
    price=10.99,
    image="summer1.jpg"
)

Product.objects.get_or_create(
    category=summer_category,
    name="Summer Tshirt",
    slug="summer-product-2",
    description="blue tshirt",
    price=15.99,
    image="uploads/tshirt_royal_blue_1.jpg"
)

Product.objects.get_or_create(
    category=winter_category,
    name="Winter Jacket",
    slug="winter-product-1",
    description="nice jacket",
    price=19.99,
    image="winter3.jpg"
)

Product.objects.get_or_create(
    category=winter_category,
    name="Winter Hat",
    slug="winter-product-2",
    description="Nice hat",
    price=25.99,
    image="hat.jpg"
)

# Create a superuser for managing the admin website
from django.contrib.auth.models import User

admin_user, created = User.objects.get_or_create(
    username="admin",
    is_staff=True,
    is_superuser=True
)

if created:
    admin_user.set_password("your_superuser_password")
    admin_user.save()

print("Categories and products created. Superuser 'admin' created for the admin site.")
