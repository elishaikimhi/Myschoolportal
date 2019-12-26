from import_export import resources
from .models import User, Student
from django.db import IntegrityError


class UsersResource(resources.ModelResource):
    class Meta:
        model = User
        skip_unchanged = True
        report_skipped = True
        # import_id_fields = ('USERNAME',)
        # fields = ('USERNAME', 'PASSWORD', 'USER_TYPE',)
        exclude = ('email',
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
                   'date_of_birth',
                   'first_name',
                   'last_name',
                   'phone_number',
                   )

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):

        # Clear out anything that may be there from a dry_run,
        #  such as the admin mixin preview
        self.set_unique = set()

    def skip_row(self, instance, original):
        username = instance.username  # Could also use composer_key_id
        password = instance.password
        tuple_unique = (username, password)

        if tuple_unique in self.set_unique:
            return True
        else:
            self.set_unique.add(tuple_unique)
        return super(UsersResource, self).skip_row(instance, original)
        # def save_instance(self, instance, using_transactions=True, dry_run=False):
        #     try:
        #         super(UserResource, self).save_instance(
        #             instance, using_transactions, dry_run)
        #     except IntegrityError:
        #         pass


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
