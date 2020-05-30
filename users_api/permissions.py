
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", obj)
        if request.user == obj or request.user == "admin":
            return True
        else:
            return False
        # if :
        #     return True
 
        # w_u = request.user.websiteuser_set.filter(user_id=request.user.id, email_settings_id=obj.id).first()
        # if w_u:
        #     return True
        # else:
        #     if request.method.lower() == 'get':
        #         return True
 
        # return False