from rest_framework import serializers
from .models import *

class API(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('Name','Email_Address','Phone_Number','id')
        
class Spamapi(serializers.ModelSerializer):
    class Meta:
        model=SpamReports
        fields=('mobspam','report_count')        