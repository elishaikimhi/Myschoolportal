from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CostumeSinupForm, CustomUserChangeForm
from .models import User, Student, Teacher, OrigenClass, Grade
# Register your models here.


# class CustomUserAdmin(UserAdmin):


#     add_form = CostumeSinupForm
#     form = CustomUserChangeForm
#     model = User
#     list_display = ['username', 'email', 'is_staff',
#                     'is_teacher']  # new


admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(OrigenClass)
admin.site.register(Grade)
