from import_export import resources
from .models import User, Student


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        exclude = (
            'user_permissions',
            'is_superuser',
            'profile_image',
            'height_field',
            'width_field',
            'is_staff',
            'is_active',
            'date_joined'
            'is_superuser',
            'groups',
            'last_login',
        )


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
