import pytest

from lang_detector.models import Snippet
from rest_framework.test import APIClient


@pytest.fixture()
def valid_snippet():
    """
    Make fixture that returns valid snippet.
    """
    data = {
        "id": "F51DE427-6694-490C-A90B-055B156052EC",
        "text": "Continental does not have an office in Zürich."
    }
    return Snippet.objects.create(**data)


@pytest.fixture()
def second_valid_snippet():
    """
    Make fixture that returns second valid snippet.
    """
    data = {
        "id": "47CB9661-520D-4674-B79B-B0A1FD3805F1",
        "text":
            """
            The report reveals that Bridgestone, Michelin, Goodyear, Pirelli and
            Continental are few of the dominant tyre manufacturers in the UAE,
            accounting for a substantial share in the country's tyre market. These
            leading players are constantly growing due to their well-established
            supply chain network, comprising exclusive distributorships and local
            dealers.
            """
    }
    return Snippet.objects.create(**data)


@pytest.fixture()
def create_client():
    client = APIClient()
    return client
