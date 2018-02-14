from django.db.models.manager import Manager
from django.db.models import Min, Avg, Max
#from .models import Category, SubCategory, Item, Listing, Transaction
import datetime


class CategoryManager(Manager):
    """
    This is a manager for Categories where we can store commonly used querysets
    that will be used in our django project

    """


class SubCatergoryManager(Manager):
    """
    This is a manager for SubCategories where we can store commonly used
    querysets that will be used in our django project
    """
    def siblings(self, catName):
        return self.get_queryset().filter(parent__name=catName)



class ItemManager(Manager):
    """
    This is a manager for Items where we can store commonly used querysets as
    well as functions that will be used in our django project
    """

    def newItem(self,name, description, material, category, subCategory):
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
                subCategory; foreignKey to the subCategory object which our
                        new item will be listed under

            Return: The New item we just created
        """
        item = self.model(name = name,
        description = description,
        material = material,
        category = category,
        subCategory = subCategory,
        lastActive = datetime.date.today()
        )

        item.save(using = self._db)

        return item

    def findItem(self, name = None , category = None  , subCategory = None):
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
                subCategory; foreignKey to the subCategory object which our
                        new item will be listed under

            Return: The New item we just created
        """
        if name != None and category != None and subCategory != None:
            return self.get_queryset().filter(name__contains = name,
            category__name = category,
            subCategory__name = subCategory
            )
        elif name != None and category != None:
            return self.get_queryset().filter(name__contains = name,
            category__name = categroy
            )
        elif category != None and subCategory != None:
            return self.get_queryset().filter(category__name = category,
            subCategory__name = subCategory
            )
        elif name != None:
            return self.get_queryset().filter(name__contains = name)

        elif category != None:
            return self.sharedCategory(category)

        else:
            return None




    def sharedCategory(self, catName):
        return self.get_queryset().filter(category__name = catName)

    def sharedSubCategory(self, subCatName):
        return self.get_queryset().filter(subCategory__name = subCatName)



# class ListingManager(Manager):
#     """
#     This is a manager for Listings where we can store commonly used querysets
#     as well as functions that will be used in our django project
#     """
#
#     def newListing(self,seller, item, conditionRating, description, location, price, size):
#         """
#             This function will create a new item and add specific filters,
#             filters will be added later
#
#             Args:
#                 self: current instance of our manager
#                 seller: the foriegn key to the user that will be attached to the
#                     seller user
#                 item: foreign key to the user that will be attached to the
#                     item that is being sold
#                 conditionRating: a decimal  from range 0.0 - 5.0 that represents
#                     the condition of the listed item
#                 description: a string that will describe the listing
#                 location: a string that contains the location of the seller
#                 price: a decimal that represents how much money the seller is
#                     asking for.
#                 size: the size of the product for example 'M' or 'XL'
#
#
#             Return: The New item we just created
#         """
#         listing = self.model(seller = seller,
#         item = item,
#         conditionRating = conditionRating,
#         description = description,
#         location = location,
#         price = price,
#         size = size,
#         available = True,
#         created = datetime.date.today(),
#         updated = datetime.date.today()
#         )
#
#         item = listing.item
#         itemLowest = listing.item.lowestCurrListing
#         itemHighest = listing.item.highestCurrListing
#
#         if itemLowest == 1.00 and itemHighest == 1.00:
#             listing.item.lowestCurrListing = listing.price
#             listing.item.highestCurrListing = listing.price
#             item.save()
#
#         elif listing.price < itemLowest:
#             listing.item.lowestCurrListing = listing.price
#             item.save()
#
#         elif listing.price > itemHighest:
#             listing.item.highestCurrListing = listing.price
#             item.save()
#
#         listing.save(using=self._db)
#         return listing
#
#     def updateSoldOrDelete(self, listing):
#         if listing.price == listing.item.lowestCurrListing:
#             listing.item.lowestCurrListing = self.lowestCurrentPrice(
#                     listing.item.name
#             )
#
#         elif listing.price == listing.item.highestCurrListing:
#             listing.item.highestCurrListing = self.highestCurrentPrice(
#                 listing.item.name
#             )
#
#
#     def avgSoldPrice(self,itemRef):
#         """
#             This function will run a query that will return the average price
#             that a paticular item has been sold for.
#
#             Args:
#                 self: current instance of that object
#                 itemRef: the reference to the item we wish to find the average
#                     selling price of
#
#             Return: An float that contains the average sold price of a
#                         particular item
#         """
#         return self.filter(
#             item__name = itemRef,
#             available = False
#             ).aggregate(Avg('price'))
#
#     def lowestSoldPrice(self, itemRef):
#         """
#             This function will run a query that will return the lowest price
#             that a paticular item has been sold for.
#
#             Args:
#                 self: current instance of that object
#                 itemRef: the reference to the item we wish to find the lowest
#                     sold price of
#
#             Return: An float that contains the lowest sold price of a
#                         particular item
#         """
#         return self.filter(
#             item__name = itemRef,
#             available = False
#             ).aggregate(Min('price'))
#
#     def highestSoldPrice(self, itemRef):
#         """
#             This function will run a query that will return the highest price
#             that a paticular item has been sold for.
#
#             Args:
#                 self: current instance of that object
#                 itemRef: the reference to the item we wish to find the highest
#                     selling price of
#
#             Return: An float that contains the lowest sold price of a
#                         particular item
#         """
#         return self.filter(
#             item__name = itemRef,
#             available = False
#             ).aggregate(Max('price'))
#
#     def lowestCurrentPrice(self, itemRef):
#         """
#             This function will run a query that will return the lowest price
#             that is currently listed
#
#             Args:
#                 self: current instance of that object
#                 itemRef: the reference to the item we wish to find the lowest
#                             current listing price
#
#             Return: An float that contains the lowest current listing price of
#                         a particular item
#         """
#         return self.filter(
#             item__name = itemRef,
#             available = True
#             ).aggregate(Min('price'))
#
#     def highestCurrentPrice(self, itemRef):
#         """
#             This function will run a query that will return the highest price
#             that is currently listed
#
#             Args:
#                 self: current instance of that object
#                 itemRef: the reference to the item we wish to find the highest
#                             current listing price
#
#             Return: An float that contains the highest current listing price of
#                         a particular item
#         """
#         return self.filter(
#             item__name = itemRef,
#             available = True
#             ).aggregate(Max('price'))

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
