from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStreamerOrReadOnly(BasePermission):
    message = 'You must be the streamer to access this'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.streamer.user == request.user

class IsUserOrReadOnly(BasePermission):
    message = 'You must be the user to access this'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

class IsUploaderOrReadOnly(BasePermission):
    message = 'You must be the uploader of the notes to access this'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.uploader.user == request.user
        