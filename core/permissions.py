from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthorAndStaffAllEditOrReadOnly(BasePermission):
    """
     작성자와 관리자(superuser)는 게시글에 대한 전체 액세스 권한을 가지고,
     운영자(staff)는 게시판을 삭제할 수 있지만 편집할 수 없도록 Custom한 Permission
    """

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        # 사용자가 로그인되어 있을 때만 create 가능
        return request.method in SAFE_METHODS or request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in SAFE_METHODS:
            return True

        if obj.author_id == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            # 운영자는 게시판을 편집할 수 없음
            return True

        return False
