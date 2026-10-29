from config.settings import validate_api_key_value


def test_validate_api_key_accepts_normal_key():
    assert validate_api_key_value("sk-test-abc123", "OPENAI_API_KEY") == "sk-test-abc123"


def test_validate_api_key_rejects_url_like_open_meteo_value():
    assert validate_api_key_value(
        "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}",
        "OPEN_METEO_API_KEY",
    ) is None
