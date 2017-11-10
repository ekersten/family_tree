from app.models import Person
from app.models import Couple


from rest_framework import serializers



class ShortPersonSerializer(serializers.HyperlinkedModelSerializer):
    pass


class ProvinceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_field='slug', view_name='province-detail')

    class Meta:
        model = Province
        fields = ('url', 'name')


class ExperienceListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(lookup_field='slug', view_name='experience-detail')

    class Meta:
        model = Experience
        fields = ('url', 'name',)


class ProvincesExperienceListSerializer(serializers.HyperlinkedModelSerializer):
    experiences = ExperienceListSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(lookup_field='slug', view_name='province-detail')

    class Meta:
        model = Province
        fields = ('url', 'name', 'experiences')
