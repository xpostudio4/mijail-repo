from rest_framework import serializers

from user_tasks.models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    User = serializers.CharField(source='user.full_name', read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']
        validated_data['user'] = request.user
        created_task = Task.objects.create(**validated_data)
        return created_task