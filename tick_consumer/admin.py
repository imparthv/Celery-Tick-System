from django.contrib import admin
from .models import Broker, Script, Ticks
# Register your models here.

@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display =('id','type', 'name', 'created_at', 'updated_at')
    search_fields = ('type', 'name')
    list_filter = ('type')
    ordering = ('id')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Script)
class ScriptAdmin(admin.ModelAdmin):
    list_display = ("id", "broker", "name", "trading_symbol", "created_at", "updated_at")
    search_fields = ("name", "trading_symbol")
    list_filter = ("broker",)
    ordering = ("id",)
    readonly_fields = ("created_at", "updated_at")

@admin.register(Ticks)
class TicksAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "script",
        "tick_value",
        "volume",
        "received_at_producer",
        "created_at",
    )
    search_fields = ("script__trading_symbol",)
    list_filter = ("script",)
    ordering = ("-id",)
    readonly_fields = ("created_at", "updated_at")