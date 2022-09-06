from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    본인만 접근 가능
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:                           # 로그인 여부 확인
            if hasattr(obj, 'username'):                            # 본인이면 권한 부여
                return obj.username == request.user.username
            else:
                return False
        else:
            return False


class IsOwnerOrStaff(permissions.BasePermission):
    """
    로그인한 본인과 운영자 접근 가능
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:                       # 로그인 여부 확인
            if request.user.is_staff:                           # 운영자이면 권한 부여
                return True
            elif hasattr(obj, 'username'):                      # 본인이면 권한 부여
                return obj.username == request.user.username
        else:
            return False
