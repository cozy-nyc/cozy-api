from django.test import TestCase
from .models import Category, SubCategory, Item, Listing, Transaction
from django.contrib.auth.models import User


# Create your tests here.

class CategoryTestCase(TestCase):
    """
    Tests ORM functions for the Category models
    """
    def setUp(self):
        '''
        The set up for the tests
        '''
        Category.objects.create(name = "Shirts",slug = "shirts")

    def test_category_exists(self):
        '''
        Simply tests if the object exists to know the ORM is working
        fine
        '''
        shirts = Category.objects.get(name = "Shirts")
        self.assertEqual(shirts.name, 'Shirts')


class SubCategoryCase(TestCase):
    def setUp(self):
        '''
        The set up for the tests
        '''
        Category.objects.create(name = "Shirts",slug = "shirts")

        SubCategory.objects.create(name = "Tank Tops",
        parent = Category.objects.get(name = "Shirts")
        )
        SubCategory.objects.create(name = "T-Shirts",
        parent = Category.objects.get(name = "Shirts")
        )

    def test_sibling(self):
        '''
        Tests if the sibiling function works correctly. Checks for all
        subcategories that share the same category parent
        '''
        subcats = SubCategory.objects.siblings('Shirts')
        self.assertEqual(len(subcats),2)

class ItemTestCase(TestCase):
    def setUp(self):
        '''
        The set up for the tests.
        Adding multiple categoryies , subcategories, and items
        '''
        Category.objects.create(name = "Shirts",slug = "shirts")

        SubCategory.objects.create(name = "Tank Tops",
        parent = Category.objects.get(name = "Shirts")
        )

        SubCategory.objects.create(name = "T-Shirts",
        parent = Category.objects.get(name = "Shirts")
        )

        Item.objects.newItem(name = 'Supreme Yankee Box Logo T-Shirt White',
        description = """Supreme's collaboration with the New York Yankee in
        SS2015 resulted in production of this shirt """,
        material = "100%% Cotton",
        category = Category.objects.get(name = "Shirts"),
        subCategory = SubCategory.objects.get(name="T-Shirts")
        )

        Item.objects.newItem(name = 'Supreme Pink Tank Top',
        description = """Supreme's Tank Top from SS2017 """,
        material = "100%% Cotton",
        category = Category.objects.get(name = "Shirts"),
        subCategory = SubCategory.objects.get(name="Tank Tops")
            )


    def test_find_one(self):
        '''
        tests if we can find items if they contain certain characters
        '''
        item = Item.objects.findItem(name = 'Tank Top')
        self.assertEqual(len(item), 1)

    def test_find_two(self):
        '''
        tests if we can find items based off their category
        '''
        item = Item.objects.findItem(category = "Shirts")
        self.assertEqual(len(item),2)

    def test_find_three(self):
        '''
        tests finding item through two different search queries
        '''
        item = Item.objects.findItem(name = 'Yankee', subCategory = 'T-Shirts')
        self.assertEqual(len(item),1)


class ListingTestCase(TestCase):
    def setUp(self):
        '''
        Set up for tests of listings.
        Adding multiple users, categories, subcategories, items and listing
        '''
        user = User.objects.create_user(username='john',
        email='jlennon@beatles.com',
        password='glassonion'
        )

        user = User.objects.create_user(username='zahi',
        email='zahi@benballer.com',
        password='playboicarti'
        )

        Category.objects.create(name = "Shirts",slug = "shirts")

        SubCategory.objects.create(name = "Tank Tops",
        parent = Category.objects.get(name = "Shirts")
        )

        SubCategory.objects.create(name = "T-Shirts",
        parent = Category.objects.get(name = "Shirts")
        )

        Item.objects.newItem(name = 'Supreme Yankee Box Logo T-Shirt White',
        description = """Supreme's collaboration with the New York Yankee in
        SS2015 resulted in production of this shirt """,
        material = "100%% Cotton",
        category = Category.objects.get(name = "Shirts"),
        subCategory = SubCategory.objects.get(name="T-Shirts")
        )

        Item.objects.newItem(name = 'Supreme Pink Tank Top',
        description = """Supreme's Tank Top from SS2017 """,
        material = "100%% Cotton",
        category = Category.objects.get(name = "Shirts"),
        subCategory = SubCategory.objects.get(name="Tank Tops")
        )

        Listing.objects.newListing(
        seller = User.objects.get(username = 'zahi'),
        item = Item.objects.get(name = 'Supreme Yankee Box Logo T-Shirt White'),
        conditionRating = 4.0,
        description = "In Good Condition. No Rips",
        location = 'Queens',
        price = 200.00,
        size = "M"
        )

        Listing.objects.newListing(
        seller = User.objects.get(username = 'john'),
        item = Item.objects.get(name = 'Supreme Yankee Box Logo T-Shirt White'),
        conditionRating = 3.0,
        description = "In Good Condition. Some stains",
        location = 'Queens',
        price = 70.00,
        size = "L"
        )

        Listing.objects.newListing(
        seller = User.objects.get(username = 'zahi'),
        item = Item.objects.get(name = 'Supreme Pink Tank Top'),
        conditionRating = 3.0,
        description = "In Good Condition. Some stains",
        location = 'Queens',
        price = 50.00,
        size = "S"
        )

    def test_lowest_current_price(self):
        '''
        tests if the loweest current price matches our query and how the
        new listing function is set up to automatically update the item
        if a new listing is created that has a smaller price then the previous
        '''
        lowestPrice = Listing.objects.lowestCurrentPrice(
        itemRef = 'Supreme Yankee Box Logo T-Shirt White'
        )

        self.assertEqual(lowestPrice['price__min'],70.00)

        item = Item.objects.get(name = 'Supreme Yankee Box Logo T-Shirt White')
        self.assertEqual(item.lowestCurrListing, 70.00)

        listing1 = Listing.objects.get(
            seller = User.objects.get(username = 'john'),
            item = Item.objects.get(name = "Supreme Yankee Box Logo T-Shirt White")
            )
        listing1.listingSold()
        listing1.save()
        Listing.objects.updateSoldOrDelete(listing1)

        newLowestPrice = Listing.objects.lowestCurrentPrice(
        itemRef = 'Supreme Yankee Box Logo T-Shirt White'
        )

        self.assertEqual(newLowestPrice['price__min'],200.00)




    def test_highest_current_price(self):
        '''
        tests if the highest current price matches our query and how the
        new listing function is set up to automatically update the item
        if a new listing is created that has a higher price then the previous
        highest price
        '''
        highestPrice = Listing.objects.highestCurrentPrice(
        itemRef = 'Supreme Yankee Box Logo T-Shirt White'
        )

        self.assertEqual(highestPrice['price__max'],200.00)

        item = Item.objects.get(name = 'Supreme Yankee Box Logo T-Shirt White')
        self.assertEqual(item.highestCurrListing, 200.00)


class TransactionTestCase(TestCase):
    def setUp(self):
        '''
        set up for the transactions tests
        adding multiple users, categories, items, subcategories,
        listings, as well as transactions
        '''
        user = User.objects.create_user(username='john',
        email='jlennon@beatles.com',
        password='glassonion'
        )

        user = User.objects.create_user(username='zahi',
        email='zahi@benballer.com',
        password='playboicarti'
        )

        Category.objects.create(name = "Shirts",slug = "shirts")

        SubCategory.objects.create(name = "Tank Tops",
        parent = Category.objects.get(name = "Shirts")
        )

        SubCategory.objects.create(name = "T-Shirts",
        parent = Category.objects.get(name = "Shirts")
        )

        Item.objects.newItem(name = 'Supreme Yankee Box Logo T-Shirt White',
        description = """Supreme's collaboration with the New York Yankee in
        SS2015 resulted in production of this shirt """,
        material = "100%% Cotton",
        category = Category.objects.get(name = "Shirts"),
        subCategory = SubCategory.objects.get(name="T-Shirts")
        )

        Item.objects.newItem(name = 'Supreme Pink Tank Top',
        description = """Supreme's Tank Top from SS2017 """,
        material = "100%% Cotton",
        category = Category.objects.get(name = "Shirts"),
        subCategory = SubCategory.objects.get(name="Tank Tops")
        )

        Listing.objects.newListing(
        seller = User.objects.gget(username = 'zahi'),
        item = Item.objects.get(name = 'Supreme Yankee Box Logo T-Shirt White'),
        conditionRating = 4.0,
        description = "In Good Condition. No Rips",
        location = 'Queens',
        price = 200.00,
        size = "M"
        )

        Listing.objects.newListing(
        seller = User.objects.get(username = 'john'),
        item = Item.objects.get(name = 'Supreme Yankee Box Logo T-Shirt White'),
        conditionRating = 3.0,
        description = "In Good Condition. Some stains",
        location = 'Queens',
        price = 70.00,
        size = "L"
        )

        Listing.objects.newListing(
        seller = User.objects.get(username = 'zahi'),
        item = Item.objects.get(name = 'Supreme Pink Tank Top'),
        conditionRating = 3.0,
        description = "In Good Condition. Some stains",
        location = 'Queens',
        price = 50.00,
        size = "S"
        )

        Transaction.objects.createTransaction(
        seller = User.objects.get(username = 'zahi'),
        buyer  = User.objects.get(username = 'john'),
        amountExchanged = 200.00,
        listing = Listing.objects.get(
            selller = User.objects.get(username = 'zahi'),
            item = Item.objects.get(name = "Supreme Yankee Box Logo T-Shirt White")
            ),
        deliveryAddress = 'Queens',
        receiveAddress = 'Queens',
        ratingSeller = 4.4,
        ratingBuyer = 5.0
        )

    #def test_average_sale(self):

    #    transaction1 = Transaction.objects.get()
