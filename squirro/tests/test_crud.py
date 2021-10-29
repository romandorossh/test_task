import json

import pytest
from django.urls import reverse
from rest_framework import status

from lang_detector.models import Snippet
from lang_detector.serializers import SnippetSerializer


@pytest.mark.django_db
def test_uniqueness_snippet(valid_snippet):
    """
    Ensure we can't save the same snippet
    """
    valid_snippet.save()
    valid_snippet.save()
    assert Snippet.objects.count() == 1


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            {"id": "C3DABBD8-E411-4477-8711-A0E185717B09", "text": "Continental does not have an office in Zürich."},
            "de"
        ),
        (
            {"id": "C3DABBD8-E411-4477-8711-A0E185717B09", "text": "This is the english language!"},
            "en"
        ),
    ]
)
@pytest.mark.django_db
def test_serialize_snippet(data, expected):
    """
    Ensure we can create a new snippet with proper language
    """
    snippet_ser = SnippetSerializer(data=data)

    assert snippet_ser.is_valid()
    snippet = snippet_ser.save()

    assert snippet.id == data["id"]
    assert snippet.language == expected


@pytest.mark.parametrize(
    "data, expected_code",
    [
        (
            {"id": "C3DABBD8-E411-4477-8711-A0E185717B09", "text": "Continental does not have an office in Zürich."},
            status.HTTP_201_CREATED
        ),
        (
            {"id": "", "text": "This is the english language!"},
            status.HTTP_400_BAD_REQUEST
        ),
    ]
)
@pytest.mark.django_db
def test_create_valid_snippet(data, client, expected_code):
    response = client.post(
        reverse("snippets"),
        data=json.dumps(data),
        content_type="application/json"
    )
    assert response.status_code == expected_code


@pytest.mark.django_db
def test_get_all_snippets(valid_snippet, second_valid_snippet, client):
    """
    Ensure we can retrieve all snippets
    """
    response = client.get(reverse("snippets"))
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, many=True)

    assert response.data == serializer.data
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_valid_single_snippet(valid_snippet, client):
    """
    Ensure we can retrieve snippet by id
    """
    response = client.get(
        reverse("snippets-detail", kwargs={"pk": valid_snippet.id})
    )
    snippet = Snippet.objects.get(pk=valid_snippet.id)
    serializer = SnippetSerializer(snippet)

    assert response.data == serializer.data
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_invalid_single_snippet(client):
    """
    Ensure we can retrieve 404 when pass invalid id
    """
    response = client.get(
        reverse("snippets-detail", kwargs={"pk": "invalid-id"})
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.parametrize(
    "data, expected_language, expected_code",
    [
        (
            {
                "id": "F51DE427-6694-490C-A90B-055B156052EC",
                "text": "Elitr expetenda nam an, Die unendliche Geschichte ei reque euismod assentior."
             },
            "de",
            status.HTTP_200_OK
        ),
        (
            {"id": "F51DE427-6694-490C-A90B-055B156052EC", "text": ""},
            None,
            status.HTTP_400_BAD_REQUEST
        ),
    ]
)
@pytest.mark.django_db
def test_update_snippet(valid_snippet, data, expected_language, expected_code, client):
    """
    Ensure we can update snippet
    """
    response = client.put(
        reverse("snippets-detail", kwargs={"pk": valid_snippet.id}),
        data=json.dumps(data),
        content_type="application/json"
    )
    assert response.status_code == expected_code
    assert response.data.get("language") == expected_language


@pytest.mark.django_db
def test_delete_snippet(valid_snippet, client):
    response = client.delete(
        reverse("snippets-detail", kwargs={"pk": valid_snippet.id})
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
