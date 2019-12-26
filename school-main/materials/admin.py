from django.contrib import admin
# from mptt.admin import MPTTModelAdmin
from .models import Subject
# admin.site.register(Subject, MPTTModelAdmin)
# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from import_export.admin import ImportExportActionModelAdmin, ImportExportMixin
from .resources import SubjectResource




@admin.register(Subject)
class SubjectAdmin(ImportExportActionModelAdmin, DraggableMPTTAdmin):
    resource_class = SubjectResource


# admin.site.register(
#     Subject,
#     DraggableMPTTAdmin,
#     list_display=(
#         'tree_actions',
#         'indented_title',
#         # ...more fields if you feel like it...
#     ),
#     list_display_links=(
#         'indented_title',
#     ),
# )

# admin.site.register(Subject, SubjectAdmin)