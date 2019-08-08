from django.db.models.manager import Manager
from django.db.models import Min, Avg, Max
# from .models import Item, Listing, Transaction
import datetime


class CategoryManager(Manager):
    """
    This is a manager for Categories where we can store commonly used querysets
    that will be used in our django project

    """



class ItemManager(Manager):
    """
    This is a manager for Items where we can store commonly used querysets as
    well as functions that will be used in our django project
    """

    def newItem(self,name, description, material, category):
        """
            This function will create a new item and add specific filters,
            filters will be added later

            Args:
                self: current instance of our manager
                name: the name of the item we are about to create
                description:the description of the of the item we are about
                        to create
                material: a string that contains the information for the
                        material for hte item we are about to create
                category: foreignKey to the category object which our new item
                        will be listed under

            Return: The New item we just created
        """
        item = self.model(name = name,
        description = description,
        material = material,
        category = category,
        lastActive = datetime.date.today()
        )

        item.save(using = self._db)

        return item

    def findItem(self, name = None , category = None ):
        """
            This function is a query that will be used for search functions

            Args:
                self: current instance of our manager
                name: the name of the item we are about to create
                description:the description of the of the item we are about
                        to create
                material: a string that contains the information for the
                        material for hte item we are about to create
                category: foreignKey to the category object which our new item
                        will be listed under


            Return: The New item we just created
        """
        if name != None and category != None:
            return self.get_queryset().filter(name__contains = name,
            category__name = categroy
            )
        elif name != None:
            return self.get_queryset().filter(name__contains = name)

        elif category != None:
            return self.sharedCategory(category)

        else:
            return None


    def sharedCategory(self, catName):
        return self.get_queryset().filter(category__name = catName)



class TransactionManager(Manager):
    """
    This is a manager for Transactions where we can store commonly used querysets
    as well as functions that will be used in our django project
    """

    def createTransaction(self, selller, buyer, amountExchanged, listing, deliveryAddress, receiveAddress, ratingSeller, ratingBuyer):
            transaction = self.model(
            seller = seller,
            buyer = buyer,
            amountExchanged = amountExchanged,
            listing = listing,
            deliveryAddress = deliveryAddress,
            receiveAddress = receiveAddress,
            timeSold = datetime.date.today(),
            ratingSeller = ratingSeller,
            ratingBuyer = ratingBuyer
            )

            item = transaction.listing.item
            itemAvg = item.avgSoldPrice
            itemHighest = item.highestSoldListing
            itemLowest = item.lowestSoldListing

            if((itemAvg == 1.00) and (itemHighest == 1.00) and (itemLowest == 1.00)):
                transaction.listing.item.avgSoldPrice = transaction.listing.price
                transaction.listing.item.highestSoldListing = transaction.listing.price
                transaction.listing.item.lowestSoldListing = transaction.listing.price

            elif(itemHighest < transaction.listing.price):
                transaction.listing.item.highestSoldListing = transaction.listing.price
                item.save()

            elif(itemLowest > transaction.listing.price):
                transaction.listing.item.lowestSoldListing = transaction.listing.price
                item.save()

            transaction.save(using = self._db)
            transaction.transactionMade()
            return transaction
