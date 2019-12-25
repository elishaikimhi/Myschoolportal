from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from .utils import upload_location, phone_regex


# Add fields to user module and uplaod image to the media location
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'teacher'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,
                                                 blank=True,
                                                 null=True
                                                 )  # user type
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=11,
                                    blank=True
                                    )  # validators should be a list
    profile_image = models.ImageField(upload_to=upload_location,
                                      blank=True,
                                      default='test.png',
                                      height_field='height_field',
                                      width_field='width_field',
                                      )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

# main student module


class Student(models.Model):
    user = models.OneToOneField(
        User, related_name='student', on_delete=models.CASCADE)
    origen_class = models.ForeignKey(
        'OrigenClass', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

# main teacher module


class Teacher(models.Model):
    user = models.OneToOneField(
        User, related_name='teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# using signal to save changes in users into students or teachers
# TBD when changing from teacher to student need to check if already exsit in one list and delete him
@receiver(post_save, sender=User)
def append_to_user_type(sender, **kwargs):
    if kwargs.get('created', False):
        if kwargs.get('instance').user_type == 2:
            Teacher.objects.get_or_create(user=kwargs.get('instance'))
        elif kwargs.get('instance').user_type == 1:
            Student.objects.get_or_create(user=kwargs.get('instance'))
    elif not kwargs.get('instance')._state.adding:
        if kwargs.get('instance').user_type == 2:
            Teacher.objects.get_or_create(user=kwargs.get('instance'))
        elif kwargs.get('instance').user_type == 1:
            Student.objects.get_or_create(user=kwargs.get('instance'))


class Grade(models.Model):
    GRADE_CHOICES = (
        (1, 'Grade 10'),
        (2, 'Grade 11'),
        (3, 'Grade 12'),
    )
    grade = models.PositiveSmallIntegerField(
        choices=GRADE_CHOICES, blank=True, null=True)  # Grade type

    def __str__(self):
        return self.GRADE_CHOICES[self.grade - 1][1]


class OrigenClass(models.Model):
    grade = models.OneToOneField(
        Grade, related_name='Grade', on_delete=models.CASCADE)
    class_name = models.PositiveIntegerField(blank=True, null=True)
    head_teacher = models.OneToOneField(
        Teacher, related_name='head_teacher', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.grade} Class {self.class_name}'
