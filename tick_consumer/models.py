from django.db import models
from django.utils import timezone

# Create your models here.

# Represents the exchange provider from which market data is being streamed
class Broker(models.Model):
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    api_config = models.JSONField(default=dict)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} ({self.type})"
    
# Represents the specific trading instrument that is being monitored
class Script(models.Model):
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE, related_name='scripts')
    name = models.CharField(max_length=100)
    trading_symbol = models.CharField(max_length=50)
    additional_data = models.JSONField(default=dict, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} - {self.trading_symbol}"
    
# Stores live price movements
class Ticks(models.Model):
    script = models.ForeignKey(Script, on_delete=models.CASCADE, related_name='ticks')
    tick_value = models.DecimalField(max_digits=20, decimal_places=10)
    volume = models.DecimalField(max_digits=30, decimal_places=10, null=True, blank=True)

    received_at_producer = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Tick {self.script.trading_symbol} @ {self.tick_value}"
