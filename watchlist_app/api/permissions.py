from rest_framework import permissions


#creating a permission which will work like:if the user is admin, then he can edit anything otherwise it's read only. 
class IsAdminOrReadOnly(permissions.IsAdminUser):
    # so if we use has_object_permission, we are specifically checking a particular object. For example, the individual review can be edit by only the user that created them. There it is useful. 
    # has_permission when we are generally checking if the user has permission to read or edit.
    
    
    # if admin is user, return true.
    def has_permission(self, request, view):
        #admin_permission = super().has_permission(request, view)
        # admin_permission = bool(request.user and request.user.is_staff)
        # return request.method == "GET" or admin_permission
    
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            # Check permissions for write request
            return bool(request.user and request.user.is_staff)
    
    

# Now creating a class such that only the user should have control over his review.
class IsReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            # Check permissions for write request
            return request.user == obj.review_user or request.user.is_staff
        