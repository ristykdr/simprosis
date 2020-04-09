# from import_export import resources
# from . models import mahasiswa
# from django.db import IntegrityError

# class mahasiswaResource(resources.ModelResource):
#     class Meta:
#         model = mahasiswa
#         skip_unchanged = True
#         report_skipped = False
#         fields = (
#             'id',
#             'npm',
#             'nama',
#         )

#     def save_instance(self, instance, using_transactions=True, dry_run=False):
#         try:
#             super(mahasiswaResource, self).save_instance(
#                 instance, using_transactions, dry_run)
#         except IntegrityError:
#             pass
