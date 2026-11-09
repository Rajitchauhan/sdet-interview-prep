

import pytest


@pytest.fixture
def config_info(request):
    print(request.config)


def test_config(config_info):
    pass