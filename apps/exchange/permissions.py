from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.seller == request.user

class IsBuyerOrSeller(BasePermission):
    message = 'You must either be the buyer or the seller of this listing'

    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        return (obj.seller == request.user) or obj.buyer == (request.user)
