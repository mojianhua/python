from rest_framework import serializers
from api02 import models as Api02Models

class pagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Api02Models.Role
        fields = '__all__'