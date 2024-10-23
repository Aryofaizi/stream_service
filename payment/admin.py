from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """payment model admin."""
    model = Payment
    list_display = ["user",
        "plan",
        "amount",
        "is_paid",
        "has_been_sent",
        "datetime_created",
        "datetime_modified",
        "zarinpal_authority",
        "zarinpal_ref_id",
        "truncate_zarinpal_data",]
    

    def truncate_zarinpal_data(self, obj):
        return obj.zarinpal_data[:30] + "..." if len(obj.zarinpal_data) > 30 else obj.zarinpal_data
    truncate_zarinpal_data.short_description = "zarinpal_data"
