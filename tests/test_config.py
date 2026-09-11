from config.settings import BASE_URL


def test_base_url_is_configured():
    assert BASE_URL
    assert BASE_URL.startswith("http")