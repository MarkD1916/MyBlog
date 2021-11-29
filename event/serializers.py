from rest_framework import serializers
from .models import Event, Tech


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['event_title', 'event_date', 'event_image_icon', 'event_type', 'production_icon', 'event_github_link',
                  'event_production_link', 'event_title_date_color']


class TechSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tech
        fields = ['tech_name', 'tech_link', 'event']
