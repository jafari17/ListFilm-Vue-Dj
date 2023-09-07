from rest_framework import serializers

from api.models import Projects


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'film', 'director', 'year', 'star', 'complete', 'slug']