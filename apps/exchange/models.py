from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from .manager import CategoryManager, ItemManager, TransactionManager
import datetime
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save

class Category(models.Model):
    """
        This is a model for a predetermined list of clothing categories.

        List:
            Jackets, shirts, sweaters, sweatshirts, pants, t-shirts, hats, accessories, skate, bike, and other

        Attributes:
            name: A string of the name of a category
            slug: A slug to make our links more presentable on the web app
    """
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('exchange:item_list_by_category', args=[self.slug])

    def save(self, **kwargs):
        """
            This function is an override of the save function of Category
            so thaat we can automatically create a slug
            Args:s
                self: current instance of that object
        """
        if not self.pk:
            slug = self.name
            slug = slug.lower()
            slug = slug.replace(" ","-")
            self.slug = slug

        super(Category, self).save(**kwargs)


class Item(models.Model):
    """
        This is a model for items sold on the exchange.

        Attributes:
            name: A string of the name of the item
            slug: A slug to make our links more readable
            description: A string which should describe the item for the users
            material: A string which should identify the materials used to make the item
            category: A foregin key to category to make items more organized
            lastActive: A date and time which represent when the last time the item has been edited
            available: A boolean which represents whether there are items avialble or not
            created = The date and time field that the item was created
            updated = the date and time field the item was last updated
            stock: a integer that represents the amount of items that are availble for the user to buy
    """
    name = models.CharField(max_length=200, db_index=True, unique = True)
    slug = models.SlugField(max_length=200, db_index=True)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    material = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='Item', on_delete=models.CASCADE)
    price = models.DecimalField(
        default=1.00,
        validators=[MinValueValidator(1.0)],
        decimal_places=2,
        max_digits=10,
    )
    lastActive = models.DateTimeField(default = timezone.now)
    visible = models.BooleanField(default = True)
    stock = models.PositiveIntegerField(
            default = 1
    )
    objects = ItemManager()
    primaryImage = models.ImageField(upload_to = 'images/')
    imageCount = models.IntegerField(default = 0)

    def save(self, **kwargs):
        """
            This function is an override of the save function so that the item object
            will be automiatcally updated everytime there is  achange within the item

            Args:
                self: current instance of that object
        """
        if not self.pk:
            slug = self.name
            slug = slug.lower()
            slug = slug.replace(" ","-")
            self.slug = slug

        super(Item, self).save(**kwargs)

    @property
    def category_name(self):
        return self.category.name

    @property
    def seller_name(self):
        return self.seller.username

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-lastActive',)
        index_together = (('id','slug'),)
        verbose_name_plural = 'Items'

    def get_absolute_url(self):
        return reverse('exchange:item_detail', args=[self.id, self.slug])

    def __unicode__(self):
        return ('%d: %s' (self.id, self.name))

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    url = models.ImageField(upload_to = scramble_uploaded_filename)
    index = models.IntegerField(default = 0)


    def save(self, **kwargs):
        if not self.pk:
            self.index = self.item.imageCount + 1
            self.item.imageCount += 1
            self.item.save()

        super(ItemImage, self).save(**kwargs)


@receiver(post_save, sender = Item)
def create_itemImage_for_new_item(sender, created, instance, **kwargs):
    if created:
        itemImage = ItemImage(item = instance, url = instance.primaryImage)
        itemImage.save()

# Add a save to transactions
class Transaction(models.Model):
    """
        This is a model for items on the exchange.

        Attributes:
            seller: A foriegn key to a user object that sold the items
            buyer: A foreign key to a user object that is buying the items
            amountExchanged: the amount of money exchanged between seller and
                buyer
            item = A foreign key to the item object to mark it as sold
            deliveryAddress = a text field which contains the address of the
                seller
            receiveAddress = a text field which contains the address of the
                buyer
            ratingSeller = a decimal field which contains a rating for the
                seller 1-5
            ratingBuyer = a decimal field which contains a rating for the buyer
                1-5
            isValid = a boolean field which stores whether the transaction
                will go through or cancel
    """
    seller = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
                related_name='Seller'
    )
    buyer = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
                related_name='Buyer'
    )
    amountExchanged = models.DecimalField(
                decimal_places=2,
                max_digits=10
    )
    item = models.ForeignKey(Item, related_name = "Item", on_delete=models.CASCADE)
    deliveryAddress = models.TextField()
    receiveAddress = models.TextField()
    timeSold = models.DateTimeField(auto_now = True)
    ratingSeller =  models.DecimalField(
            decimal_places = 1,
            max_digits = 1

    )
    ratingBuyer = models.DecimalField(
            decimal_places = 1,
            max_digits = 1

    )
    isValid = models.BooleanField(default = True)
    objects = TransactionManager()
