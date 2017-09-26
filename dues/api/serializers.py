from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Transaction
        
        fields = ('id', 'name', 'date_created', 'date_modified', 'user_to', 'user_from', 'value')

        read_only_fields = ('date_created', 'date_modified')