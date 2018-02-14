from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )

from .permissions import IsOwnerOrReadOnly, IsBuyerOrSeller

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

from .serializers import *


#------------------------------------------------------------------------------
#Category
#------------------------------------------------------------------------------


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [AllowAny]



class CategoryDetail(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [AllowAny]


#------------------------------------------------------------------------------
#subCategory
#------------------------------------------------------------------------------



class SubCategoryCreate(CreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryCreateUpdateSerializer
    permission_classes = [IsAdminUser]



class SubCategoryList(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer
    permission_classes = [AllowAny]


class SubCategoryDetial(RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryDetailSerializer
    permission_classes = [AllowAny]

#------------------------------------------------------------------------------
#Items
#------------------------------------------------------------------------------

class ItemCreate(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class ItemUpdate(RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemCreateUpdateSerializer
    permission_classes = [IsAdminUser]

    def perform_update(self, serializer):
        serializer.save()

class ItemDelete(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class =  ItemDetailSeralizer
    permission_classes = [IsAdminUser]


class ItemDetail(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSeralizer
    permission_classes = [AllowAny]

class ItemList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListlSeralizer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ['name', 'category', 'subCatergory' , 'description']
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Item.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains = query)|
                Q(category__name__icontains = query)|
                Q(description__icontains = query)
            ).distinct()
        return queryset_list


#------------------------------------------------------------------------------
#Listing
#------------------------------------------------------------------------------


# class ListingCreate(CreateAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingCreateUpdateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(seller = self.request.user)
#
# class ListingUpdate(RetrieveUpdateAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingCreateUpdateSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#
#     def perform_update(self, serializer):
#         serializer.save(seller = self.request.user)
#
# class ListingDelete(DestroyAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingDetailSeralizer
#     permission_classes = [IsOwnerOrReadOnly]
#
#
# class ListingDetial(RetrieveAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingDetailSeralizer
#     permission_classes = [AllowAny]
#
#
# class ListingList(ListAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingListSeralizer
#     permission_classes = [AllowAny]
#
#     def get_queryset(self, *args, **kwargs):
#         queryset_list = Listing.objects.all()
#         query = self.request.GET.get("q")
#         if query:
#             queryset_list = queryset_list.filter(
#             Q(item__name__icontains = query)|
#             Q(item__description__icontains = query)|
#             Q(item__subCategory__name__icontains = query)|
#             Q(item__category__name__icontains = query)|
#             Q(price__icontains = query)
#
#             ).distinct()
#         return queryset_list




#------------------------------------------------------------------------------
#Transaction
#------------------------------------------------------------------------------

class TransactionCreate(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionCreateUpdateSerializer
    premission_classes = [IsAuthenticated]


    #def perform_create(self, serializer):

class TransactionUpdate(RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionCreateUpdateSerializer
    permission_classes = [IsBuyerOrSeller, IsAdminUser]

##Need to add the query to this thing
class TransactionList(ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if (user.is_superuser):
            return Transaction.objects.all()
        else:
            return Transaction.objects.filter(Q(seller = user) | Q(buyer = user))


class TransactionDetail(RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsBuyerOrSeller, IsAdminUser]
