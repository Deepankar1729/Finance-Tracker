from django.contrib import admin
from .models import Transaction, Goal
from import_export import resources
from import_export.admin import ExportMixin

# Register your models here.

class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction
        fields = ('date', 'title', 'amount', 'transaction_type', 'category')
        export_order = ('date', 'title', 'amount', 'transaction_type', 'category')


class TransactionAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TransactionResource
    list_display = ('user', 'title', 'amount', 'transaction_type', 'created_at')
    list_filter = ('user', 'transaction_type', 'created_at')
    search_fields = ('title',)


class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'target_amount', 'deadline')
    list_filter = ('user',)
    search_fields = ('name',)


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Goal, GoalAdmin)