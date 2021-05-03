import pytest
from _pytest.fixtures import fixture
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

from user_tasks.models import Project, Tag, Epic


@fixture
def api_client():
    return APIClient()


@fixture
def project():
    return Project.objects.create(title='new_title')


@fixture
def epic(project):
    return Epic.objects.create(title='new_epic', project=project)


@fixture
def tags():
    tag_list = []
    for index in range(3):
        tag = Tag.objects.create(title='new_title')
        tag_list.append(tag.id)
    return tag_list


@fixture
def user():
    return User.objects.create(username='new_username', email='email@test.com')


@pytest.mark.django_db
def test_create_project(api_client):
    url = reverse('project-list')
    data = {'title': 'new_title_project'}
    response = api_client.post(url, data=data)
    print(response)
    data = response.json()
    assert response.status_code == 201
    assert data['title'] == 'new_title_project'
    assert 'id' in data


@pytest.mark.django_db
def test_create_project_as_request_if_title_empty(api_client):
    url = reverse('project-list')
    data = {'title': ''}
    response = api_client.post(url, data=data)

    data = response.json()
    assert response.status_code == 400
    assert 'title' in data


@pytest.mark.django_db
def test_update_project(api_client, project):
    url = reverse('project-detail', kwargs={'pk': project.id})
    data = {'title': 'new_project_name'}
    response = api_client.put(url, data=data)

    data = response.json()
    assert response.status_code == 200
    assert data['title'] == 'other title'


@pytest.mark.django_db
def test_create_task(api_client, tags, user, epic):
    url = reverse('task-list')
    data = {
        'title': 'new_task',
        'type': 'feature',
        'tags': tags,
        'status': 'created',
        'priority': 'normal',
        'description': 'new task created',
        'owners': [user.id],
        'linked_tasks': [],
        'epic': epic
    }
    response = api_client.post(url, data=data)
    data = response.json()
    assert response.status_code == 201
    assert data['title'] == 'new_task'
    assert 'id' in data
