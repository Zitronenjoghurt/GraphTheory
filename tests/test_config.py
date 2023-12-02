from src.classes.config import Config

def test_init():
    config = Config()

    assert config is not None
    assert config.config is not None

    assert config.get_option('decimal_places') == 2