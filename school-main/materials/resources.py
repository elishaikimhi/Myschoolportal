from import_export import resources
from .models import Subject
from django.db import IntegrityError


class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subject
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('name',)
        fields = ('name', 'slug', 'id', 'parent',)
        exclude = ('lft',
                   'rght',

                   'tree_id',
                   'level',



                   )

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        # Clear out anything that may be there from a dry_run,
        #  such as the admin mixin preview
        self.set_unique = set()

    def skip_row(self, instance, original):
        name = instance.name
        slug = instance.slug
        parent = instance.parent
        tuple_unique = (name, parent, slug)

        if tuple_unique in self.set_unique:
            return True
        else:
            self.set_unique.add(tuple_unique)
        return super(SubjectResource, self).skip_row(instance, original)
    
    def save_instance(self, instance, using_transactions=True, dry_run=False):
        try:
            super(SubjectResource, self).save_instance(
                instance, using_transactions, dry_run)
        except IntegrityError:
            pass
