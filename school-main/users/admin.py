from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportActionModelAdmin, ExportActionModelAdmin, ImportExportMixin
from .resources import UsersResource
from django.utils.html import format_html
from django.utils.translation import gettext_lazy

# from .forms import CostumeSinupForm, CustomUserChangeForm
from .models import User, Student, Teacher, OrigenClass, Grade
# Register your models here.


@admin.register(User)
class UsersAdmin(ImportExportActionModelAdmin, UserAdmin):
    resource_class = UsersResource

    def profile_image_tag(self, obj):
        height = 50
        width = 50
        border_radius = 100
        if obj.profile_image:
            return format_html(f'<img style="height: {height}px;\
                               width: {width}px;\
                               border-radius: {border_radius}%"\
                               src="{obj.profile_image.url}">')
        else:
            return format_html(f'<img style="height: {height}px;\
                               width: {width}px; \
                               border-radius: {border_radius}%" \
                               src="https://encrypted-tbn0.gstatic.com/\
                               images?q=tbn:ANd9GcTtAnWXwSHisKlipWhuvSU5\
                               _kXYb7UBejOTZTaHpMTdwlklRrYv">')

    profile_image_tag.short_description = 'Profile image'

    list_per_page = 20
    list_display = ('id',
                    'profile_image_tag',
                    'username',
                    'first_name',
                    'last_name',
                    'is_active',
                    'is_superuser',
                    'user_type',
                    'date_joined',
                    )

    search_fields = ('id', 'username', 'first_name', 'last_name')
    list_filter = ('user_type', 'is_active',)
    show_full_result_count = False
    readonly_fields = ('date_joined',)
    ordering = ('id',)

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    fieldsets = (
        ('Personal details', {
            'fields': ('username', 'email', 'password',
                       'first_name', 'last_name', 'date_of_birth',)
        }),
        ('contact details', {
            'fields': ('phone_number', 'profile_image')
        }),
        ('user permission', {
            'fields': [('user_type', 'is_active'),
                       ('date_joined', 'last_login'), 'user_permissions']
        }),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    # actions = ["deactivate_selected_users", "activate_selected_users"]

    # # Deactivate selected user
    # def deactivate_selected_users(self, request, queryset):
    #     queryset.update(is_active=False)

    # # Activate selected user
    # def activate_selected_users(self, request, queryset):
    #     queryset.update(is_active=True)


@admin.register(Teacher)
class TeacherAdmin(ExportActionModelAdmin):
    list_display = ['user_id',
                    'teacher_full_name',
                    'user_profile_image',
                    'user',
                    'user_personal_number',
                    'teacher_subject',
                   
                    ]
    ordering = ('user',)

    # get the profile image from User(AbstarctUser)
    def user_profile_image(self, obj):
        height = 50
        width = 50
        border_radius = 100
        if obj.user.profile_image:
            return format_html(f'<img style="height: {height}px;\
                                width: {width}px; \
                                border-radius: {border_radius}%" \
                                src="{obj.user.profile_image.url}">')
        else:
            return format_html(f'<img style="height: {height}px; \
                                width: {width}px;\
                                border-radius: {border_radius}%"\
                                src="https://encrypted-tbn0.gstatic.com/\
                                images?q=tbn:ANd9GcTtAnWXwSHisKlipWhuvSU5\
                                _kXYb7UBejOTZTaHpMTdwlklRrYv">')
    user_profile_image.short_description = 'profile image'

    # oneToone field of user from User get 'username'
    def user_personal_number(self, obj):
        return obj.user.phone_number
    user_personal_number.short_description = 'personal number 📞'

    def teacher_full_name(self, obj):
        return f'Teacher {obj.user.last_name} {obj.user.first_name}'


@admin.register(Student)
class StudentAdmin(ExportActionModelAdmin):
    list_display = ('user_id',
                    'user_profile_image',
                    'user',
                    'user_personal_number',
                    'origen_class',
                    )
    list_filter = ('origen_class',)
    search_fields = ('user__id', 'user__username')  # search field for students
    # filter_horizontal = ('subjects',)

    # oneToone field of user from User get 'profile image'
    def user_profile_image(self, obj):
        height = 50
        width = 50
        border_radius = 100
        if obj.user.profile_image:
            return format_html(f'<img style="height:{height}px; width:{width}px; \
                               border-radius:{border_radius}%" \
                               src="{obj.user.profile_image.url}">')
        else:
            return format_html(f'<img style="height:{height}px; width:{width}px; \
                               border-radius: {border_radius}%" \
                               src="https://encrypted-tbn0.gstatic.com/\
                               images?q=tbn:ANd9GcTtAnWXwSHisKlipWhuvSU\
                               5_kXYb7UBejOTZTaHpMTdwlklRrYv">')
    user_profile_image.short_description = 'profile image'

    # oneToone field of user from User get 'username'
    def user_personal_number(self, obj):
        return obj.user.phone_number
    user_personal_number.short_description = 'personal number 📞'


# admin.site.register(User)
# admin.site.register(Student)
# admin.site.register(Teacher)
admin.site.register(OrigenClass, ImportExportActionModelAdmin)
admin.site.register(Grade)


# admin.AdminSite.site_title = gettext_lazy('My School')

# # Text to put in each page's <h1>.
# admin.AdminSite.site_header = gettext_lazy('My School Administration')

# # Text to put at the top of the admin index page.
# admin.AdminSite.index_title = gettext_lazy('My School Administration')
