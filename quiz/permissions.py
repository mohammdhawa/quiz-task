from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsTeacherOrReadOnly(BasePermission):
    """
    The request is authenticated as a teacher for write access,
    otherwise read-only access is allowed.
    """
    def has_permission(self, request, view):
        # Allow all users to view (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True
        # Only allow teachers to create, update, or delete
        return request.user.is_authenticated and request.user.role == 'teacher'

class IsTeacherOrReadOnlyOrIsStudentForSubmission(BasePermission):
    """
    Allows:
    - Read-only access to all users (including students).
    - Teachers to perform any action.
    - Students to create submissions but not update or delete them.
    """
    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for all authenticated users
        if request.method in SAFE_METHODS:
            return True
        # Allow submission creation by authenticated users (students)
        if request.method == 'POST':
            return request.user.is_authenticated
        # Only allow teachers to update or delete
        return request.user.is_authenticated and request.user.role == 'teacher'