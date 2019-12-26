from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Subject(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                            related_name='Topics', db_index=True)
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        # unique_together = (('parent', 'slug',))
        verbose_name_plural = 'Subjects'

    # def get_slug_list(self):
    #     try:
    #         ancestors = self.get_ancestors(include_self=True)
    #     except:
    #         ancestors = []
    #     else:
    #         ancestors = [i.slug for i in ancestors]
    #     slugs = []
    #     for i in range(len(ancestors)):
    #         slugs.append('/'.join(ancestors[:i + 1]))
    #     return slugs

    def __str__(self):
        return self.name
